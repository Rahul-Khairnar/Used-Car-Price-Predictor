from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/price_predict',methods=['GET','POST'])
def price_predict():

    kilometers = int(request.form["kilometers"])
    mileage = float(request.form["mileage"])
    engine = int(request.form["engine"])  
    power = float(request.form["power"])
    age = int(request.form["age"])
    fuel = request.form["fuel"]
    seats = int(request.form["seats"])
    transmission = request.form["transmission"]
    owner = request.form["owner"] 
    brand = request.form["brand"]

    response = jsonify({
        'estimated_price':util.price_predict(kilometers,mileage,engine,power,seats,age,fuel,transmission,owner,brand)})
   
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Starting the FLask Server for Car Price Estimation....")
    util.load_saved_artifacts()
    app.run()





