
import tensorflow as tf 
import random 
import numpy as np
import pandas as pd
import time 
import nltk
nltk.download('punkt')
import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow import keras
from keras.models import Model
from keras.layers import Dense
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
import pickle
from flask import Flask, request, make_response, send_file, render_template
from preprocessing import *
import joblib

#create flask app
app = Flask(__name__)


#load models 
# loading
tokenizer = joblib.load('./tokenizer.joblib')
model_gru = tf.keras.models.load_model('./1670681640.h5')
# print(model_gru.summary())
    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    max_length = 38
    if request.method == 'POST':
        Full_Name = request.form['message']
        Full_Name = [Full_Name]
        
        # print(Full_Name)
        # Create the sequences
        padding_type='post'
        sample_sequences = tokenizer.texts_to_sequences([clean_text(Full_Name[0])])
        # print(sample_sequences)
        fakes_padded = pad_sequences(sample_sequences, padding=padding_type, maxlen=max_length)                      
        # print(fakes_padded)
        classes = model_gru.predict(fakes_padded)
        result  = classes[0][0]
        # print(result)
    return render_template('result.html', prediction = result)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
