#get one integer from user (3 digit int only)
#armstrong or no (without using loops)

#153 ===> 1^3 + 5^3 + 3^3
#370 ===> 3^3 + 7^3 + 0^3
#371 ====> 3^3 + 7^3 + 1^3

User_input=int(input("Enter 3 digit number: "))

if User_input >= 100 and User_input <=999:
    print("Valid 3 digit number!!!")
    usr_inpt=str(User_input)
    first_digit=usr_inpt[0]
    #print(usr_inpt[0])
    second_digit=usr_inpt[1]
    #print(usr_inpt[1])
    third_digit=usr_inpt[2]
    #print(usr_inpt[2])
    final_calc=int(first_digit)**3+int(second_digit)**3+int(third_digit)**3
    #print(final_calc)
    if final_calc==User_input:
        print("The 3 digit number {} is a Armstrong Number!".format(final_calc))
    else:
        print("The 3 digit number {} is a Not Armstrong Number!".format(User_input))
else:
    print("Invalid entry!. Enter 3 digit number only")
