import pickle
import numpy as np

__model = None
__columns = None

def price_predict(kilometers,mileage,engine,power,seats,age,fuel,transmission,owner,brand):
    columns = ["Kilometers_Driven", "Mileage", "Engine", "Power", "Seats", "Age", "Fuel_Type_Diesel", "Fuel_Type_Others", "Fuel_Type_Petrol", "Transmission_Automatic", "Transmission_Manual", "Owner_Type_First", "Owner_Type_Second or More", "Brand_Audi", "Brand_BMW", "Brand_Chevrolet", "Brand_Datsun", "Brand_Fiat", "Brand_Force", "Brand_Ford", "Brand_Honda", "Brand_Hyundai", "Brand_ISUZU", "Brand_Jaguar", "Brand_Jeep", "Brand_Land", "Brand_Mahindra", "Brand_Maruti", "Brand_Mercedes-Benz", "Brand_Mini", "Brand_Mitsubishi", "Brand_Nissan", "Brand_Porsche", "Brand_Renault", "Brand_Skoda", "Brand_Tata", "Brand_Toyota", "Brand_Volkswagen", "Brand_Volvo"]
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
    return __model.predict([x])[0]

def load_saved_artifacts():
   print("Loading the saved artifacts....")
       
   global __columns
   if __columns is None:
       with open("Car_price_prediction.pickle","rb") as f:
           __columns = pickle.load(f)
   global __model
   if __model is None:    
       with open("Car_price_prediction.pickle","rb") as f:
               __model = pickle.load(f)
                         
if __name__ == '__main__':
    print(price_predict(67000,18,1100,67,5,16,"Petrol","Manual","Second","Hyundai"))