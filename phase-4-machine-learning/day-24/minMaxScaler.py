import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler

df= pd.read_csv('housing-data.csv')

# the features are not in the same range
# price -cr,area-thousands,bedrooms,bathrooms,stories, parking-ones,
print(df.head(5))


## Checking is any null values in dataset
print(df.isnull().sum())

X = df[["area", "bedrooms", "bathrooms", "stories", "parking"]]
y= df["price"]

#split the data into train,test data with train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# scaling the data with MinMaxScaler to get more accuracy score
scaler = MinMaxScaler()

#trained data scaling
X_scaled_train_data = scaler.fit_transform(X_train)

#test data scaling
X_scaled_test_data = scaler.transform(X_test)

# model creation using LinearRegression
model1 = LinearRegression()
model2 = LinearRegression()

#train the model with scaled tarin data
model1.fit(X_train,y_train)
model2.fit(X_scaled_train_data,y_train)

# predict the result
y_predict_without_scaling = model1.predict(X_test)
y_predict = model2.predict(X_scaled_test_data)

## Evaluate
score_without_scaling = r2_score(y_test,y_predict_without_scaling)
score_withscaling = r2_score(y_test,y_predict)

# train,test model scores
train_score = model2.score(X_scaled_train_data, y_train)
test_score = model2.score(X_scaled_test_data, y_test)

#task2
print(X_scaled_train_data[:5])

print(f"Model Accuracy without Scaling: {score_without_scaling:.2f}")
print(f"Model Accuracy after Scaling: {score_withscaling:.2f}")

print(f"Training Score: {train_score:.2f}")
print(f"Testing Score: {test_score:.2f}")
