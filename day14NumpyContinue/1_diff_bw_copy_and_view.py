"""
COPY AND VIEW :
BOTH copy and view both used for copying but there is differences in both.

MAIN DIFFERENCES :

Copy :
1)  in copy jab ham data ko copy krtay hain array say tu wo uss ko koii new
    jagah pr save krta haii.
    matlab k new space storage mein create ho jati hai...
2)  in copy agar for example hm nay original data mein koii changes ki tu
    uss say copy hue data ko koii far nai parega. wo waisa hi hoga jaisay copy hua tha.
    qk wo tu new jagah pr save hua hoga.



View :
1)  in view jab hm data ko copy krtay hain tu wo data ko usse jagah pr save krta hai
    uss k liyee koii new space create nai krta...
2)  agar hm original data mein koii changes kr lein tu uss mein jo view data hoga uss mein
    b changes hogi. it's opposite of copy.
    tu matlab k agar hm changes karengay original mein tu wo changes view hue data mein b hogi.


so it depends on us that when to use .copy and when to use .view
jab hm chahein k humein data pr kuch cheezain perform krni hai  magar hm chahtay hain  k
original data mein koii changes na ayee tu hm copy ka use kr sktay hain.

agar hm chahein k khair hai original data mein kuch changes aa b jaye
tu phir hm view ka use kr sktay hain...

it depend on us.

"""
import numpy as np

# for copying
print("copy....")
var1 = np.array([1, 3, 4, 9])
cp = var1.copy()

print("var : ",var1)
print("copy : ",cp)

# --------------------------------------------------------------------
# for View....
print("view....")
var = np.array([1, 3, 4, 9])
vii = var.view()
print("var : ",var)
print("view : ",vii)

print("Example of Changing original data...")
var = np.array([1, 3, 4, 9])
cp = var.copy()

var[1] = 50

print("var : ",var)
print("copy : ",cp)

"""
in above example agar hm is ko run karein tu hm nay 1st index pr value ko change ki hai
tu agar hm iss ko ab run karengay tu var wali array mein 1st index pr 3 ki jagah 50 ajaye gii
magar agar hmm neechay copy wali array ko print karengay tu wohii 3 aye ga..
qk copy mein data new jagah pr store hota hai. or agar original mein data koii changes aa b jaye
tu copy wala data wohi purana hoga. 
"""