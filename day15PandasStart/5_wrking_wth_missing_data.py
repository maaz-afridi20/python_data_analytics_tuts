"""
working with missing data :

file2 = pd.read_excel("D:/assets/generaldata/nameage.xlsx")
dd = pd.DataFrame(file2)


dd.isnull().sum() => if write this, this will return the name of the columns and then
                     number of null values in front of them.

dd.dropna() =>  this will delete all the NaN values which mean all the null values.
                but just like removing a duplicates we also have to keep in mind that
                where we should use this type of commands because
                agar hm nay ye command use kr liyaa tu jahan prrr NaN hogaa tu
                iss ki waja say uss for eg uss employee ki sari details hii iss k sath
                delete ho jayengii... tu humein soch smj say ye use krnaa hai..
                k for example agar kisi k name mein null value hain
                magar uss ki baki details tu hain like age, salary etc
                agar hm nay ye function use kiyaa tu name ki null value ki waja say uss
                ki ye sari details b delete ho jayengii...

dd.replace()    tu for example hmm kahi koii aisi condition hogii k NaN ko delete naii
                kr sakengay tu humein uss ko raplace krna hoga kisi value say tu humein wahan prr
                .replace() use krna hoga.
                tu .replace() mein 2 parameters hain aik tu ye k humein replace krna kiaa hai
                wo dena hoga orr 2nd ye k kiss cheez say replace krna hai wo b mention krna hoga...
                like eg below.
                nan ko remove krnay k liye hum numpy ka use krtay hain.
                dd.replace(np.nan, "hello")
                tu ab jahan prr b NaN value hogi wahan prr ye hello replace kr dega.
                ye sari jagah prr jahan b nan ho waha hello ajaye ga.

                magar aik problem ye hai k agar salary mein koii nan value hai tu ab wahan
                prr agar hello ajaye gaa tu phirr tu ye ghalat ho gaya tu is k liye hm
                specifically mention b kr sktay hain like
                dd["salary"] = dd["salary"].replace(np.nan, 12000)
                this will go to salary column find the nan value
                and replace with 12000. tu agar ab yahan salary mein
                value 12000 aa b jaye tu masla naii...

                tu humein sari cheezain soch smj k krni hogi tu agar for example hm salary
                ka case lein tu hmm yahan prr ye b kr sktay thay k hm salary ka colum
                le letay orr uss ka mean le letay. or uss k mean ki jo value aati
                tu no NaN values hain uss ko uss mein ki value say replace kr letay
                tu iss say data mein correctness zyada ajati...
                just like....

                dd["salary"].mean() this will give mean of salaries.

                now we can replace this with...

                dd["salary"] = dd["salary"].replace(np.nan, 51755)


                magar agar humein ab koii name haii ya Female, ya Male parameter hai ab hm iss mein tu
                slaray kii values naii dal sktay, ya phirr iss ka mean etc b naii nikal sktay..
                tu ab hm ye kr sktay hain k iss liye aik orr new method haii k
dd.fillna(method="bfill") =>  ab ye, ye karega k for example agar koii column hai uss mein male(m)
                              and felame(f) likhaa hai tu ab hm jab ye lagayengay tu ab ye ye karega
                              k for example jahan prr b value null hai uss k neechay ki value dhekega
                              tu agar wo f hogi tu uss mein f likh lega agar wo m hogi tu uss mein b
                              m likh lega... bfill ka matlab hai k below fill
dd.fillna(method="ffill")  => ye b same work karega ka magar ye oper ki value say fill kar dega
                              jiss tarah bfill say neechay ki value ko dhekh krr null value ko fill
                              kiyaa thaa ye ooper ki value ko dhekh krr fill ke dega.. tu iss mein ab
                              thorii sii correctness ajayee gii...
                              ffill = forward fill

print(dd["gender"].fillna(method="ffill"))  # we can also specify one column....

"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sb

filee = pd.read_csv("D:/assets/kaggledatasets/csv_of_that_zip_files/hotel_booking.csv")
data = pd.DataFrame(filee)

file2 = pd.read_excel("D:/assets/generaldata/nameage.xlsx")
dd = pd.DataFrame(file2)

print(dd)

print(dd.isnull().sum())  # will count of null values

dd.dropna()  # will delete NaN values from the whole file
dd.replace(np.nan, "hello")  # will replace NaN values by hello from the whole file

dd["salary"] = dd["salary"].replace(np.nan, 12000)


print(dd.fillna(method="bfill"))
print(dd.fillna(method="ffill"))

print(dd["gender"].fillna(method="ffill"))  # we can also specify one column....

