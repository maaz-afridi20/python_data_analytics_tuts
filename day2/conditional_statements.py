"""
if the, if-else, if-elif-else, nested statement, shorthand if statement


👉
"""

a = 50

#  if statement.
if a < 10:
    print('false')


#  if else statement.
if a > 10:
    print('true')
else:
    print('else statement')


print('----------------------------')
#  if-elif-else statement
marks = 98
if marks >= 90:
    print('enjoy the trip')
elif marks >= 80 and marks < 90:
    print('new phone')
elif marks >=70 and marks <80:
    print('new book')
else:
    print('nothing..')

print('----------------------------')
print('nested if')
#  nested if statement.


if marks >= 80:
    print('goog practice')
    if marks >= 90:
        print('very good.')
else:
    print('noting.')


# -------------------------------------------------------------------------
# short handed if statement.
#  in the shorthand statement we use the condition and body of if in the same line

if marks >= 90:print('yes true')

# -------------------------------------------------------------------------
# short handed if else statement.
#  in the shorthand statement we use the condition and body of if in the same line
# in this first we will write the body of the if and then the condition and then the else statement

print('new phone') if marks > 90 else print('no phone')
# so this will print new phone statement because the marks are more than 90

# in the on liner statement of if else we don't use :
