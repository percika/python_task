#Calculate Area of Cylinder
radius=int(input("Radius in cm: "))
height=float(input("Height in cm: "))
pi=3.14
area_of_cylinder=int(pi*float((radius**2))*height)
print("The area of Cylinder is {} for radius {} cm and height {} cm".format(area_of_cylinder,radius,height))
