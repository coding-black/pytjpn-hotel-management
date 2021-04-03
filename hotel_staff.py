avalible_items = {}

print("press q to quit ")

def cust():
    while True:
        print('OK\n')

        cust = input("enter your item you want to oder : ")

        if cust in avalible_items:
            print("thanks for oder")

        elif cust == 'q':
            break
        else:
            print("sorry we don't have that item")

def manage():
    while True:
        manager = input("enter your items : ")
        if manager != 'q':
            price = input("enter the item price : ")
            avalible_items[manager] = price
        
        else:
            break

def bill():
    name = input('Enter your name :- ')
    file = open(f'{name}.txt', 'a', encoding='utf-8')
    file.writelines(f'Hello, {name}. Good to see you at our hotel.')
    file.writelines('\n')
    file.writelines('\n')
    file.writelines(f'{avalible_items}')
    file.writelines('\n')

print(avalible_items)
