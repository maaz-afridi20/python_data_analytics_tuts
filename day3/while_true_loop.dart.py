"""
while true loop is an infinite loop.
it can only be stopped by the break statement.
"""

# n = 1
# while True:
#     print('hello')
#     n += 1
#
# # this is infinite loop.


while True:
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    print(num1 + num2)

    repeat = input("do you want to repeat : ")
    if repeat == 'no':
        break

# now in this we have mentioned the break statement
# so due to the break statement the infinite loop will stop
