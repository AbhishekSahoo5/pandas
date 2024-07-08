import pandas as pd

l=[1,2,3,4,5,6]

x1=pd.DataFrame(l)

print(x1)
print(type(x1))

# Dictionary Data frames
d={"a":[1,2,3,4,5],"s":[1,100,3,4,5],"d":[1,2,3,4,5],1:[1,2,3,4,5]}
# The length of array must be same
x2=pd.DataFrame(d)
print(x2)
print(type(x2))

# To choose particular column
x3=pd.DataFrame(d,columns=["a",1])
print(x3)
print(type(x3))

# To change the index
x4=pd.DataFrame(d,columns=["a",1],index=["a","s","d","f","g"])
print(x4)
print(type(x4))

# Accessing particular data
x5=pd.DataFrame(d)
print(x5["s"][1])

# DataFrame list of list
l1=[[1,2,3,4,5],[11,12,13,14,15]]
x6=pd.DataFrame(l1)
print(type(x6))
print(x6)

# DataFrames of series
sr={"s":pd.Series([1,2,3,4]),"r":pd.Series([1,2,3,4])}
x7=pd.DataFrame(sr)
print(type(x7))
print(x7)


