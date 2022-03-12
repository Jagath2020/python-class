#project1 with module

#importing sys module
import sys
    
#print Welcome to Data structure calculator
print("Welcome to Data structure calculator")

#Exception handling for ValueError
try:
    #Please select any one Data structure by user input

    user =  int (input('''
Please select anyone option:
1.list
2:Tuple
3:Set
4:Dictionary
your option is:'''))
    #Condition For negative integer input
    if user>=0 and user<=4:
        print("valid input")
    elif user>=5:
        #printing reason for Error
        print("please select data structure number from 1 to 4")
        sys.exit()
except ValueError:
    #printing reason for Error
    print("please give your input in integer number and range from 1 to 4")
    sys.exit()
  
# LIST OPERATIONS

#Importing list by user defined modules using * method
from listopr import *

#Conditions for user input
# User selected 1 means it will print all list methods
if user==1:
    print("User selected LIST")
    #Calling created list and assigned to new_list
    new_list=create_list()
    
    #While loop for list operations
    while True:
        print("\n")
        #printing All list methods
        print("Welcome to the List operations")
        print('''
LIST OPERATIONS ARE:
1.append
2.pop
3.reverse
4.sum/min
5.extend
6.max
7.del
8.len
9.remove
10.sort
11.mean
12.median
13.frequeuncy
14.find
15.insert
16.exit''')

        #Exception handling for valueError(incase user enter char for int number it will handle)
    
        try:
            #Getting list choice from user
            list_input =int(input("Enter your choice of operation:"))
            
        except ValueError:
            #printing reason for Error
            print("please enter the number from 1 to 15 and not a characters")
            sys.exit()

        #conditions for list methods depends upon user choice

        #List1:Append method
        if list_input == 1:
            #Exception handling For ValueError
            try:
                #printing a list before append
                print("List:",new_list)
                #Getting the element to append from user
                app = int(input("please enter the element you want to append:"))
                #Calling append method by function
                new_list=list_append(new_list,app)
                #printing the append method output
                print("List is after append the element:",new_list)
            except ValueError:
                #printing reason for Error
                print("enter only integer number to append")
                sys.exit()

        #List2:Pop method
        elif list_input == 2:
            #Exception handling For ValueError and indexError
            try:
                #printing a list before pop
                print("List:",new_list)
                #Getting the element to pop from user
                pop1 = int(input("please enter the position:"))
                #Calling pop method by function call
                new_list=list_pop(new_list,pop1)
                #printing the append method output
                print("List is after pop the element:",new_list)
            except IndexError:
                #printing reason for indexError
                print("please give index number in list range to pop")
                sys.exit()
            except ValueError:
                #printing reason for ValueError
                print("enter only integer number with in list index to pop")
                sys.exit()

        #LIst3:Reverse a list
        elif list_input == 3:
            #printing a list before reverse
            print("List:",new_list)
            #printing a list after reverse
            print("The list in in reverse:",list_reverse(new_list))

        #List4: Sum and min of list
        elif list_input == 4:
            #printing a list
            print("List:",new_list)
            #printing a sum and min of list
            print("Sum of the list is:",sum(new_list))
            print("Minimum of the list is:",min(new_list))

        #List5:extending newlist from old list
        elif list_input == 5:
            #printing a List
            print("List:",new_list)
            #printing a list after extend
            print("list1 is extended with list2 is:",list_extend(new_list))
            
        #List6:Maximum of list
        elif list_input == 6:
            # printing a List
            print("List:",new_list)
            #printing max of list
            print("Maxium of the list is:",max(new_list))
            
        #List7:Del function
        elif list_input == 7:
            #Exception handling for valueError and indexError
            try:
                #printing a List
                print("List:",new_list)
                #Getting the delete position from user
                del1 = int(input("please enter the pos you want to delete:"))
                #Callinf del method by function call
                new_list=list_del(new_list,del1)
                #printing a List after delete
                print("Deleted list is:",new_list)
            except IndexError:
                #printing reason for indexError
                print("please give index number in list range to delete")
                sys.exit()
            except ValueError:
                #printing reason for Error
                 print("enter only integer with in list index to delete ")
                 sys.exit()

        #List8: Length of the list
        elif list_input == 8:
            #printing a list
            print("List:",new_list)
            #printing a Length of the list
            print("Length of the list is:",len(new_list))

       #list9:Remove element from List 
        elif list_input == 9:
            #Exception handling for valueError
            try:
                #printing a List
                print("List:",new_list)
                #Geting the element to remove from user
                rem1 = int(input("please enter the element to remove:"))
                new_list=list_remove(new_list,rem1)
                #printing the list after the removing element
                print("The list  after removed element is:",new_list)
            except ValueError:
                #printing reason for valueError
                print("please enter the int number to remove that is available in list")
                sys.exit()
                
        #List10:Ascending order
        elif list_input == 10:
            #Printing orginal List
            print("Original list is:",new_list)
            #printing ascending order of list
            print("The list in ascending order:",list_sort(new_list))
            
      #List11:Mean of the list
        elif list_input == 11:
            #printing list
            print("List:",new_list)
            #Printing a mean of list
            print("The mean of the list1 is:",list_mean(new_list))
            
        #List12:median of list
        elif list_input == 12:
            #printing list
            print("List:",new_list)
            #printing median of List
            print("The median of the list odd/even list is:",list_median(new_list))

         #List13: Frequency of list  
        elif list_input == 13:
            #exception handling for Valueerror
            try:
                #Printing a List
                print("List:",new_list)
                #Getting a number to find frequency
                fre = int(input("please enter the frequency of element:"))
                #printing Frequency of given number
                print("Frequency of the given element is:",list_frequency(new_list,fre))
            except ValueError:
                #printing reason for error
                print("please enter int number to find frequency that is available in list")
                sys.exit()
                
        #List14:Find position of given element
        elif list_input == 14:
            #exception handling
            try:
                #printing a List
                print("List:",new_list)
                #Getting number to find position
                find1 = int(input("please enter the element to find:"))
                #printing the pos of given element
                print("The element find in position:",list_find(new_list,find1))
            except ValueError:
                #printing the reason for error
                print("please enter the element to find pos that is available in list")
                sys.exit()

        #List15:Insert a new element
        elif list_input == 15:
             #exception handling
            try:
                #printing a List
                print("List:",new_list)
                #Getting number to insert pos and value
                pos1 = int(input("enter the position to insert :"))
                val= int(input("enter the value to insert :"))
                #calling insert method by function call
                new_list=list_insert(new_list,pos1,val)
                #printing a List after insert the element
                print("The new element inserted after list is:",new_list)
            
            except ValueError:
                #printing reason for error
                 print("enter only integer with in list index to insert ")
                 sys.exit()
                 
        #condition to exit from loop
        elif list_input == 16:
            break
        #Condition for list negative input and greater than 16
        elif list_input<=0 or list_input>=17:
            print("please enter the number for List options from 1 to 15")

        
