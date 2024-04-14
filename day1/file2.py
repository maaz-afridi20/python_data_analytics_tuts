f"""
variables and user input.

Data types 👇
1 String
2 Numeric(int,float,complex)
3 Sequence (list,tuple,range)
4 Mapping (dictionaries{dict})
5 Set (set,frozenset)
6 Boolean (bool)
7 Binary (byte,bytearray,memoryview)


UserInput 👇
we can use input() for taking input from the users.

if we write simply input() then this will take this input automatically in string
but if we want to take the input in int or float we have to mention it.
like int(input())

=> for decimal we have to use float()
=> eval
 we can use eval for evaluating like for example if we use
 a = eval(42-32) this this will give me the evaluated answer like it will give me 10 ans
"""
name = "ali"
print(name)

name_two = input('enter your name : ')
print(name_two)

age = int(input('enter your age : '))
print(age)

someDecimal = float(input('enter some decimal : '))
print(someDecimal)

exp1 = eval(input('enter some thing. : '))
print(exp1)
