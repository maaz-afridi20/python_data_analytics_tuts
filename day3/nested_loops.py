"""
a loop inside a loop is called nested loops.
nested loop khud koii aik loop naii hai... ye jo b loops hon
or wo aik k ander doosra use ho raha ho..tu uss ko nested loops. kahtay hain

if we want to have the value in one line then we can also use end=""
this will print the values in one line.
"""

# for i in range(1, 4):
#     for j in range(1, 11):
#         print(j, end="")
#     print()


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
