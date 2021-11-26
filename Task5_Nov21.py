#Get one string from user
#Find the middle letter
#find ascii value for the middle letter
#check whether ascii value is odd or even
Input_name=input("Enter the string: ")
if len(Input_name)%2 == 0:
    MidLength_of_name=(len(Input_name)//2)-1
else:
    MidLength_of_name=len(Input_name)//2     
MidLetter=Input_name[MidLength_of_name]
ascii_val=ord(MidLetter)
print("Ascii value of Midletter {1} is {0}".format(ascii_val,MidLetter))


