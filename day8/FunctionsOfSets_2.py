"""
FUNCTIONS OF SETS PART 2

👉 UNION                     => this will add all of the values of one set into another set
                                but this will remove the duplicate values.
👉 DIFFERENCE              =>  ye jo hai humein differnce return karega like k union mein jo thaa
                               wo common ko chor deta thaa siraf aik baar print kr leta tha
                               iss mein jo jai agar hum likhein a.difference(b) tu ye iss mei
                               ye karega k jo values a and b mein common hain wo b chor dega
                               orr jo values b ki hain wo b chor dega uss ko b print nai karega
                               siraf or siraf uss values ko print karega jo set a mein hongi
                               common ko b print nai karega or jo second set mein hongi values
                               uss ko b print nai karega.
👉 DIFFERENCE UPDATE =>        the main difference between the difference and the difference_update is k
                               jab hm simple difference ko use krtay hain tu iss mein jo value aati hai wo
                               uss ko new set mein save kr leta hai.
                               magar agar hm chahtay hain k usse same set mein hii difference ajaye tu hm
                               difference_update ko use karengay baki concept sara same hai.
👉 INTERSECTION  =>           intersection only provides the common elements.
                              from both the sets it will provide the common elements.
👉 INTERSECTION UPDATE =>     intersection update has same concept like the difference update
                             like k agar hm chahein k ye jo intersection jo hai humein isse same
                             set mein hii chahiyee tu phirr hm intersection_update ko use krengay...
👉 SYMMETRIC DIFFERENCE =>   ye jo symmetric difference mein wo values hongii jo change hongi like
                             is mein un values ko ignore kr diya jaye gaa jo same hongii orr siraf
                             wohi values ko print kiya jaye ga dono sets mein jo different hongi

👉 SYMMETRIC DIFFERENCE UPDATE => same concept like intersection_update, difference_update like
                                if we want the symmetric differnce in the same set then we will use
                                symmetric_difference_update.
"""


a = {"thor", "ali", "king", "khan", "imran"}
b = {"thor", "this", "imran", "america", "pakistan"}
c = {"india", "srilanka", "pakistan"}

a.union(b)
print(a)
print("------------------difference------------------")

x = a.difference(b)
y = b.difference(a)
print(x)
print(y)

a.difference_update(b)
print(a)

print("------------------intersection------------------")

print(b.intersection(a))
print(b.intersection(c))

b.intersection_update(c)
print(b)

print("------------------symmetric difference------------------")

yeyy = b.symmetric_difference(a)
print(yeyy)


b.symmetric_difference_update(a)
print(b)

