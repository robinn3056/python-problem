# volume calculator for different shapes
print("Choose one option to find out volume:\n")

A = "A.Cone"
B = "B.Cuboid"
C = "C.Cylinder"
D = "D.Sphere"
E = "E.Cube"
print(A, B, C, D, E, sep= "\n")

# User select the shape
Enter_option = input("Enter your option")

# Condition for input selected by user to measure the volume

if Enter_option == "A":
    H = float(input("Enter height of cone"))
    R = float(input("Enter radius of cone"))
    Volume = (1/3)*((22/7)*R*R*H)
    print("Volume of cone is: ", Volume)

elif Enter_option == "B":
    L = float(input("Enter length of cuboid"))
    b = float(input("Enter breadth of cuboid"))
    W = float(input("Enter width of cuboid"))
    Volume = (L*b*W)
    print("volume of cuboid is: ", Volume)

elif Enter_option == "C":
    H = float(input("Enter height of cylinder"))
    R = float(input("Enter radius of cylinder"))
    Volume = ((22/7)*R*R*H)
    print("volume of cylinder is: ", Volume)

elif Enter_option == "D":
    R = float(input("Enter radius of sphere"))
    Volume = ((4/3)*(22/7)*(R*R*R))
    print("volume of sphere is: ", Volume)

elif Enter_option == "E":
    H = float(input("Enter length of side of cube"))
    Volume = (H*H*H)
    print("volume of cube is: ", Volume)

else:
    None