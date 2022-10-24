Usernamelogin=input('User name : ')
Passwordlogin=input('Password : ')
if Usernamelogin=='admin' and Passwordlogin=='123456789':
    print('successful login')
    print('---Select a product list---')
    print('1.Book 1 : 120 THB')
    print('2.Book 2 : 150 THB')
    print('3.Book 3 : 170 THB')
    print('4.Book 4 : 200 THB')
    Selectlist=int(input('Enter the selected item : '))
    if Selectlist >= 1 and Selectlist <=4:
        Productneeded=int(input('Number of products needed : '))
        if Selectlist == 1:
            totalprice=120*Productneeded
            print('---Total price =',totalprice,'THB---')
        elif Selectlist == 2:
            totalprice=150*Productneeded
            print('---Total price =',totalprice,'THB---')
        elif Selectlist == 3:
            totalprice=170*Productneeded
            print('---Total price =',totalprice,'THB---')
        elif Selectlist == 4:
            totalprice=200*Productneeded
            print('---Total price =',totalprice,'THB---')
    else:
        print('---You entered incorrect information---')
else:
    print('---Login failed---')