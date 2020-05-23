# -*- coding: utf-8 -*-
"""
Created on Sat May 23 10:20:46 2020

@author: Nimish
"""

from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger      #For UI part
from flasgger import Swagger   


app = Flask(__name__)
Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)

@app.route('/') # Route Path
def welcome():
    return "Welcome Everybody"



@app.route('/predict', methods=['GET'])
def predict_note_authentication():
    
    #This is the Title
    """Lest's Authenticate the Banks Notes                       
    This is using docstrings for specifications.
    ---
    parameters:
        
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values
          
        
    """
    
    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return "Hello The answer is"+str(prediction)

@app.route('/predict_file', methods=['POST'])
def predict_note_file():
    
        #This is the Title
    """Lest's Authenticate the Banks Notes                       
    This is using docstrings for specifications.
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true
          
    response:
        200:
            The output values
        
    """
    
    df_test= pd.read_csv(request.files.get('file'))
    prediction = classifier.predict(df_test)
    return "The predicted for the csv is"+str(list(prediction))


if __name__ == '__main__':
    app.run()