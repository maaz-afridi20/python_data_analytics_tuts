# Q1 write a fibonacci series up to 10 numbers

# a = 0
# b = 1
#
# print(a)
# print(b)

# enterRange = int(input("Enter up to how much range you want fibonacci series : "))
#
# if enterRange == 1:
#     print(1)
# else:
#     for i in range(2, enterRange):
#         c = a + b
#         a = b
#         b = c
#         print(c)


# Q2 check whether number is prime or not.(divisible by itself)


# Number = int(input("Enter Range : "))
#
# if Number <= 1:
#     print('not prime')
# else:
#     for i in range(2, Number):
#         if Number % i == 0:
#             print("Not Prime")
#             break
#         else:
#             print("Prime")
#             break
#
#


# Q3  write a palindrome number

# palindrome number mean that number if we read that number from either side it should look like same
# like  131, 131


# numm = int(input("enter a number : "))
# temp = numm
# rev = 0
#
# while numm > 0:
#     dig = numm % 10
#     rev = rev * 10 + dig
#     numm = numm // 10
#
# if rev == temp:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# Q4 : Area Calculator.


print("********** Area Calculator *************")

while True:
    print("""
    Press 1 for finding area of square 
    Press 2 for finding area of rectangle
    press 3 for finding area of circle
    press 4 for finding area of triangle 
    """)
    choice = int(input("Enter number between 1-4 "))
    if choice == 1:
        while True:
            side = float(input("Enter sides of square : "))
            area = side ** 2
            print("area of square is ", area)
            repeatSquare = input("do you want to find area of square again ? ")
            if repeatSquare == 'no' or 'No':
                break

    elif choice == 2:
        while True:
            length = float(input("Enter length of rectangle "))
            width = float(input("Enter width of rectangle "))
            rectangle = length * width
            print("area of rectangle is ", rectangle)
            repeatRectangle = input("do you want to find area of rectangle again ?")
            if repeatRectangle == "no" or "No":
                break

    elif choice == 3:
        while True:
            radius = int(input("Enter radius of circle "))
            circleArea = (22/7) * (radius ** 2)
            print("area of circle is ", circleArea)
            repeatCircle = input("do you want to find area of circle again ? ")
            if repeatCircle == "no" or "No":
                break

    elif choice == 4:
        while True:
            base = float(input("Enter base of triangle : "))
            height = float(input("Enter height of triangle : "))
            triangleArea = 0.5 * base * height
            print("area of triangle is ", triangleArea)
            repeatTriangle = input("do you want to find the area of triangle again ? ")
            if repeatTriangle == "no" or repeatTriangle == "No":
                break

    repeatProcess = input("Repeat whole menu again ?")
    if repeatProcess == 'No' or repeatProcess == 'no':
        break
