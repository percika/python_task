#collect one number from user, check whether the number is positive or negative
#collect one number from user, check whether the number is even or odd
#collect one string from user, check whether the string is palindrome or not
Number1=int(input("Enter number for check positive or negative:"))
if Number1<0:
    print("Number {} is negative".format(Number1))
else:
    print("Number {} is positive".format(Number1))

Number2=int(input("Enter number for checking even or odd:"))
if Number2%2==0:
    print("Number {} is even".format(Number2))
else:
    print("Number {} is odd".format(Number2))

    
String1=input("Enter string for checking palindrome:")
String2=String1[::-1]
if String1==String2:
    print("String {} is palindrome".format(String1))
else:
    print("String {} is not a palindrome".format(String1))
