#get one string from user
#check whether length of the string is odd or even
Input_name=input("Enter the string: ")
if len(Input_name)%2 == 0:
    print("String length is {} and it\'s even".format(len(Input_name)))
else:
    print("String length is {} and it\'s odd".format(len(Input_name)))    
