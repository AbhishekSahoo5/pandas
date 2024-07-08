import pandas as pd

var=pd.DataFrame({"A":[1,2,3,4,5],"B":[9,8,7,6,5]})

print(var)

print("-----------------------------------")

# Insert
var.insert(1,"Python",var["A"])
# var.insert(index,col. name, value)

print(var)

print("-----------------------------------")

var.insert(1,"Python_1",[11,12,13,14,15])
print(var)

print("-----------------------------------")

# insert column and copy data upto certain row
var["python_123"]=var["A"][:3]
print(var)

print("-----------------------------------")


#delete
var1=var.pop("Python")
print(var)

print("-----------------------------------")

print(var1)

print("-----------------------------------")

# Deleteing using del keyword
del var["Python_1"]
print(var)
