import math

#declare varibles
shape = 0 #default is 0
area = 0
side = 0
length = 0
width = 0
heigth = 0
base = 0
radius = 0
pi = math.pi



print("""==================
Area Calculator 📐
==================
""")

print("""1) Triangle
2) Rectangle
3) Square
4) Circle
5) Quit
""")

shape = int(input("Which shape: "))

if(shape == 1):
    heigth = int(input("Heigth: "))
    base = int(input("Base: "))

    #calc area
    area = (heigth*base)/2

    print(f"The area is {area}")
elif(shape == 2):
    length = int(input("Length: "))
    width = int(input("Width: "))

    #calc area
    area = length * width

    print(f"The area is {area}")
elif(shape == 3):
    side = int(input("Side: "))

    #calc area
    area = side**2

    print(f"The area is {area}")
elif(shape == 4):
    radius = int(input("radius: "))

    #calc area
    area = pi*(radius**2)

    print(f"The area is {area}")
elif(shape == 5):
    quit