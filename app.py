#Import dependencies
from flask import Flask, render_template, request
import pandas as pd
import pickle

#Create Flask App
app = Flask(__name__)

#Render Main Page
@app.route("/")
def index():
    return render_template('index.html')

#Read Input and Predict New Value
@app.route("/predict_temperature/", methods=["POST"])
def pred_temp():
    input1 = request.form['input1']
    input2 = request.form['input2']
    input3 = request.form['input3']
    input4 = request.form['input4']

#Calculate latitude and longitude based on received city
    file = 'final_global.csv'
    df = pd.read_csv(file, encoding="ISO-8859-1")
    lat = df.loc[df.City == input4]["Latitude"].values[0]
    lon = df.loc[df.City == input4]["Longitude"].values[0]
    dir_lat = df.loc[df.City == input4]["Dir_Lat"].values[0]
    dir_lon = df.loc[df.City == input4]["Dir_Long"].values[0]

#read model and calculate response
    filename = 'Tempregression.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    res = loaded_model.predict([[input1, input2, input3, lat, lon, dir_lat, dir_lon]])
    return render_template("index.html", res=round(res[0],2), year=input1, month=input2, day=input3, city=input4)

if __name__ == "__main__":
    app.run(debug=True)