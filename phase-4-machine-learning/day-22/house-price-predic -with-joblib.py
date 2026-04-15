import joblib

# 1. Load the 'brain' we saved earlier
model = joblib.load('house_model.pkl')

# 2. Use it immediately
# Predict for: 2500 sqft, 4 beds, 5 years old
new_house = [[2500, 4, 5]]
prediction = model.predict(new_house)

print(f"Prediction from loaded model: {prediction[0]:,.2f}")