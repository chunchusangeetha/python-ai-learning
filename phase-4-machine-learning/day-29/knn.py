import pandas as pd
from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix

dataset = load_dataset("aai510-group1/telco-customer-churn")
df = pd.DataFrame(dataset['train'])

# 1. Remove hidden spaces from column names
df.columns = df.columns.str.strip()

# Drop the noise/leakage/unusefull columns
cols_to_drop = ['Customer ID ','Churn Category', 'Churn Reason', 'Latitude', 'Longitude', 'Zip Code','Churn Score',
    'Customer Status',
    'CLTV',
    'Total Revenue']

cleaned_df = df.drop(columns = cols_to_drop , errors = 'ignore')
print(cleaned_df.head(5))

X = cleaned_df.drop('Churn', axis=1)
y= cleaned_df["Churn"]

cat_cols = X.select_dtypes(include=['object','string']).columns
num_cols = X.select_dtypes(exclude=['object']).columns

# Split categorical
low_card_cols = [col for col in cat_cols if X[col].nunique() < 10]
high_card_cols = [col for col in cat_cols if X[col].nunique() >= 10]

# Drop high-cardinality columns
X = X.drop(columns=high_card_cols)

# Encode only safe columns
X = pd.get_dummies(X, columns=low_card_cols, drop_first=True)

# Reduce memory
X = X.astype('float32')

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scale = StandardScaler()

X_train_scaled = scale.fit_transform(X_train)
X_test_scaled = scale.transform(X_test)

for k in [3,5,7]:
    print(f"metric scores for n_neighbors = {k}::: "*40)
    model = KNeighborsClassifier(n_neighbors=k)

    model.fit(X_train_scaled,y_train)

    y_pred = model.predict(X_test_scaled)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("precision_score:", precision_score(y_test, y_pred))
    print("recall_score:", recall_score(y_test, y_pred))
    print("confusion_matrix:", confusion_matrix(y_test, y_pred))