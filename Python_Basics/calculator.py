import math

print("==================")
print("Area Calculator 📐")
print("==================\n")

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

answer = int(input("Which shape: "))

area = 0

while True:
    if answer == 1:
        side = int(input("Side: "))
        area = math.pow(side, 2)
    elif answer == 2:
        length = int(input("Length: "))
        width = int(input("Width: "))
        area = length * width
    elif answer == 3:
        height = int(input("Height: "))
        base = int(input("Base: "))
        area = (height * base) / 2
    elif answer == 4:
        radius = int(input("Radius: "))
        area = math.pi * math.pow(radius, 2)
    elif answer == 5:
        break
    print(f"The area is {area}")
    answer = int(input("Which shape: "))

