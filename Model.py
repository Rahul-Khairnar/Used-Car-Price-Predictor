# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 22:15:36 2020

@author: RAHUL KHAIRNAR
"""


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

from sklearn import linear_model
from sklearn import svm





df = pd.read_csv("Cleaned_data_final.csv")
df.isnull().sum()
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

x = [40000,20.1,1248,88.5,5,3,1,0,0,0,1,1,0]
ranreg.predict([x])





