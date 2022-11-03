systemMENU={'rice':10,'egg':5,'Apple':25,'Banana':15}
menuLIST = [] 
def shoeBill():
    sum=0 
    print('---My Food---')
    for number in range(len(menuLIST)):  
        print(menuLIST[number][0],menuLIST[number][1]) 
        sum+=int(menuLIST[number][1])
    print('Total : ',sum,' THB')

while True:
    menuNAME=input('Enter your memu : ')
    if (menuNAME.lower() == 'exit'): 
        break 
    else:
        menuLIST.append([menuNAME,systemMENU[menuNAME]]) 
print(menuLIST)
shoeBill()
