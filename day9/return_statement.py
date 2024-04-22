"""
👉 Return keyword used to exit the function and return the value of the function
👉 Recursion : recursion ka matlab hai k jo b function ho wo khud ko hii bar bar
               recall karay apnay ander tu hm uss ko recursive kahengay.
               iss ka benefit ye hai k for example agr humray pass koi data hai
               or humein looping krni hai tu hm recursion ko use kr sktay hain.


in the below function we use the return, we are not printing
so if we directly use the function,  hello() it will not give us anything
so that is why we have to print this.


Advantages :
code may look clean.
complex task may get easily done.
sequence generation become easier.

Disadvantages :
may take alot of memory.
sometime logic become harder.

"""


def hello():
    return "hello world"


print(hello())


def add(a, b):
    summ = a + b
    return summ


print(add(10, 10))  # here again we use the print statement with recalling the function.


print("------------------Recursion Example-----------------------")

# tu ye recursion hai.. qk hm nay print or return b use kiyaa hai tu
# tu jab tk ye condition false nai ho jati. ye tb tk khud ko racall krtaa jaye ga.
# we can also do this by loop but this is just the example of recursion.


def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(8))


