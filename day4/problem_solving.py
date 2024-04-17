# Q1 =>  write a program to find the sum of all the even number up to 50
# mySum = 0
# for i in range(1, 51):
#     if i % 2 == 0:
#         mySum += i

# print("Sum is", mySum)

# Q2 =>
#  write a program up to 20 number and write their squared number in front of them

# square = 0
# for i in range(1, 21):
#     print(i, i**2)

# Q3 =>
#  write sum of first 10 odd number using while loop.

# oddSum = 0
# n = 0
# while n <= 20:
#     if n % 2 != 0:
#         oddSum += n
#     n += 1
#
# print(oddSum)

# Q4 =>

while True:
    name = input("Enter your name : ")
    total = 0
    while True:
        print("enter amount and quantity")
        amount = float(input("Enter amount : "))
        quantity = float(input("Enter quantity : "))
        total += amount * quantity
        repeat = input('Repeat ? ')
        if repeat == 'no' or repeat == 'No':
            break
    print('-'*40)
    print("Name : ", name)
    print("Total : ", total)
    print('-' * 40)
    print('********** Good Shopping **********')

    repeat1 = input("Do you want to move to next customer? yes/no")
    if repeat1 == 'no' or repeat1 == 'No':
        break





