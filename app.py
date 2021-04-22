# Required Imports
from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app , storage


app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://127.0.0.1:3306/PlateIQ-Assignment'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred , {
    'storageBucket' : 'plate-iq-assignment.appspot.com'
})
invoice_storage = storage.bucket()



