import pandas as pd
from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Models
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
dataset = load_dataset("aai510-group1/telco-customer-churn")
df = pd.DataFrame(dataset['train'])

# Clean column names
df.columns = df.columns.str.strip()

# Drop leakage / useless columns
cols_to_drop = [
    'Customer ID ', 'Churn Category', 'Churn Reason',
    'Latitude', 'Longitude', 'Zip Code',
    'Churn Score', 'Customer Status', 'CLTV', 'Total Revenue'
]

df = df.drop(columns=cols_to_drop, errors='ignore')

# Features & target
X = df.drop('Churn', axis=1)
y = df['Churn']

# Handle categorical columns
cat_cols = X.select_dtypes(include=['object','string']).columns

# Drop high-cardinality columns
low_card_cols = [col for col in cat_cols if X[col].nunique() < 10]
X = X.drop(columns=[col for col in cat_cols if col not in low_card_cols])

# One-hot encoding
X = pd.get_dummies(X, columns=low_card_cols, drop_first=True)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale (important for SVM & KNN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Models
models = {
    "SVM": SVC(C=50, kernel='linear'),
    "RandomForest": RandomForestClassifier(n_estimators=50, random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=7)
}

print("📊 Model Comparison Results:\n")

for name, model in models.items():
    
    # Use scaled data for SVM & KNN
    if name in ["SVM", "KNN"]:
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)

    print(f"{name}")
    print(f"Accuracy: {acc:.3f}")
    print(f"Precision: {prec:.3f}")
    print(f"Recall: {rec:.3f}")
    print("-" * 30)