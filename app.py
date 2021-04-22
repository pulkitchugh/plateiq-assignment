# Required Imports
import os
from flask import Flask
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app , storage
import uuid
import datetime

app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred , {
    'storageBucket' : 'plate-iq-assignment.appspot.com'
})
db = firestore.client()
invoice_ref = db.collection('invoices')
invoice_storage = storage.bucket()



if __name__ == '__main__':
    app.run()