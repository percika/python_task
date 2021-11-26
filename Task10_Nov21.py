#two strings from user

#mathematics ===> 4 vowels
#science ==> 3 vowels

#both are equal count or not equal
User_input1=input("Enter first string for validation: ")
User_input2=input("Enter second string for validation: ")
list1_a=['a','e','i','o','u']
list1=list(User_input1)
x1=list1.count("a")
x2=list1.count("e")
x3=list1.count("i")
x4=list1.count("o")
x5=list1.count("u")
first_string_count=x1+x2+x3+x4+x5
list2=list(User_input2)
x1=list2.count("a")
x2=list2.count("e")
x3=list2.count("i")
x4=list2.count("o")
x5=list2.count("u")
second_string_count=x1+x2+x3+x4+x5
if first_string_count==second_string_count:
    print("Vowel Counts are equal for User inputs- \"{}\" and \"{}\"- {}".format(User_input1,User_input2,first_string_count))
else:
    print("Vowel Counts are not equal for User inputs- \"{}\" and \"{}\"- {},{}".format(User_input1,User_input2,first_string_count,second_string_count))
