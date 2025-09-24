def factorial(x):
    '''This program finds the factorial of some numbers'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print("The factorial of 1 is:",factorial(1))
print("The factoral of 4 is:",factorial(4))
print("The factorial of 7 is:",factorial(7))    

    