import json


userJSON = '{"first_name":"John", "last_name":"Miracle", "age":12}'

user = json.loads(userJSON)

print(user)
print(user["last_name"])
print("\n\n")

car = {"make": "Ford",
       "model": "Mustang",
       "release_year": 2019
       }

carJSON = json.dumps(car)

print(carJSON)

for k, v in car.items():
    print(k, v)

