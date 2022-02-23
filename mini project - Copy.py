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
    system_choice=random.choice(system)
    print("system choice is:",system_choice)
    system_list.append(system_choice)

    if (user_list[i]==system_list[i]):
        print("Game TIE")
        tie+=1

    elif (
        
        user_list[i]=="scissor" and system_list[i]=="paper" or
        user_list[i]=="paper" and system_list[i]=="rock" or
        user_list[i]=="rock" and system_list[i]=="scissor"):
        print("Congrats User wins the game!!!!")
        user_count+=1
                             
    else:
        print("System wins the game")
        
        system_count+=1
     

#Who wins
print("User selected options list :",user_list)
print("system selected options list :",system_list)
print("Total no of games :",n)
print("System Score :",system_count)
print("User Score :",user_count)
print("Tie :",tie)



