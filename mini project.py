#Miniproject:  date:21.2.2022

#Game:rock paper scissor

#Number of games you want to play ? collect one integer
n= int(input(("enter the no of times you want to play:")))


#intilize the counts
tie= 0
user_count=0
system_count=0
#input lists
user_list=[]
system_list=[]

#conditions
for i in range(0,n):
    user = input(("give your choice (rock/paper/scissor):"))
    user_list.append(user)

    # collect system input ==> random
    import random
    system = ["rock","paper","scissor"]
    x=random.choice(system)
    system_list.append(x)

    if (user_list[i]==system_list[i]):
        tie+=1

    elif (
        
        user_list[i]=="scissor" and system_list[i]=="paper" or
        user_list[i]=="paper" and system_list[i]=="rock" or
        user_list[i]=="rock" and system_list[i]=="scissor"):
        
        user_count+=1
                             
    else:
        system_count+=1
     

#Who wins
print("User list is:",user_list)
print("system list is:",system_list)

print("Total no of games:",n)
print("System points:",system_count)
print("User points:",user_count)
print("Tie:",tie)

if (user_count>system_count):
    print("USER wins the game !!! Congrats !!!!")
elif (system_count>user_count):
    print("System wins the game!!")
else:
    print("TIE")



