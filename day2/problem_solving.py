# check whether the number is positive or not
num = int(input('enter any number : '))
if num > 0:
    print('positive')
else:
    print('negative')

# write program to check whether number is even or odd.

nummy = int(input('Enter any number : '))

if nummy % 2 == 0:
    print('even')
else:
    print('odd')


# write a program of area calculator

print("Area calculator...")
print("choose any number between 1-4")
print("""
press 1 to find the area of square
press 2 to find the ares of rectangle
press 3 to find the area of circle
press 4 to find the area of triangle
""")

choice = int(input('Enter your choice '))

if choice == 1:
    side = float(input('enter sides '))
    area = side * side
    print('area of circle is ', area)
elif choice == 2:
    length = float(input('enter length '))
    width = float(input('enter width '))
    area = length * width
    print('area of rectangle is ', area)
elif choice == 3:
    radius = float(input('enter radius of circle '))
    area = ((22/7)*(radius**2))
    print("area of circle is ", area)
elif choice == 4:
    base = float(input('enter triangle base '))
    height = float(input('enter triangle height '))
    area = 0.5*base*height
    print('area of triangle is ', area)
else:
    print('Invalid Input ')


# check whether the given input is vowel or not
vowelCheck = input('enter any string ')
if vowelCheck == 'a' or vowelCheck == 'e' or vowelCheck == 'i' or vowelCheck == 'o' or vowelCheck == 'u':
    print('yes vowel')
else:
    print('not a vowel')


vovwels = ['a', 'e', 'i', 'o', 'u']
againVowelCheck = input('enter str ')
if againVowelCheck in vovwels:
    print('yesss great')
else:
    print('nooooo')
