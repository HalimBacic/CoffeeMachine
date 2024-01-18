from Data.menu import MENU, resources

print('CoffeeMachine v1.0.0')

cmd = "-"
bank = 0

def printReport():
    print("Water:" + resources['water'])
    print("Milk:" + resources['milk'])
    print("Coffee:" + resources['coffee'])
    print("Bank status:" + bank);

def checkCoffee(cmd):
    if cmd == 'es':
        if resources['water'] < MENU['espresso']['water'] or resources['coffee'] < MENU['espresso']['coffee']:
            return 0
        return 1;
    if cmd == 'la':
        if resources['water'] < MENU['latte']['water'] or resources['coffee'] < MENU['latte']['coffee'] or resources['milk'] < MENU['latte']['milk']:
            return 0
        return 1;
    if cmd == 'ca':
        if resources['water'] < MENU['cappuccino']['water'] or resources['coffee'] < MENU['cappuccino']['coffee'] or resources['milk'] < MENU['cappuccino']['milk']:
            return 0
        return 1;

def insertCoins(cmd):
    print("Insert coins")
    q = int(input("How many quarters?"))
    d = int(input("How many dimes?"))
    n = int(input("How many nickles?"))
    p = int(input("How many pennies?"))
    count = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    if MENU[cmd]['cost'] < count:
        return 0
    elif MENU[cmd]['cost'] > count:
        change = count - MENU[cmd]['cost']
        print(f"You have {change} change.")
    bank += count
    bank -= change
    return 1

def makeCoffee(cmd):
    if cmd == 'es':
        resources['water'] -= MENU['espresso']['water']
        resources['coffee'] -= MENU['espresso']['coffee']
    elif cmd == 'la':
        resources['water'] -= MENU['latte']['water']
        resources['coffee'] -= MENU['latte']['coffee']
        resources['milk'] -= MENU['latte']['coffee']
    elif cmd == 'ca':
        resources['water'] -= MENU['cappuccino']['water']
        resources['coffee'] -= MENU['cappuccino']['coffee']
        resources['milk'] -= MENU['cappuccino']['coffee']



print("Which coffee you want? (es) espresso - (la) latte - (ca) cappuccino")
cmd = input()

while cmd != off:
    if cmd == 'report':
        printReport()
    elif cmd == 'es' or cmd == 'es' or cmd == 'es':
        if checkCoffee(cmd) == 1:
            if insertCoins(cmd) == 1:
                makeCoffee(cmd)
    elif cmd != 'off':
        print('Unknown function')
