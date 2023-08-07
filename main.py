from data import MENU,resources
is_on=True
profit=0
def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item]>resources[item]:
            print("Sorry there is not enough {item}")
            return False
        return True
def process_coins():
    total=int(input("number of quarters"))*0.25
    total+= int(input("number of quarters")) * 0.10
    total+= int(input("number of quarters")) * 0.01
    total+= int(input("number of quarters")) * 0.05
    return total


def transaction_successful(payment,drink_cost):
    global profit
    if payment >= drink_cost:
       profit+=payment
       balance=payment-drink_cost
       print(f"Here is your change {balance}$")
       return True
    else:
        print("that's not enough money")
        return False
def make_coffee(drink,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink}")
while is_on:
    choice=input("what would you like?(espresso/latte/cappuccino): ")
    if choice=='off':
        is_on=False
    elif choice=='report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"profit: {profit}$")


    else:
        drink=MENU[choice]
        if  is_resource_sufficient(drink['ingredients']):
            if transaction_successful(process_coins(),drink['cost']):
                make_coffee(choice,drink['ingredients'])





