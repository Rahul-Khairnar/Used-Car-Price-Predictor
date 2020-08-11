## Used Car Price Prediction - Project Overview

![alt text](https://github.com/Rahul-Khairnar/Used-Car-Price-Predictor/blob/master/Photos/used_car2.jpg "Localities Explore")

* It is said that India has a very huge market for automobiles. 
* The used car market was valued at USD 24.24 billion in 2019.
* In this market, the price for a car is not given according to any fixed price criterion. 
* Many times, a used car is sold to a customer at a price more than what was expected.
* This used car price prediction application will help people to get an estimated price range between which they should expect the price of the car they are willing to buy.
* This will also help them in selecting the best car in their budget.
* This will also help the customers who are willing to sell their cars get a proper price for their car.

## Resources used and referred

* Programming languages - Python
* Modules used - Numpy, Pandas, Matplotlib, Seaborn, Flask, Jsonify, Pickle, Sklearn
* Machine Learning Algorithms tested - Decisiontree, RandomForests, LinearRegression, Lasso, SVC
* Dataset - https://www.kaggle.com/avikasliwal/used-cars-price-prediction
* Tools used - Jupyter Notebook, Spyder IDE, Anaconda, Postman, Git, Sublime Text 3
* Server - Flask

## About the Dataset

* Columns in the dataset used :-
    * Model_Name
    * Year
    * Location
    * Transmission
    * Engine
    * Power
    * Mileage
    * Fuel
    * Owner_Type
    * Price

* The dataset consists of about 7000 rows with cars for sale from almost all the states from across the India.
* Car models for sale included brands like Maruti, Hyundai, Mahindra, Mercedez-Benz etc.

## Data Cleaning & Exploratory Data Analysis

The dataset received is already cleaned in some columns but some columns need to be cleaned for acheiving maximum performance from algorithm.
* Brand of the car is extracted from the Name column.
* In the column Fuel, LPG, CNG and Electric are changed to Others.
* The engine column is changed to number only by removing the string "CC" from it.
* The power column is changed to number only by removing the string "Hp" from it.
* The mileage column is changed to number only column by removing Kmpl.
* The owner type is changed to categorical data by converting the whole column into two values i.e. "First", "Second or more".

The values in certain columns are converted to lesser categories to avoid overfitting in the machine learning algorithm after converting the dataset to dummies.

* Locations which has highest number of cars for sale.

![alt text](https://github.com/Rahul-Khairnar/Used-Car-Price-Predictor/blob/master/Photos/top_loc.PNG "Localities Explore")


* Models with highest listings.

![alt text](https://github.com/Rahul-Khairnar/Used-Car-Price-Predictor/blob/master/Photos/top_models.PNG "Localities Explore")



* Brands with highest models listed.

![alt text](https://github.com/Rahul-Khairnar/Used-Car-Price-Predictor/blob/master/Photos/top_brands.PNG "Localities Explore")



* Listings in two types of transmissions i.e. Automatic and Manual

![alt text](https://github.com/Rahul-Khairnar/Used-Car-Price-Predictor/blob/master/Photos/transmissions.PNG "Localities Explore")


* Listings in different types of Fuels i.e. Petrol, Diesel and Others which includes LPG, CNG and Electric.

![alt text](https://github.com/Rahul-Khairnar/Used-Car-Price-Predictor/blob/master/Photos/Fuel.PNG "Localities Explore")


* Distribution of car prices is explored.

![alt text](https://github.com/Rahul-Khairnar/Used-Car-Price-Predictor/blob/master/Photos/prices.PNG "Localities Explore")


* Heat map to check for correlations is plotted.

![alt text](https://github.com/Rahul-Khairnar/Used-Car-Price-Predictor/blob/master/Photos/heat_map.PNG "Localities Explore")


## Model Building

* Various algorithms were tested. Algorithms include:-
      * DecisionTree
      * RandomForests
      * LinearRegression
      * Lasso
      * SVC
* Algorithms which performed well include Logistic Regression and Random Forests where Random Forest has an accuracy of almost 92% followed by Linear Regression with an accuracy of about 82%.
* Price predicted by the algorithm using user input data from carwale.com is very close to what is listed by the customer.
* Due to high accuracy, Random Forest is used for further development purposes.

![alt text](https://github.com/Rahul-Khairnar/Used-Car-Price-Predictor/blob/master/Photos/model_performance.PNG "Localities Explore")


## Flask Server

* The model is exported to a pickle file which is then imported in the util.py file.
* Flask server is tested using the Postman app where response from the server can also be easily tested..

![alt text](https://github.com/Rahul-Khairnar/Used-Car-Price-Predictor/blob/master/Photos/postman.PNG "Localities Explore")
