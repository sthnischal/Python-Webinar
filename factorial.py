"""
This is a Python program for gettting factorial Numbers
"""
NUM = 10
def factorial_function(number):
    '''
    This is a function for factorial
    '''
    fact = 1
    for i in range(1, number+1):
        fact = fact * i
    return fact

FCT = factorial_function(NUM)
print(FCT)
