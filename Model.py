# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 22:15:36 2020

@author: RAHUL KHAIRNAR
"""


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import pickle
import json

df = pd.read_csv("Cleaned_data_final.csv")
cars = df["Name"].unique().tolist()
df["Brand"] = df["Name"].apply(lambda x:x.split(" ")[0])
df3 = df.dropna()
df3["Age"] = df3["Year"].apply(lambda x:2020-x)
df1= df3.copy()


df1 = df1.drop("Name",axis=1)
df1 = df1.drop("Location",axis=1)
df1 = df1.drop("Year",axis=1)
df_dummy = pd.get_dummies(df1)
y = df_dummy["Price"]
df_dummy_dupli = df_dummy.copy()
X = df_dummy_dupli.drop("Price",axis = 1)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=10)   

linreg = LinearRegression()
linreg.fit(X_train, y_train) 
linreg.score(X_test,y_test)

ranreg = RandomForestRegressor(n_estimators = 100,criterion="mse")
ranreg.fit(X_train,y_train)
ranreg.score(X_test,y_test)

def price_predict(kilometers,mileage,engine,power,seats,age,fuel,transmission,owner,brand):
    columns = X_train.columns.tolist()
    print(type(columns))
    x = np.zeros(len(columns))
    x[0] = kilometers
    x[1] = mileage
    x[2] = engine
    x[3] = power
    x[4] = seats
    x[5] = age
    for d in columns:
        if fuel in d:
            pos = columns.index(d)
            x[pos] = 1
        if transmission in d:
            pos = columns.index(d)
            x[pos] = 1
        if owner in d:
            pos = columns.index(d)
            x[pos] = 1
        if brand in d:
            pos = columns.index(d)
            x[pos] = 1
    return ranreg.predict([x])[0]

list1 = price_predict(67000,18,1100,67,5,16,"Petrol","Manual","Second","Maruti")
print("Rs.",round(list1,2),"Lacs")

with open("Car_price_prediction.pickle","wb") as f:
    pickle.dump(ranreg,f)

columns = X_train.columns.tolist()
with open("columns.json","w") as f:
    f.write(json.dumps(columns))
    



