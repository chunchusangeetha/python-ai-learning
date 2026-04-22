import pandas as pd
from datasets import load_dataset
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, recall_score

# Load dataset
dataset = load_dataset("aai510-group1/telco-customer-churn")
df = pd.DataFrame(dataset['train'])

# Clean column names
df.columns = df.columns.str.strip()

# Drop unnecessary columns
cols_to_drop = [
    'Customer ID ', 'Churn Category', 'Churn Reason',
    'Latitude', 'Longitude', 'Zip Code', 'Churn Score',
    'Customer Status', 'CLTV', 'Total Revenue'
]
df = df.drop(columns=cols_to_drop, errors='ignore')

# Features & target
X = df.drop('Churn', axis=1)
y = df['Churn']

# Handle categorical data
cat_cols = X.select_dtypes(include=['object','string']).columns

# Drop high-cardinality columns
high_card_cols = [col for col in cat_cols if X[col].nunique() > 10]
X = X.drop(columns=high_card_cols)

# Encode
X = pd.get_dummies(X, drop_first=True)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 🔥 Grid Search
param_grid = {
    'C': [0.1, 1, 10, 50],
    'kernel': ['linear', 'rbf'],
    'gamma': ['scale', 0.1, 0.01]
}

grid = GridSearchCV(
    SVC(),
    param_grid,
    cv=3,
    scoring='recall',   # IMPORTANT (churn problem)
    n_jobs=-1
)

grid.fit(X_train_scaled, y_train)

# Best model
best_model = grid.best_estimator_

print("Best Parameters:", grid.best_params_)

# Predict
y_pred = best_model.predict(X_test_scaled)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))