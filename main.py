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
money = {"quarters": 0 ,
         "dimes": 0 ,
         "nickles": 0 ,
         "pennies": 0,
         }


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def calculate_money(quarters,dimes,nickles,pennies):
    return int(quarters*0.25+ dimes*0.1+ nickles*0.05+pennies*0.01)


def ingredients(drink):
    """will return the ingredients which contains another dictionary and the cost of the item """
    return MENU["drink","ingredients"]

def check_resource(drink):
    if ingredients(drink)["water"] > resources["water"] or ingredients(drink)["milk"] > resources["milk"]:
        print("sorry not enough resources")


continue_operating= True
#TODO: prompt
while continue_operating:
    prompt = input("What would you like? (espresso/latte/cappuccino):").lower()
    if prompt == "espresso":



    elif prompt == "latte":



    elif prompt == "cappuccino":



    elif prompt == "report":
        print(resources)


    elif prompt == "off":
        continue_operating= False