from flask import jsonify
import pyrebase
import pandas as pd
from time import time

config = {
    "apiKey": "AIzaSyDfqd6oHbt02f7FKoDsofc7052t95iZ6r0",
    "authDomain": "wine-reviews-b9275.firebaseapp.com",
    "databaseURL": "https://wine-reviews-b9275.firebaseio.com",
    "projectId": "wine-reviews-b9275",
    "storageBucket": "wine-reviews-b9275.appspot.com",
    "messagingSenderId": "740632990358",
    "appId": "1:740632990358:web:d0ed0b41582bb618a8a8b7",
    "measurementId": "G-604TW7T0DJ"
    }

firebase = pyrebase.initialize_app(config)
db = firebase.database()

#df = pd.read_csv("C:/Users/rezen/Desktop/Curso_Data_Science/Modulo5/winemag-data-130k-v2.csv")

#del df['Unnamed: 0']
#df = df.dropna()
#df["points"] = df["points"].astype('object', copy=False)
#df["price"] = df["price"].astype('object', copy=False)

#for i in range(1000):
#    id = int(time())+i
#    db.child('wines').child(id).set(df.iloc[i].to_dict())

def remover(timestamp):
    wine = db.child("wines").child(timestamp).get()
    if not wine:
    	return "Wine não encontrado.", 400
    db.child("wines").child(timestamp).remove()
    return jsonify({'sucesso': True})

def atualizar(timestamp, request):
    wine = db.child("wines").child(timestamp).get()
    if not wine:
    	return "Wine não encontrado.", 400
    req = request.json
    db.child("wines").child(timestamp).update(req)
    return jsonify({'sucesso': True})

def buscar(timestamp):
	wine = db.child('wines').child(timestamp).get()
	if not wine:
		return 'Wine não encontrado.', 400
	return jsonify(wine.val())

#def wines_province():
#	wine = db.child("wines").order_by_child("province").get()
#	return jsonify(wine.val())
#
#def wines_points():
#    wine = db.child("wines").order_by_child("points").limit_to_first(15).get()
#    return jsonify(wine.val())

def criar(request):
	id = int(time())+i
	req = request.json
	data = {"country": req["country"], "points": req["points"]}
	db.child('wines').child(str(req["timestamp"])).set(data)
	return "Wine salvo com sucesso!", 200

def wines(request):
    if request.path == '/' or request.path == '':
        if request.method == 'POST':
            return criar(request)
        else:
            return 'Método não suportado.', 400
    
    if request.path.startswith('/'):
        timestamp = request.path.lstrip('/')
        if request.method == 'DELETE' and timestamp is not None:
            return remover(timestamp)
        elif request.method == 'GET' and timestamp is not None:
       		return buscar(timestamp)
        elif request.method == 'PUT' and timestamp is not None:
            return atualizar(timestamp, request)
        else:
            return 'Método não suportado teste.', 400
    return 'URL não encontrada.', 400