#TUPLE OPERATIONS
#importing user defined Tuple
from tupleopr import *
#Condition for selecting Tuple        
if user==2:
    print("User selected TUPLE")
    #Calling Created tuple by function
    new_tuple=create_tuple()
    #while loop for Tuple methods
    while True:
        print("\n")
        #Printing all tuple operations
        print("Welcome to the Tuple operations")
        print('''
TUPLE OPERATIONS ARE:
1.sum/min/len
2.reverse
3.find
4.count
5.join
6.exit''')
        #Exception handling for valueError
        try:
            #Getting choice of operations from user by input method
            tuple_input =int(input("Enter your choice of operation:"))
        except ValueError:
            #printing reason for error
            print("please enter the integer number from 1 to 5 ensure not a characters ")
            sys.exit()
            
        #Tuple1:Sum,min and max of Tuple
        if tuple_input == 1:
            #Printing a tuple
            print("Tuple:",new_tuple)
            #printing sum ,min and max of tuple
            print("Sum of the tuple is:",sum(new_tuple))
            print("minimum of the tuple is:",min(new_tuple))
            print("The length of the tuple is:",len(new_tuple))

        #Tuple2:Reverse a Tuple
        elif tuple_input == 2:
            #Printing a tuple
            print("Tuple:",new_tuple)
            #Printing a reversed tuple
            print("The tuple in in reverse:",tuple_reverse(new_tuple))

        #Tuple3:Find postion of Tuple 
        elif tuple_input == 3:
            try:
                #Printing a tuple
                print("Tuple:",new_tuple)
                #Getting the element to find position
                find1 = int(input("please enter the element to find:"))
                #Printing a position of tuple
                print("The element find in tuple at position:",tuple_find(new_tuple,find1))
            except ValueError:
                #Printing a reason for error
                print("please enter the integer number that is available in list to find")
                sys.exit() 

        #Tuple4:Count of given element
        elif tuple_input == 4:
            #Exception handling for valueError
            try:
                #Printing a tuple
                print("Tuple:",new_tuple)
                #Getting the element to count
                count_f=int(input("please enter the element to count"))
                #Printing a count of given number in tuple
                print("Count of the given element is:",tuple_count(new_tuple,count_f))
            except ValueError:
                #Printing a reason for error

                print("please enter the integer number that is available in list to count")
                sys.exit()
                
        #Tuple5:concodenate or join
        elif tuple_input == 5:
            #Printing a tuple
            print("Tuple:",new_tuple)
            #Printing a  joined tuple
            print("Joined  tuples are:",tuple_join(new_tuple))

        #Tuple6:exit from loop   
        elif tuple_input==6:
            break
        #Condition for negetive and out of range tuple input
        elif tuple_input<=0 or tuple_input>=7:
            print("please enter the number between 1 to 5 for tuple operations:")



