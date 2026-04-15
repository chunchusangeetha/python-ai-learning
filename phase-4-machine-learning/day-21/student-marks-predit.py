import numpy as np
from sklearn.linear_model import LinearRegression

# number of hours students are studied
X = np.array([[4],[6],[2],[9],[5],[3],[6]])

# number of marks student get
y = np.array([36,72,30,57,43,37,59])

model =  LinearRegression();
model.fit(X,y)

# predicting the 7 hours studied marks
predict_marks = model.predict([[7]])

print(f"predict the marks for 7 hours studied sudnet:{predict_marks[0]}")

print("Slope (coef):", model.coef_[0])
print("Intercept:", model.intercept_)