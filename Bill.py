Pay=int(input("Please enter the amount to pay:"))
Tip=int(input("Please enter the amount to tip the waiter:"))
def tot_bill(Pay,Tip):
    total=Pay+Tip/2.5
    total=round(total)
    print("Please pay:",total)    
tot_bill(Pay,Tip)    