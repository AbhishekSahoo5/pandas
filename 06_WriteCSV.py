import pandas as pd

dis={"a":[1,2,3,4,5,6],"s":[1,2,3,4,5,6],"d":[1,2,3,4,5,6]}
d=pd.DataFrame(dis)
print(d)

# to create csv file
d.to_csv("Test_new.csv")
d.to_csv("Test_new1.csv",index=False)
d.to_csv("Test_new2.csv",index=False,header=[1,2,3])