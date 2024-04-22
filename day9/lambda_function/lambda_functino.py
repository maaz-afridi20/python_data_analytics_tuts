"""
Lambda Function :
lambda function aik anonymous function hain iss ka matlab hai k
iss function ko koii name denay ki need nai hai.

tu agar humein koii small cheezain chahiyee jaisay k koii number ko add krna hai
multiply krna hai even, odd find krna hai iss tarah k small functinos
matlab k jo chotay ho tu python khud kahta hai k kia zaroora hai
itnay baray function ko bananay ki k pahlay name likho phir body etc likho..
tu iss k liye hm lambda function ko use kr sktay hainn..
iss mein hm siraf lambda ka name zaroor likhengay....

lambda function is nothing but ye k humein python kahta hai k agar
koi function chota ho tu uss ko waisay hi fuzool mein named function  ko q use
krtay ho.. simple lambda function ko use karo.. jaisay k hm nay even
ko find krnay mein likhaa hai..


it is used when anonymous function is required for very short period of time.
it can take any number of arguments.
it can return only one expression.



lambda is just anonymous function which run for very short period of time.

"""

a = lambda b: b * 19
print(a(10))

# so ye just a mein function ho jaye ga lambda ka
# orr ye b argument lega orr uss argument ko 18 say multiply kr lega.


add = lambda x, y, z: (x + y) * 10  # this is taking
print(add(10, 10, 10))


numbers = [12, 78, 98, 77, 23, 17, 88, 67, 44, 100]


# this is normal named function.....
def even(x):
    return x % 2 == 0


evenss = list(filter(even, numbers))

print("Even Number : ", evenss)


# this is the same function but lambda .....

numbers2 = [12, 78, 98, 77, 23, 17, 88, 67, 44, 100]

evenn2 = list(filter(lambda x: x % 2 == 0 and x > 50, numbers2))
print("Thn number which is greater than 50 and also even are : ", evenn2)


# program for sorting city name according to the length of characters...
city = ["kohat", "islamabad", "karachi", "lahore", "pindi", "peshawar"]


def sorting(city):
    return len(city)


sort = sorted(city, key=sorting)

print("sorted according to city", sort)

# now the same above function with lambda...


sort2 = sorted(city, key=lambda x: len(x))

print("sorted with lamda...", sort2)


# so above both of them working same
