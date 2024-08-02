import json

import requests
from main import app

# TODO: send a GET using the URL http://127.0.0.1:8000
url = "http://127.0.0.1:8000"
r = requests.get(url)

# TODO: print the status code
print(r.status_code)

# TODO: print the welcome message
print(r.json())



data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# TODO: send a POST using the data above
response = requests.post(f"{url}/data/", data)


# TODO: print the status code
print(response.status_code)

# TODO: print the result
print(response.json())
