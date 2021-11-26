#Get one mark from student
#mark 0 to 100 otherwise invalid mark

#50 + PASS otherwise FAIL
#90 to 100 ===> A  ==> Even + Odd -
#80 to 89 ===> B
#70 to 79 ===> C
#60 to 69 ===> D
#50 to 59 ===> E
#0 to 49 ===> FAIL
#93 ===> A-
#99 ===> A-
#88 ====> B+

#78

#VALID MARK
#PASS MARK
#C+
Mark=int(input("Enter the mark received: "))
if Mark%2 == 0:
    sign="+"
else:
    sign='-'
if Mark >= 0 and Mark <= 100:
    print("Valid mark!")
    if Mark >=50:
        print("Pass mark")
        if Mark >= 90 and Mark <=100:
            print("Congrats you have got A{} grade".format(sign))
        elif Mark >= 80 and Mark <=89:
            print("Congrats you have got B{} grade".format(sign))
        elif Mark >= 70 and Mark <=79:
            print("Congrats you have got C{} grade".format(sign))
        elif Mark >= 60 and Mark <=69:
            print("Congrats you have got D{} grade".format(sign))
        elif Mark >= 50 and Mark <=59:
            print("Congrats you have got E{} grade".format(sign))
    else:
        print("Fail mark")
else:
    print("Invalid mark!")
    
