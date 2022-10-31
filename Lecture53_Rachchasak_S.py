def vatCalculus(totalprice):
    result=totalprice+(totalprice*7/100)
    return result
userinput=int(input('Please Enter Price : '))
print(vatCalculus(userinput))
