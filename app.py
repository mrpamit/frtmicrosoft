#Import Libraries
from flask import Flask, request, render_template
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
 

app = Flask(__name__)
model = pickle.load(open('model_house_price_prediction.pkl', 'rb'))
@app.route('/',methods=['GET'])
 
# render htmp page
@app.route('/')
def home():
    return render_template('index.html')
 
# get user input and the predict the output and return to user
@app.route('/predict',methods=['POST'])
def predict():
     
    #take data from form and store in each feature    
    #[[ "OverallQual", "GrLivArea", "GarageCars", "TotalBsmtSF", "FullBath", "YearBuilt"]]

        YearBuilt = float(request.form['YearBuilt'])
        GarageCars=float(request.form['GarageCars'])
        TotalBsmtSF=float(request.form['TotalBsmtSF'])
    
        OverallQua=float(request.form['OverallQua'])
        GrLivArea=float(request.form['GrLivArea'])
        FullBath=float(request.form['FullBath'])
     
    # predict the price of house by calling model.py
        predicted_price = model.predict(np.array([OverallQua, GrLivArea, GarageCars, TotalBsmtSF, FullBath,YearBuilt ]).reshape(1,-1))    
        print(predicted_price)   


        # render the html page and show the output
        return render_template('index.html', prediction_text='Predicted Price House is {}'.format(predicted_price[0]))

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="8080")
     
if __name__ == "__main__":
    app.run(debug=True)
