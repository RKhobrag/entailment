from flask import Flask,render_template,url_for,request, jsonify
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
import RTE

app = Flask(__name__)
rte = RTE.RTE()

@app.route('/')
def home():
	print("-----home--------")
	return render_template('home.html')

# @app.route('/upload_doc')
# def upload_doc():
# 	if request.method == 'POST':


@app.route('/predict',methods=['POST', 'GET'])
def predict():
	print("-----predict--------")
	premise = request.form['premise']
	hypothesis = request.form['hypothesis']
	# premise='hi'
	# hypothesis='hello'
	p = rte.get_score(premise, hypothesis)
	print("passage: ", p)

	return jsonify(fwd=str(p[0]))



if __name__ == '__main__':
	
	app.run(host='0.0.0.0', debug=True, port=5001)