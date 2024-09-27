import json
import os

file_name = 'users.json'


def saveUser(id, fullname, username, email, phone):
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            json.dump([], file)

    with open(file_name, "r") as f:
        users = json.load(f)

    users.append({
        "id": id,
        "fullname": fullname,
        "username": username,
        "email": email,
        "phone": phone
    })

    with open(file_name, "w") as f:
        json.dump(users, f)


def checkUser(id):
    with open(file_name, "r") as f:
        users = json.load(f)

    for user in users:
        if user["id"] == id:
            return True

    return False
