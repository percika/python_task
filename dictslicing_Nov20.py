#extract 3
#Extract 1994
#extract backend
#split this "frontend/backend" with / and itentify index 0
#extract core
dict1={"python":[1994,"interpreter","scripting","development",3], "java":[1992,"compiler","scripts","frontend/backend",10],"c":[1980,"core","scripting","Both",20]}
list1=dict1["python"]
print(list1[4])
print(list1[0])
list2=dict1["java"]
print(list2[3][9:])
list3=list2[3].split("/")
print(list3.index(list3[0]))
list4=dict1["c"]
print(list4[1])
