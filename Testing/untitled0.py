import os
import numpy as np
import pandas as pd

df = pd.read_csv('sales_data_sample.csv', encoding="cp1252", index_col="ORDERNUMBER")

def fun(value):
    if value >= 35:
        return("yes")
    else:
        return("no")
        
df["OVERBOUGHT"] = df["QUANTITYORDERED"].apply(fun)
#print(df["OVERBOUGHT"])

count_yes = 0
for value in df["OVERBOUGHT"]:
    if value == "yes":
        count_yes += 1
    else:
        count_yes += 0 
        
#print(count_yes)

#print(df["COUNTRY"].value_counts()["USA"])

sales_max = df["SALES"].max()
#df["SALES"] = df["SALES"].apply(lambda x: x/sales_max)
#df = df.sort_values(by="ORDERNUMBER", ascending = True)
#print(df["SALES"])
#print(sales_max)
#print(df["SALES"].head(5))

#df["SALES"].head(5).plot.bar()

df["POSTALCODE"] = df["POSTALCODE"].fillna(0)
#print(df["POSTALCODE"].loc[10159])

#print(df)

df["POTENTIALPROFIT"] = df["QUANTITYORDERED"]*df["PRICEEACH"]
#print(df["POTENTIALPROFIT"].head(5))

df = df[["QUANTITYORDERED", "POTENTIALPROFIT"]].shift(1) 
print(df["POTENTIALPROFIT"].head(5))