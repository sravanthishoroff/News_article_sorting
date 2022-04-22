# importing required packages
from flask import Flask, render_template, request, abort
import pandas as pd
import numpy as np
import logging
import pickle
import re
import nltk
# nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn import preprocessing
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# # configuring logging method
logging.basicConfig(filename='info.txt',
                    level=logging.INFO,
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M-%S')

# Load the model
model = pickle.load(open('gnb.pkl', 'rb'))


app = Flask(__name__)


# route for 404 error handler
@app.errorhandler(404)
def page_not_found(error):
    logging.error("Page not found: %s", (request.path))
    return render_template('404.html', title='404 Error', msg=request.path)

# # route for 403 error handler
@app.errorhandler(405)
def page_not_found(error):
    logging.error("Method is not allowed: %s", (request.path))
    return render_template('405.html', title='405 Error', msg=request.path)


# route for 500 error handler
@app.errorhandler(500)
def internal_server_error(error):
    logging.error('Server Error: %s' % error)
    return render_template('500.html', title='500 Error', msg=error)

# route for main page
@app.route('/')
def index():
    try:
        logging.info("someone is accessing index.html!!!")
        return render_template("index.html")
    except Exception as e:
        logging.critical("Cannot able to access index.html...! ")
        return render_template("error.html")
    # return "HI"

# route for prediction 
@app.route('/predict', methods=['POST'])
def predict():
    # try:
        if request.method == 'POST':
            # print("hi")

            article = request.form['article']
            # print(article)
            news = [article]
            # news = news.append(article)
            logging.info("Successfully retrieved information from user...! ")
            vectorizer = TfidfVectorizer(max_features=100)
            result = vectorizer.fit_transform(news)
            print(result)
            result = result.toarray()
            print(result)

            prediction = model.predict(result)
            

            logging.info("Successfully predicted")
        return render_template('Result.html', predict=prediction)

    # except Exception as e:
    #     logging.critical("Found Exception in route /predict: ")
    #     return render_template('error.html')

        
   




if __name__ == "__main__":
    app.run(debug=True)