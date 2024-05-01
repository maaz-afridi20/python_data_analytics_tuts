"""
in order to analyze data we have to explore data that what type of data is.
how many null values are there
how many values are string, how many values are int, float, bool etc.
mean all the basic info you have to know.


.head(10) => this will show only first 10 values of data.
.tail(10) => will only print 10 values from tail.
.info() => this will give you the info of the data types of the data.
data.describe() => this will give you mean, std, min, max, and different percentage of the data
                   in row and table form.
                   Describe mein jitnay b numerical columns hain ye un ko find karega
                   or uss mein kuch operation kr k describe kr dega jaisa k ooper mention kiya
                   huaa hai..
data.isnull() => this will show where is null value
data.isnull().sum() => this will sum of all the null values in the
                       rows and columns.
                       this will show you like for example is there is any column named is_canceled
                       now if we use this command this will count number of null values
                       in this is_canceled column and will show the value that how much
                       null values is there.
data["country"].isnull().sum() => if we want to specify some specific column to check
                                  the null data then we can also use that specific column name
                                  so basically here the data is the variable name in which
                                  we have stored the filee data. so if we want to
                                  check whether is there any null value in country column
                                  in the data file then we can use
                                  data["country"].isnull().sum()
                                  so this will give the sum or we can say that
                                  it will give you the count of null values that are null
                                  in country column.

"""
import pandas as pd
filee = pd.read_csv("D:/assets/kaggledatasets/csv_of_that_zip_files/hotel_booking.csv")
data = pd.DataFrame(filee)
print(data.head(10))
print(data.tail(10))
print(data.info())

