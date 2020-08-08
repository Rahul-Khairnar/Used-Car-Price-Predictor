# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 22:15:36 2020

@author: RAHUL KHAIRNAR
"""


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Cleaned_data_final.csv")
df["Age"] = df["Year"].apply(lambda x:2020-x)

X = df.drop("Price",axis=1)
X = X.drop("Name",axis=1)
X = X.drop("Location",axis=1)
X = X.drop("Year",axis=1)
y = df["Price"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=10)   

linreg = LinearRegression()
linreg.fit(X_train, y_train) 
