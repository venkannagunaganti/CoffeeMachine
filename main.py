from data import MENU,profit,resources
water_available=0
milk_available=0
coffee_available=0
def resources_available(Flavour, resource):
    if resource=="water":
      return int(MENU[Flavour]['ingredients'][resource])
    elif resource=='milk':
      return int(MENU[Flavour]['ingredients'][resource])
    elif resource=='coffee':
      return int(MENU[Flavour]['ingredients'][resource])


def price_of_resource(resource):
    return MENU[resource]['cost']

def resource_available(ingredient):
    global water_available
    global coffee_available
    global milk_available
    if ingredient=="water":
        water_available= resources[ingredient]
        return water_available
    elif ingredient=='milk':
        milk_available=resources[ingredient]
        return milk_available
    elif ingredient=="coffee":
        coffee_available=resources[ingredient]
        return coffee_available


def quantity_available(type_of_ingredient):
    """this takes type of ingredient as input and returns value of that corressponding input"""
    return resources_available(user_choice,type_of_ingredient)


def check_quantity_expresso():
    global water_available
    global coffee_available
    global milk_available
    water_available = resource_available('water')
    coffee_available = resource_available('coffee')
    milk_available=resource_available('milk')
    if water_available >= quantity_available('water') and coffee_available >= quantity_available('coffee'):
        water_available-=quantity_available('water')
        coffee_available-=quantity_available('coffee')
        print("enjoy your coffee")
    elif water_available < quantity_available('water'):
        print("Sorry there is not enough water")
    elif coffee_available < quantity_available('coffee'):
        print("Sorry there is not enough coffe")
def check_quantity_latte():
    if quantity_available("water") >= 200 and quantity_available("coffee") >= 24 and quantity_available("milk")>=150:
        print("enjoy your coffee")
    elif quantity_available("water") < 200:
        print("Sorry there is not enough water")
    elif quantity_available("coffee") < 24:
        print("Sorry there is not enough coffee")
    elif quantity_available("milk"):
        print("Sorry there is not enough milk")

def check_availability(water_available,coffee_available,milk_available):
        # global water_available
        # global coffee_available
        # global milk_available
        # water_available = resource_available('water')
        # coffee_available = resource_available('coffee')
        # milk_available = resource_available('milk')
        if water_available >= quantity_available("water") and  coffee_available>= quantity_available('coffee') and milk_available>=quantity_available("milk"):
            water_available-=quantity_available('water')
            coffee_available-=quantity_available('coffee')
            milk_available-=quantity_available('milk')
            print("enjoy your coffee")
        elif water_available < quantity_available('water'):
            print("Sorry there is not enough water")
        elif coffee_available < quantity_available('coffee'):
            print("Sorry there is not enough coffee")
        elif milk_available<quantity_available('milk'):
            print("Sorry there is not enough milk")
water_available=resource_available('water')
coffee_available=resource_available('coffee')
milk_available=resource_available("milk")
run=True
while run:

    user_choice=input('what would you like?(espresso/latte/cappuccino) ').lower()

    if user_choice=="espresso":
        check_quantity_expresso()
    elif user_choice=="latte":
        check_availability(water_available,coffee_available,milk_available)
    elif user_choice=='cappuccino':
        check_availability()
    elif user_choice == 'report':
        print(f"water: {water_available}\ncoffee: {coffee_available}\nmilk: {milk_available} ")
    elif user_choice=='s':
        run=False
