"""
Handling duplicate data :
in order to find the duplicate data we can use

filee = pd.read_csv("D:/assets/kaggledatasets/csv_of_that_zip_files/hotel_booking.csv")
data = pd.DataFrame(filee)

.duplicated() => this will show true where is value duplicated
                 we can also give a specific column name, so it will check in that
                 column like .duplicated("country")
                 or we can also use like this.
                 data["country"].duplicate()
                 this will work same.
                 now this will check whether is there any country name repeating or duplicate.
                 print(data.duplicated("email").sum()) this will show number of values
                 in the email column which are duplicated.

                 agar humein duplicate koii cheez ka pata krna b hai tu aisee cheez prr apply krna hai
                 k uss mein koii duplicate cheez anay k chances na hon. for example k agar hm
                 duplicate ka method name pr laga lein tu iss mein tu bohat say aisay log hongay k
                 jiss k duplicate ho sktay hain. tu humein ye b sochna chaiyee.
                 so humein ye yaar raknaa haii k name, country, age, salary etc ye sari cheezain
                 duplicates ho skti hain tu humein agar kisi duplicate ko pata krna ho ya phirr
                 duplicated ko delete krna ho tu humein aisay kisi column prr aplly krna hai
                 jiss mein duplicate anay k chance na ho jaisay kisi ki employee id.
                 ya phirr kisi user ka id number etc.

.drop_duplicated("column_name") => by this method we can drop or delete all the duplicate values
                                   in some specific column. like
                                   data.drop_duplicate("country")
                                   so in this it will delete all the duplicate country name
                                   in the country column.

"""
import pandas as pd

filee = pd.read_csv("D:/assets/kaggledatasets/csv_of_that_zip_files/hotel_booking.csv")
data = pd.DataFrame(filee)

file2 = pd.read_excel("D:/assets/generaldata/nameage.xlsx")
dd = pd.DataFrame(file2)

print(data.duplicated().head(10))  # will print duplicated values


print(data.isnull().sum())  # will print number(count) of null values
print(data.duplicated("lead_time").sum())  # will print number of duplicated values in "lead_time"
# column and count it and will print

# we can also do this
print(data["adr"].duplicated().sum())  # this will check duplicate specifically in adr column
data["arrival_date_week_number"].isnull().sum()  # is will check null values specifically in arrival_date_week_number column

print(data["customer_type"].isnull().sum())  # is will check null values specifically in customer_type column

dd["empid"].duplicated().sum()   # this will check duplicate specifically in empid column
print(dd.drop_duplicates("empid"))  # this will remove all duplicates values in empid