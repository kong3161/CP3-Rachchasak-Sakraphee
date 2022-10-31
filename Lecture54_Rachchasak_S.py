vat = 7
def Login():
    userName=input('User : ')
    password=input('Password : ')
    if userName=='admin' and password=='1234' :
        print('Done !')
        return ShowMenu()
    else:
        print('login Error')
        return Login()
def ShowMenu():
    print('---i Shop---')
    print('1. Vat celculator')
    print('2. Price celculator')
    print('3. Exit ')
    return SelectMenu()
def SelectMenu():
    userSelec=int(input('>> '))
    if userSelec==1:
        return VatCalculator()
    if userSelec==2:
        return PriceCalculator()
    elif userSelec==3:
        return Login()
    else:
        print('Please fill out the correct information.')
        return ShowMenu()
def VatCalculator():
    price=int(input('Price : '))
    print('---Total---')
    result=str(price+(price*(vat/100)))+' THB'
    return result 
def PriceCalculator():
    price1=int(input('Fist price : '))
    price2=int(input('second price : '))
    ('---Total---')
    Total=str((price1+price2)+((price1+price2)*(vat/100)))+' THB'
    return Total
print(Login())
while VatCalculator or PriceCalculator == True:
    print(ShowMenu())
