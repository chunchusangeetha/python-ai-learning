import json

# Data to be written
user_data = {
  "name": "Sangeetha",
  "age": 25,
  "skills": ["React", "Python"]
}

with open("user.json","w") as f:
    json.dump(user_data,f,indent=4)
    print("File 'user.json' created successfully!")