#SET OPERATIONS :
#import user defined Set module
import setopr as se

#Condition for selecting Tuple        
if user==3:
    print("User selected SET")
    #Calling Created Set by function
    new_set=se.create_set()
    #While loop for set operations
    while True:
        print("\n")
        #Printing all Set operations
        print("Welcome to the Set operations")
        print('''
SET OPERATIONS ARE:
1.add
2.len
3.clear
4.copy
5.remove/discard
6.pop
7.update
8.union
9.intersection
10.difference
11.symmetric_diffrence
12.subset
13.superset
14.isdisjiont
15.diffrence_update
16.exit''')

        #Exception handling for valueError
        try:
            #Getting user choice set methods by user input
            set1_input =int(input("Enter your choice of operation:"))
        except ValueError:
            #printing reason for error
             print("please give valid input in integer number 1 to 15 not a characters")
             sys.exit()
             
        #Set1:Add element to the set    
        if set1_input == 1:
            #Exception handling for valueError
            try:
                #printing a Set
                print("Set:",new_set)
                #Getting the element to add from user
                add1 = int(input("enter the element to add:"))
                #Calling add function
                new_set=se.set_add(new_set,add1)
                #printing a Set after adding element
                print("Set after the add the element is:",new_set)
            except ValueError:
                #printing reason for error
                print("please enter the integer number to add")
                sys.exit()
                
        #Set2: Length of the Set
        elif set1_input == 2:
            #printing a Set
            print("Set:",new_set)
            #printing a length
            print("The length of the set is:",len(new_set))

        #Set3:Clear the set
        elif set1_input == 3:
            #printing a Set before clear
            print("Set before clear:",new_set)
            clear1=new_set.clear()
            #printing a Set after clear
            print("Set  after cleared the element is :",new_set)
        
        #Set4:copy of set
        elif set1_input == 4:
            #printing a Set before copy
            print("Set:",new_set)
            #Calling set copy function
            copy1=new_set.copy()
            #printing a Set after copy
            print("The copy of new set is:",copy1)

        #Set5:Remove element from set
        elif set1_input == 5:
            #Exception handling for valueError
            try:
                #printing a Set
                print("Set before remove:",new_set)
                remove1 = int(input("please enter the element:"))
                #Calling set remove function
                new_set=se.set_remove(new_set,remove1)
                #printing a Set after removed the element
                print("Set is after removed the element is :",new_set)
            except ValueError:
                #printing a reason for error
                print("please enter the int number to remove that is available in Set")
                sys.exit()

        #Set6:Pop the element from Set
        elif set1_input == 6:
            #printing a Set before pop
            print("Set before pop:",new_set)
            #Calling set pop function
            new_set = se.set_pop(new_set)
            #printing a Set after pop
            print("Set sfter pop:",new_set)

        #Set7:Update a Set
        elif set1_input==7:
            #printing a Set before update
            print("Set before update:",new_set)
            #printing a Set after Update
            print("set1 is updated with set2 is:",se.set_update(new_set))

        #Set8:Union of two sets
        elif set1_input==8:
            #printing a old set
            print("Set:",new_set)
            ##printing a Set after union
            print("union of these two sets are:",se.set_union(new_set))

        #Set9:Intersection of two sets
        elif set1_input==9:
            #printing a Set before intersection
            print("Set:",new_set)
            #printing a Set after intersection
            print("intersection of  two sets are :",se.set_intersection(new_set))

        #Set10:Difference of two sets
        elif set1_input==10:
            #printing a Set
            print("Set:",new_set)
            #printing a Set after difference
            print("diffrence between these two sets are:",se.set_difference(new_set))

        #Set11:Symmetric difference of two Sets
        elif set1_input==11:
            #printing a Set
            print("Set:",new_set)
            #printing a Set after symmetric diff
            print("symmetric diffrence of these two sets are:",se.set_symmetric_difference(new_set))

        #Set12:Subset checking
        elif set1_input==12:
            #printing a Set
            print("Set:",new_set)
            #printing a Set is subset or not
            print("set1 is subset of set2 ? ",se.set_subset(new_set))
            
        #Set13:Superset checking
        elif set1_input==13:
            #printing a Set
            print("Set:",new_set)
            #printing a Set is superset or not
            print("set1 is superset of set2? ",se.set_superset(new_set))
            
       #Set14:Disjoint
        elif set1_input==14:
            #printing a Set
            print("Set:",new_set)
            #printing a Set is disjoint or not
            print("disjoints is present ? ",se.set_is_disjoint(new_set))

        #Set15:Difference Update
        elif set1_input==15:
            #printing a Set
            print("Set:",new_set)
            #printing a Set after diffrence updated
            print("diffrence update between two sets are:",se.set_difference_update(new_set))
            
        #Set16:exit from loop
        elif set1_input==16:
            break
        
        #Condition for negative and outofrange set operations
        elif set_input<=0 or set_input>=17:
            print("please enter the number from 1 to 15 for set operations")
            
    
