
#whether the string is palindrome or not

def polindrome(string):
    if string ==string[::-1]:
        return "polindrome"
    else:
        return "not a polindrome"
print(polindrome("malayalam"))
print(polindrome("python"))
print(polindrome("madam"))
print(polindrome("level"))
print(polindrome("java"))

# whether the number is armstrong or not
def armstrong(num):
    
    for i in (num):
        sum1 = 0
        arm = int(i)**3
        sum1 = sum1+arm
        
    if sum1==int(num):
        print("armstrong")
    else:
        print("not a amstrong")

print(armstrong("153"))
    
