age = 16
height = 5.10
complex = 2 + 3j

base = print("Enter the base: ")
height = print("Enter the height: ")
area_of_triangle = 0.5 * base * height
print("The area of the triangle is: ", area_of_triangle)

side_a = print("Enter the length of side a: ")
side_b = print("Enter the length of side b: ")
side_c = print("Enter the length of side c: ")
perimeter_of_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is: ", perimeter_of_triangle)

width = print("Enter the width: ")
length = print("Enter the length: ")
area_of_rectangle = width * length
print("The area of the rectangle is: ", area_of_rectangle)

radius = print("Enter the radius: ")
area_of_circle = 3.14 * radius ** 2
m = 2
x_int = 1
y_int = 2(0)-2
slope=(10-2)/(6-2)
distance = ((6-2)**2 + (10-2)**2) ** 0.5
if m > slope:
    print("The slop of y=2x-2 is steeper.")
else:
    print("The slop of y=2x-2 is less steep.")

for x in range(-10, 11):
    y = x ** 2 + 6 * x + 9
    if y == 0:
        print("When x is", x, "y is 0.")
    else:
        print("No solution in range")

print(len("python") > len("dragon"))
print("on" in "python" and "on" in "dragon")
print("jargon" in "python" and "jargon" in "dragon")
print("on" not in "python" and "on" not in "dragon")

python_length=float(len("python"))

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

if 7 // 3 == 2.7:
    print("True")
else:
    print("False")

type('10') == type(10)
int('9.8') == 10

hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
pay = print("Your weekly earning is: " + str(hours * rate))

years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")

print("1 1 1 1 1\n`2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")