import os
from getpass import getpass

# hotel_staff.func()

while True:

    type = input('''
1. Customer
2. Hotel Staff
3. bill
4. exit 

Type your type here :- ''')

    def customer(): 
       from hotel_staff import cust
       cust()

    def hotel_staff():
        from hotel_staff import manage
        manage()

    def bill_File():
        from hotel_staff import bill
        bill()

    if type == '1':
        customer()
            
    elif type == '2':
        passwd = getpass('Enter your code :- ')
        if passwd == 'dev':
            hotel_staff()
        

        else: 
            print('invalid passwd')


    elif type == '3':
        bill_File()
        print('Bill formed')

    else:
        break


    