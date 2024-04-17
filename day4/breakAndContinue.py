"""
Continue: we can use continue statement when we want to skip something
like if we have a loop from 1-10, and we want to skip number 5 then we can use continue statement...
continue only skip that and continue other loop.

Break: if we want to break the loop at certain condition then we can use the
break statement. it will break or stop that loop at that condition.
while break will stop the loop.

break and continue is only used in the loops with the help of conditional statements.

"""

for i in range(1, 11):
    if i == 4:
        continue
    else:
        print(i)

print('break')
for j in range(1, 11):
    if j == 7:
        break  # now after 7 this loop will not execute.
    else:
        print(j)

print("out of loop...")
