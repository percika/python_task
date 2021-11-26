#Using Range function  print multiples of 5 from 0 to 75
#Using Range function  print multiples of 8 from 0 to 72
#Using Range function  print multiples of 5 from 75 to 0
#Using Range function  print multiples of 8 from 96 to 72
list1=[]
for i in range(0,76,5):
    list1.append(i)
print("multiples of 5 from 0 to 75",list1)
list2=[]
for i in range(0,72,8):
    list2.append(i)
print("multiples of 8 from 0 to 72",list2)
list3=[]
for i in range(75,-1,-5):
    list3.append(i)
print("multiples of 5 from 0 to 75",list3)
list4=[]
for i in range(96,71,-8):
    list4.append(i)
print("multiples of 8 from 0 to 72",list4)


