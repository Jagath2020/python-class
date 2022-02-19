#Find factorial of a number using recursive function

def factorial(n):
    #base case
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(7))
print(factorial(9))    
print(factorial(5))      
        
