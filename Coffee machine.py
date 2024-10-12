menu = {
    'espresso': { 
        'ingridents': {
            'water': 50,
            'milk': 0,
            'coffee': 18
        },
        'cost': 1.5
    },
    'latte': {
        'ingridents': {
            'water': 200,
            'milk': 150,
            'coffee': 24
        },
        'cost': 2.5
    },
    'cappuccino': {
        'ingridents': {
            'water': 250,
            'milk': 100,
            'coffee': 24
        },
        'cost': 3.0
    }
}
resources = {
    'water': 1000,
    'milk' : 500,
    'coffee' : 200,
    'money' : 0
}
def check_resource(ingridents):
    can_make = True
    for item in ingridents:
        if ingridents[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            can_make = False
    return can_make
def coin_input():
    print("Please insert Coins")
    quarter = int(input("How many Quarters?: "))
    dime = int(input("How many dime?: "))
    nickle = int(input("How many nickle?: "))
    penny = int(input("How many Penny?: "))
    paid = 0.25*quarter + 0.1*dime + 0.05*nickle + 0.01*penny
    return paid
def make_coffee(ingridents):
    resources['coffee'] -= ingridents['coffee']
    resources['water'] -= ingridents['water']
    resources['milk'] -= ingridents['milk']
is_on = True

while is_on:
    choice = str(input("What would you like?(espresso/latte/cappuccino) "))

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f'Water: {resources["water"]}ml\nMilk :{resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}')
    else:
        requirement = menu[choice]
        if check_resource(requirement['ingridents']):
            paid = coin_input()
            if paid < requirement['cost']:
                print("Sorry that's not enough money. Money refunded.")
            elif paid > requirement['cost']:
                change = round((paid -requirement['cost']),2)
                print(f'Here is ${change} in change')
                resources['money'] = requirement['cost']
                make_coffee(requirement['ingridents'])
                print(f"Here is your {choice}. Enjoy!")
            else:
                resources['money'] = paid
                make_coffee(requirement['ingridents'])
                print(f"Here is your {choice}. Enjoy!")