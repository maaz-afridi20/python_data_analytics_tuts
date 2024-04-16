"""
1 for loop
2 while loop
3 do while loop
4 nested loop


we can also give any gap so that the number jump that much.
like if we give range(1,11,2) so now this will print 1,3,5,7,9
by jumping 2  , 2 gaps.
"""
print("day 3")

for i in range(1, 11):
    print("hello", i)

for i in range(1, 20, 2):
    print(i)

number = int(input("enter number : "))
for i in range(1, 11):
    print(number, "X", i, "=", number*i)
