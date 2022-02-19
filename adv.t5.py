# factorial using function



def fact(n):
     factorial = 1;
     #if (n<=0):
      #   return "none"
              
     if(n<=1):
        return 1
        for i in range(2, n + 1):
            factorial= factorial * i;
            return factorial;
                      
print(fact(7))

