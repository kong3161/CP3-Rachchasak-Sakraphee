menuLIST = [] 
PriceList = [] 
def showBill(): 
    print('---My FOOD---')
    sum = 0
    for number in range(len(menuLIST)):
        print(menuLIST[number],PriceList[number])
        sum += int(PriceList[number])
        Total = 'Total : '+str(sum)+' THB'
    return Total

while True:
    menuNAME=input('Enter your memu : ')
    if (menuNAME.lower() == 'exit'):
        break 
    else:
        menuPRICE=input('Price : ')
        menuLIST.append(menuNAME)
        PriceList.append(menuPRICE)

print(showBill())
