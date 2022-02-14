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
