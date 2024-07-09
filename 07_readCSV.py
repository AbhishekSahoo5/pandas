import pandas as pd


# Read CSV
csv_1=pd.read_csv("E:\\DataAnalytics\\pandas\\pandas\\country.csv")

# no. of rows
csv_2=pd.read_csv("E:\\DataAnalytics\\pandas\\pandas\\country.csv",nrows=5)


print(csv_2)
print(type(csv_2))

print("-----------------------------------")

# select columns
csv_3=pd.read_csv("E:\\DataAnalytics\\pandas\\pandas\\country.csv",usecols=["Code","Name"])

# print(csv_3)

#select columns through index
csv_4=pd.read_csv("E:\\DataAnalytics\\pandas\\pandas\\country.csv",usecols=[0,1])

print(csv_4)


# skip particular row
csv_5=pd.read_csv("E:\\DataAnalytics\\pandas\\pandas\\country.csv",skiprows=[0,3])
print(csv_5)

print("----------------------------------------------")

csv_6=pd.read_csv("E:\\DataAnalytics\\pandas\\pandas\\country.csv",index_col="Code")
print(csv_6)

print("----------------------------------------------")

csv_7=pd.read_csv("E:\\DataAnalytics\\pandas\\pandas\\country.csv",header=2)

print(csv_7)

print("----------------------------------------------")

csv_8=pd.read_csv("E:\\DataAnalytics\\pandas\\pandas\\country.csv",names=["Col1","Col2"])

print(csv_8)

print("----------------------------------------------")

# csv_9=pd.read_csv("E:\\DataAnalytics\\pandas\\pandas\\country.csv",header=None, prefix="col")

# print(csv_9)

print("----------------------------------------------")

csv_10=pd.read_csv("E:\\DataAnalytics\\pandas\\pandas\\country.csv",dtype={"TODAY - VOLUME":float})

print(csv_10)




