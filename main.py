"""creating a Dictionary of Menu and resources required , cost and Resources available in the coffe machine"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print("1-Menu:\n    1-Espresso--1.5\n    2-Latte--2.5\n    3-Cappuccino--3.0\n2-Report(Machines resources)")
order = input("What would you like to have? ").lower()
if order == "report":
    print(resources)