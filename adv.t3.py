#write a program for prime no using function

def prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return "not a prime number"
        else:
            return "prime no"
    
print(prime(7))
print(prime(14))
print(prime(14))
print(prime(19))
print(prime(23))
