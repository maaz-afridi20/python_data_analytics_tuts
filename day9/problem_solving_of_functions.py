# write function to find maximum 3 number
def max_number(val1, val2, val3):
    if val1 > val2 and val1 > val3:
        print(val1, " is the greatest")
    elif val2 > val1 and val2 > val3:
        print(val2, " is the greatest")
    else:
        print(val3, " is the greatest")


max_number(19, 50, 28)


# write a python function to create and print a list where
# values are square of number between 1 and 30


# def create_list():
#     squared_list = []
#     for i in range(31):
#         squared_list.append(i**2)
#     return squared_list
#
#
# print(create_list())


# write a function that take number as parameter and check whether if its prime or not.

def check_prime(num):
    if num == 0 and num == 1:
        print("0 and 1 are not prime")
    if num == 2:
        print("2 is Prime number")
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                print(num, " is not a prime number")
                break
        else:
            print(num, " is a prime number")


check_prime(49)

# write a program to find the sum of all the element of the list.
# summingList = [12, 428, 50, 39, 8, 248]
#
#
# def find_sum():
#     return sum(summingList)
#
#
# print(find_sum())


def add_all(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total


print(add_all([10, 10, 10]))


# same addition of list using recursion method....

def add_all_2(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + add_all_2(numbers[1:])


print(add_all_2([10, 20, 40]))

