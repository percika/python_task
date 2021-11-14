#create a dictionary
#{1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
#Extract "bobtn" from above dictionary
#Extract "arbeg" from above dictionary
#print all keys in dictionary and convert it into tuple
#Find the average of all numbers available under key "2"
dict1={}
dict1.update({1:["english","maths","science"], 2:[10,20,30]})
dict1.update({3:["bio-botany","bio-zoology","Algebra"]})
print(dict1)
list1=dict1[3]
#print(list1)
#print(type(list1))
str1="".join(list1)
print(str1)
print("Extract \"bobtn\" and \"arbeg\" from above dictionary")
print(str1[:10:2])
print(str1[:-6:-1])
#print all keys in dictionary and convert it into tuple
print("All keys in dictionary are",dict1.keys())
print(dict1.values())
print(dict1.items())
tuple1=tuple(dict1.keys())
print("Converted it into tuple",tuple1)

#Find the average of all numbers available under key "2"
list2=dict1[2]
a=sum(list2)/len(list2)
print("The average of all numbers available under key \"2\" is ",a)
