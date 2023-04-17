employee = {
    "name": "Adam",
    "email": "adam@example.com",
    "rank": "programmer",
    "salary": 8000
    }

def promoteToManager(user):
    if user["rank"] == "manager":
        print("Pracownik już jest managerem")
        return
    user["rank"] = "manager"
    user["salary"] *= 1.5

promoteToManager(employee)
print(employee)