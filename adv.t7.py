#find fibonacci series

def fibonacci(n):
    a = 0#first no 
    b = 1#second no
     
    # Check is n is less than 0
    
    if n < 0:
        print("Invalid")
         
    # Check is n is equal to 0
    
    elif n == 0:
        return 0
       
    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b#c is third no
            print(c,end = " ")
            a = b
            b = c
        return b
 
print(fibonacci(8))
print(fibonacci(10))
 
