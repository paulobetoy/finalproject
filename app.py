#Import dependencies
from flask import Flask, render_template, request
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
    # input1 = request.form['input1']
    # input2 = request.form['input2']
    # input3 = request.form['input3']
    # input4 = request.form['input4']
    # input5 = request.form['input5']
    # input6 = request.form['input6']
    # input7 = request.form['input7']
    input1 = 2030
    input2 = 11
    input3 = 1
    input4 = '12.05'
    input5 = '14.79'
    input6 = 1
    input7 = 1
    filename = 'Tempregression.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    res = loaded_model.predict([[input1, input2, input3, input4, input5, input6, input7]])
    return render_template("index.html", res=round(res[0],2))


if __name__ == "__main__":
    app.run(debug=True)