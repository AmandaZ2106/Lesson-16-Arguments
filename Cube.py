def cube(number):
    return number*number*number
def div_3(number):
    if number%3==0:
        return cube(number) 
    else:
        print("False!") 
        
print(div_3(3))  
print(div_3(5))

