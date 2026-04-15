import numpy as np
from sklearn.linear_model import LinearRegression



X = np.array([[1], [9], [3], [4], [15]])


y = np.array([20300, 30700, 40800, 59000, 65000])


model = LinearRegression()


model.fit(X, y)


predicted_salary = model.predict([[6]])

print(f"Predicted salary for 6 years experience: {predicted_salary[0]}")