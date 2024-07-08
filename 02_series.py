import pandas as pd


x=[3,4,5,6]
var=pd.Series(x)

print(var)

print(type(var))

print(var[2])

x2=pd.Series(x,index=['a','s','d','f',])
print(x2)

x3=pd.Series(x,index=['a','s','d','f',], dtype="float", name="pythonAB")
print(x3)

print("--------------------------------------------------------")

dic={"name":['python','c','c++','java'],"por":[12,13,14,15],"rank":[1,4,3,2]}
x4=pd.Series(dic)
print(x4)



s=pd.Series(12,index=[1,2,3,4,5,6,7])
print(s)
print(type(s))


s1=pd.Series(12,index=[1,2,3,4,5,6,7])
s2=pd.Series(12,index=[1,2,3,4])

print(s1+s2)