#DICTIONARY
           
import dictopr as d

if user==4:
    print("User selected DICTIONARY ")
    new_dict=d.create_dict()
    while True:
        print("\n")
        print("Welcome to the DICTIONARY operations")
        print('''
DICTIONARY OPERATIONS ARE:
1.get_keys
2.update_key
3.clear
4.copy
5.all_values
6.pop/pop_items
7.sum/len
8.min_key/max_key
9.del
10.add_new_item
11.all_items
12.exit''')

        try:
            dict_input =int(input("Enter your choice of operation:"))
        except ValueError:
             print("please enter valid input in integer number 1 to 11 not a characters")
             sys.exit()

        if dict_input==1:
            try:
                print("Dictionary:",new_dict)
                key1= int(input("please enter the key to get value:"))
                print("The value of the given key is:",d.dict_get_key(new_dict,key1))
            except ValueError:
                print("please enter valid key name ensure not a characters")
                sys.exit()
            except KeyError:
                 print("please enter the key value that is available in dictionary")
                 sys.exit()


        elif dict_input==2:
            try:
                print("Dictionary before update is:",new_dict)
                key= int(input("please enter the key to be update:"))
                val=input("please enter the new value to change:")
                print("dictionary after update is:",d.dict_val_update(new_dict,key,val))
            except ValueError:
                print("please enter valid key name ensure not a characters")
                sys.exit()
    
        elif dict_input==3:
            print("Dictionary before Clear:",new_dict)
            clear_dict = new_dict.clear()
            print(" Dictionary after Clear:",d.dict_clear(new_dict))
        
        elif dict_input==4:
            print("Orginal Dictionary is:",new_dict)
            print("The Copied Dictionary is:",d.dict_copy(new_dict))

        elif dict_input==5:
            print("Dictionary :",new_dict)
            print("All the values in the dictionary are:",d.dict_val(new_dict))
   

        elif dict_input==6:
            try:
                print("Dictionary before pop:",new_dict)
                pop1= int(input("please enter the key to pop:"))
                print("Popped val in the dictionary:",d.dict_pop(new_dict,pop1))
                print("popped items in the dictionary",new_dict.popitem())
            except ValueError:
                print("please enter valid key in integer number ensure not a characters")
                sys.exit()
            except KeyError:
                print("please enter valid key name available in Dictionary")
                sys.exit()
           
        elif dict_input==7:
            print("Dictionary :",new_dict)
            d.dict_sum_len(new_dict)

        elif dict_input==8:
            print("Dictionary :",new_dict)
            print("Miniumu of keys is:",d.dict_min(new_dict))
            print("Maximum of key is:",d.dict_max(new_dict))

        elif dict_input==9:
            try:
                print("Dictionary before delete:",new_dict)
                del1= int(input("please enter the key to del:"))
                print("dictionary after deleted the item is:",d.dict_del(new_dict,del1))
            except ValueError:
                print("please enter valid key in integer number ensure not a characters")
                sys.exit()
            except KeyError:
                print("please enter valid key name available in Dictionary")
                sys.exit()

        elif dict_input==10:
            try:
                print("Dictionary:",new_dict)
                key_item=int(input("please enter the new key:"))
                val_item = input("please enter the new val:")
                print("dictionary after added new item is:",d.dict_update_item(new_dict,key_item,val_item))
            except ValueError:
                print("please enter valid key in integer number ensure not a characters")
                sys.exit()

        elif dict_input==11:
            print("Dictionary:",new_dict)
            print("All the items in the dictionary are:",d.dict_items(new_dict))

        elif dict_input==12:
            break
        
        elif dict_input<=0 or dict_input>=12:
            print("please enter the number from 1 to 11 for Dictionary operations")
    
        


    
