from app import *

ALLOWED_EXTENSIONS = {'pdf'}
UPLOAD_DIRECTORY = "./uploads/"

def upload_file_to_firebase_storage(filename):
    print("uploading File")
    try:
        blob = invoice_storage.blob(filename)
        blob.upload_from_filename(UPLOAD_DIRECTORY+filename)
        print(blob.public_url)
        return blob.public_url
    except Exception as e :
        print(e)
