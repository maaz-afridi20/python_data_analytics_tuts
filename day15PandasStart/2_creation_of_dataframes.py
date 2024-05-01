"""
Creation of data frames :

we can create any data from by using .DataFrame(any_data)
in the () we can give the value from anywhere like form csv etc.
or we can also give manually by our selves etc.


if we want to import data from any other source then can use .read method

dd = pd.read_csv(data) => for importing data from any csv file
dd = pd.read_excel(data) => importing data from excel file

if we want to open our excel file in pandas then we have to install
pip install (((openpyxl)))

we have to give the path of that file which we want to import
just like this


importing from csv
data = pd.read_csv("D:/assets/kaggledatasets/csv_of_that_zip_files/hotel_booking.csv")

importing from excel file
data = pd.read_excel("D:/assets/generaldata/nameage.xlsx")
print(data)
"""
import pandas as pd

data = {"name":["john","lisa","bala"],
        "age":[43, 43, 13],
        "salary":[44000, 23000, 32000]}

df = pd.DataFrame(data)  # now this will print the data in rows and columns
# just like rows and columns.
print(df)


data2 = pd.read_csv("D:/assets/kaggledatasets/csv_of_that_zip_files/hotel_booking.csv")
print(data2)  # this will load that csv file data and will print.
