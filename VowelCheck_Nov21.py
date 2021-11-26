##User input
Input_name=input("Enter the string: ")
if len(Input_name)%2 == 0:
    MidLength_of_name=(len(Input_name)//2)-1
else:
    MidLength_of_name=len(Input_name)//2     
MidLetter=Input_name[MidLength_of_name]
if MidLetter.lower() in "aeiou":
    print("Midletter {} is a vowel".format(MidLetter))
else:
    print("Midletter {} is a not vowel".format(MidLetter))

