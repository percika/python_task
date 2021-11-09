#Concatenating Name & its length
First_Name=input("Enter First Name: ")
Second_Name=input("Enter Second Name: ")
print(First_Name)
print(Second_Name)
Length_of_First_Name=str(len(First_Name))
Length_of_Second_Name=str(len(Second_Name))
Output=First_Name+Length_of_Second_Name+Second_Name+Length_of_First_Name
print(Output)
