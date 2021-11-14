#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
#Find the common elements between two tuples
#Concatenate both tuples and remove duplicates from tuple
#Find the index value of 9 (after concatenation)
#multiply above elements 3 times
tuple1=(1,4,5,6,7,8)
tuple2=(5,6,7,8,9)
print("The two tuples are {} and {}".format(tuple1,tuple2))
set1=set(tuple1)
#print(set1)
set2=set(tuple2)
#print(set2)
set3=set1.intersection(set2)
set4=set1.union(set2)
print("The common elements in both tuples are ",tuple(set3))
print("The union of both tuples are ",tuple(set4))
tuple3=tuple(set4)
x=tuple3.index(9)
y=tuple3*3
print("The index value of 9 is", x)
print("The three times of above tuple is ",y)
