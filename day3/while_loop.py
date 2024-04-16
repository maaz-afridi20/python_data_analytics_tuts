"""
the while loop will be executed until and unless some specific condition
is not completed and then the while loop will be stopped.
in the while loop we have to write the increment by our own.
so in the while loop
we have to increment the condition. otherwise it will go in infinite loop.

"""


n = 0
while n <= 5:
    print(n)
    n += 1


a = 1
number = int(input("enter number : "))
while a <= 10:
    print(number, "X", a, "=", number*a)
    a = a + 1
