#Create an empty list
#Concatenate with [5,6,7,8,10]
#add 8,3,4,4,10,9,1,5,6,7,8,1 elements to that list
#Find frequency of 8 (count) and index of 10
#find the mean of the list
#find sum (List) + min + Max 
#Find median of the list
#remove duplicates from list and give output in the format of tuple
#convert to tuple and set
List1=[]
List2=[5,6,7,8,10]
List1=[]+List2
print(List1)
List1.append(8)
List1.append(3)
List1.append(4)
List1.append(4)
List1.append(10)
List1.append(9)
List1.append(1)
List1.append(5)
List1.append(6)
List1.append(7)
List1.append(8)
List1.append(1)
x=List1.count(4)
y=List1.index(10)
print(List1)
print("The frequency of 4 is {} and index of 10 is {}".format(x,y))
z=sum(List1)
mean_list1=z/len(List1)
min_list1=min(List1)
max_list1=max(List1)
print("The sum of {} is {} and its mean {}".format(List1,z,mean_list1))
print("Min value is {2} and Max value is {1} of list{0}".format(List1,max_list1,min_list1))
set1=set(List1)
print("The set format is",set1)
tuple1=tuple(set1)
print("The Tuple format is",tuple1)

