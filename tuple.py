#TUPLE

#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
#Find the common elements between two tuples
#Concatenate both tuples and remove duplicates from tuple
#Find the index value of 9 (after concatenation)
#multiply above elements 3 times

#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
tup1 = (1,4,5,6,7,8)
tup2 = (5,6,7,8,9)

#Find the common elements between two tuples
#conveting tuple in to set
a = set(tup1)
b = set(tup2)
#find common elements
c = a.intersection(b)
print("The common elements between two tuples :",c)

#Concatenate both tuples 
new_tup= tup1 + tup2
print(new_tup)

#reomoves duplicates from tuple
dup = set(new_tup)
org = tuple(dup)
print("the orginal set after removed duplicate is:",org)

#Find the index value of 9 (after concatenation)
find9 = new_tup[9]
print("the index value of 9 is:",find9)

#multiply above elements 3 times
mul = org*3
print("the multipleied by 3 tuple is:",mul)

#OUTPUT
The common elements between two tuples : {8, 5, 6, 7}
(1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9)
the orginal set after removed duplicate is: (1, 4, 5, 6, 7, 8, 9)
the index value of 9 is: 8
the multipleied by 3 tuple is: (1, 4, 5, 6, 7, 8, 9, 1, 4, 5, 6, 7, 8, 9, 1, 4, 5, 6, 7, 8, 9)


#SET

#Create two empty sets
#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
#check whether set2 is subset of set1 or no ?
#check whether both have common elements are no ?
#remove 8 from set 1 and set 2 ==> find the inferences
#discard 0 from set1 and set2 
#find collection of both sets ===> set1 and set2

#Create two empty sets
set1 = set()
set2 = set()

#update set1 with 7,8,9,1,2,3,4,5,0
new_set1 = (7,8,9,1,2,3,4,5,0)
set1.update(new_set1)
print("the updated set1 is:",set1)

#update set2 with 4,5,6,0
new_set2 = (4,5,6,0)
set2.update(new_set2)
print("the updated set2 is:",set2)

#check whether set2 is subset of set1 or no
x = set2.issubset(set1)
print(x)

#check whether both have common elements are no ?
common = set1.intersection(set2)
print("the common elements between two sets are:",common)

#remove 8 from set 1 and set 2 ==> find the inferences
set1.remove(8)
print("the elements 8 removed set is:",set1)

#discard 0 from set1 and set2
set1.discard(0)
set2.discard(0)             
print("the zero remove by set1 is {} and set2 is {} ".format(set1,set2))

# OUTPUT


#find collection of both sets ===> set1 and set2

#DICTIONARY

#create a dictionary
#{1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
#Extract "bobtn" from above dictionary
#Extract "arbeg" from above dictionary
#print all keys in dictionary and convert it into tuple
#Find the average of all numbers available under key "2"

#create a dictionary
dict1 = {1:["english","maths","science"],
         2:[10,20,30],
         3:["bio-botany","bio-zoology","Algebra"]}
print(dict1)

#get the value of key3 using get() function
x = dict1.get(3)
print("The key3 values are:",x)
y = x[0]
#extract the values "bobtn"
var_bobtn = y[0]+y[2]+y[4]+y[6]+y[8]
print("the extract output1:",var_bobtn)

#Extract "arbeg" from above dictionary
z= x[2]

#extract the values "arbeg"
var_arbeg = z[0]+z[5]+z[4]+z[3]+z[2]
print("the extract output2 is:",var_arbeg)

#print all keys in dictionary and convert it into tuple
allkeys = dict1.keys()
print("The keys are in dictionaries are:",allkeys)
#convert in to tuple
tup1 = tuple(allkeys)
print("the keys in tuple format :",tup1)

#Find the average of all numbers available under key "2"
#extract key2 values
key2 = dict1.get(2)
print("the key2 values are:",key2)
sum1= sum(key2)
avreage = (sum1/len(key2))
print("the avreage of key2 value is:",avreage)

#OUTPUT

{1: ['english', 'maths', 'science'], 2: [10, 20, 30], 3: ['bio-botany', 'bio-zoology', 'Algebra']}
The key3 values are: ['bio-botany', 'bio-zoology', 'Algebra']
the extract output1: bobtn
the extract output2 is: Arbeg
The keys are in dictionaries are: dict_keys([1, 2, 3])
the keys in tuple format : (1, 2, 3)
the key2 values are: [10, 20, 30]
the avreage of key2 value is: 20.0
