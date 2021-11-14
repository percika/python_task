#Create two empty sets
#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
#check whether set2 is subset of set1 or no ?
#check whether both have common elements are no ?
#remove 8 from set 1 and set 2 ==> find the inferences
#discard 0 from set1 and set2 
#find collection of both sets ===> set1 and set2
set1=set()
set2=set()
set3={7,8,9,1,2,3,4,5,0}
set1.update(set3)
set2.add(4)
set2.add(5)
set2.add(6)
set2.add(0)
print("The first set is ",set1)
print("The second set is ",set2)
result=set2.issubset(set1)
print("Is set2 a subset of set1 ?- ",result)
print("Is set1 {} different from set2 {} ?- {}".format(set1,set2,set1.isdisjoint(set2)))
print("common elements between set1 {} and set2 {} are {}".format(set1,set2,set1.intersection(set2)))
set1.discard(8)
set2.discard(8)
print("Removed 8 from set1 {} and set2 {}".format(set1,set2))
set1.remove(0)
set2.remove(0)
print("Removed 0 from set1 {} and set2 {}".format(set1,set2))
x=set1.union(set2)
print("Collection of both sets are ", x)
#y=set1.symmetric_difference(set2)
#print(y)

