def cir():
    r = int(input("enter the radius: "))
    area = 3.14 * r * r
    return area

def tria():
    b = int(input("enter the base: "))
    h = int(input("enter the height: "))
    area = 0.5 * b * h
    return area

def square():
    a = int(input("enter the side: "))
    area = a * a
    return area

def rect():
    l = int(input("enter the length: "))
    w = int(input("enter the width: "))
    area = l * w
    return area

print("circle area:", cir())
print("triangle area:", tria())
print("square area:", square())
print("rectangle area:", rect())
