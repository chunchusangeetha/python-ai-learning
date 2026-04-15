import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv("insurance_data.csv")

df["random_noise"] = np.random.rand(len(df))
X = df[["age","bmi","smoker","random_noise"]]
y = df["charges"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Scores
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"Training Score: {train_score:.2f}")
print(f"Testing Score: {test_score:.2f}")