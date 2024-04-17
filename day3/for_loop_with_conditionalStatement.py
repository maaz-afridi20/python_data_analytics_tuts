for i in range(1, 11):
    if i == 3:
        print(i, "Song Added To Favourite")
    else:
        print(i)

# for printing the common multiple...

for j in range(1, 101):
    if j % 8 == 0 and j % 12 == 0:
        print("number is ", j)

# same conditional statement with while loop...
print("while loop..")
n = 1
while n <= 10:
    if n == 3:
        print(n, "Added To Favourite")
    else:
        print(n)
    n += 1
