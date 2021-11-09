#Convert middle character to upper case
Input_name=input("Enter Name for Conversion: ")
print(Input_name)
if len(Input_name)%2 == 0:
    MidLength_of_name=(len(Input_name)//2)-1
else:
    MidLength_of_name=len(Input_name)//2     
MidLetter=Input_name[MidLength_of_name]
MidConv=MidLetter.upper()
print(MidConv)
print(Input_name.replace(MidLetter,MidConv))
