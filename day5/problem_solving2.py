# # Q1 write a program to separate the values into comma separated values
# A = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
# splitted = A.split(".")
# print("separated values list is : ", splitted)
#
# # Q2  sort the given values.
# b = "zxcvbnmlkjhgfdsaqwertyuiop"
# sortedValues = sorted(b)
# print("sorted values is ", sortedValues)
#
# # Q3 replace some given values
#
# c = "hello"
# print(c.replace("e", "a"))
#
#
# # Q4
# d = "F.R.I.E.N.D.S"
# e = d.replace(".", "")  # this will replace . with empty spaces.
# print(e)


# stringgg = "she sells shells on the sea sore of sea"
# counted = stringgg.count("sea")  # this will count sea in the above string.
# print(counted)
#
# # Q 5 take input from user and then reverse it.
# enter = input("enter any string to reverse it ")
# print(enter[::-1])
#
#
# # Q 6 write a program to check whether it only contain digits.
# anyy = input("input any thing ")
# bb = anyy.isdigit()
# if bb:
#     print("yes! it only contain digits")
# else:
#     print("No! it does not only contain digits")
#
#


# word = input("Enter word to check palindrome : ")
# wordReverse = word[::-1]
# if word == wordReverse:
#     print("yes! Palindrome ")
# else:
#     print("No! not palindrome")


# Q check the word if it contains vowels or not..

aa = input("Enter a word to find number of vowels ")
vowels = 0
for i in aa:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowels += 1


print("number of vowels are ", vowels)

# check the word if it begins with capital letter.


wordd = input("Enter a word to check whether all te words are capital or not : ")
correct = wordd.istitle()
if correct:
    print("yes! all letters are capitalize")
else:
    print("No! all letters are not capitalize")
