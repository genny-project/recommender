from flask import Flask, Response, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():

	return("Home Page")


@app.route("/scoring",methods=['POST'])
def scoring():
	from sklearn.feature_extraction.text import TfidfVectorizer
	from sklearn.metrics.pairwise import linear_kernel
	from pandas import DataFrame
	import requests
	import json
	import pandas as pd
	from pandas.io.json import json_normalize
	import ast


	#Getting the request data
	request_data = request.get_json()
	base_Entity_X = request_data['base_Entity_X']
	base_Entity_Y = request_data['base_Entity_Y']

	# Getting Auth Token
	headers = {
	    'Content-Type': 'application/x-www-form-urlencoded',
	}

	data = {
	  'username': 'service',
	  'password': 'Wubba!Lubba!Dub!Dub!',
	  'grant_type': 'password',
	  'client_id': 'genny',
	  'client_secret': '056b73c1-7078-411d-80ec-87d41c55c3b4'
	}

	response = requests.post('http://keycloak.genny.life:8180/auth/realms/genny/protocol/openid-connect/token', headers=headers, data=data)
	auth_token = (ast.literal_eval(response.text))['access_token']


	#Getting Base Entity X details
	# Getting all Internships
	headers = {
	    'Content-Type': 'application/json',
	    'Authorization': 'Bearer '+ auth_token,
	}

	response_X = requests.post('http://keycloak.genny.life:8280/qwanda/baseentitys/search', headers=headers, data=json.dumps(base_Entity_X[0]))
	df_X = response_X.json()['items']
	df_X = json_normalize(df_X,record_path='baseEntityAttributes')
	df_X = df_X[['attributeCode','baseEntityCode','valueString']]
	df_X = df_X.pivot(index='baseEntityCode',columns='attributeCode',values='valueString')
	df_toSend = df_X.copy()

	#Cleaning the Data
	df_X.fillna("",inplace=True)
	df_X = df_X.apply(lambda x : x.str.replace('<[^<]+?>', ' '),axis=1)
	df_X = pd.Series(df_X.fillna('').values.tolist()).str.join('')


	#Getting Base Entity Y Details
	response_Y = requests.post('http://keycloak.genny.life:8280/qwanda/baseentitys/search', headers=headers, data=json.dumps(base_Entity_Y[0]))

	df_Y = response_Y.json()['items']
	df_Y = json_normalize(df_Y,record_path='baseEntityAttributes')
	df_Y = df_Y[['attributeCode','baseEntityCode','valueString']]
	df_Y = df_Y.pivot(index='baseEntityCode',columns='attributeCode',values='valueString')

	#Cleaning the Data
	df_Y.fillna("",inplace=True)
	df_Y = df_Y.apply(lambda x : x.str.replace('<[^<]+?>', ''),axis=1)
	df_Y = pd.Series(df_Y.fillna('').values.tolist()).str.join(' ')


	#TFIDF
	tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2), stop_words='english',lowercase=True)

	tf_X = tf.fit_transform(df_X)
	tf_Y = tf.transform(df_Y)

	#Scoring
	sim_scores = list(enumerate(linear_kernel(tf_X,tf_Y)))
	sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[0:5]
	top_indices = [i[0] for i in sim_scores]
	top_X = df_toSend.iloc[top_indices]

	return(str(top_X.index))



if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
