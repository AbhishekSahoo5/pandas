import pandas as pd

var=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
print(var)

print("--------------------------------")

# Addition
var["SUM"]=var["A"]+var["B"]
print(var)

print("--------------------------------")

# Subtraction
var["SUB"]=var["A"]-var["B"]
print(var)

print("--------------------------------")

# Multiplication
var["MUL"]=var["A"]*var["B"]
print(var)

print("--------------------------------")


# Division
var["DIV"]=var["A"]/var["B"]
print(var)

print("--------------------------------")


var1=pd.DataFrame({"A":[10,20,30,40],"B":[15,16,17,18]})
print(var1)

print("--------------------------------")

var1["A<=20"]=var1["A"] <=20

print(var1)

print("--------------------------------")


var1["B>=16"]=var1["B"] >=16
print(var1)

