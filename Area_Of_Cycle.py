#Calculate Area of Circle and its Circumference
radius=int(input("Enter radius in cm: "))
pi=3.14
Area_of_Circle=int(pi*radius*radius)
Circumference_Of_Circle=2*pi*radius
print("The area of circle is {1} sq.cm and circumference is {2} cm for the radius {0} cm".format(radius,Area_of_Circle,Circumference_Of_Circle))
