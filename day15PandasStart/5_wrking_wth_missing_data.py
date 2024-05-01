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
