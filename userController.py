from invoice import *
from adminController import *
import uuid
import datetime
from fileUploadUtil import *
import os

@app.route('/get_invoice', methods=['GET'])
def get_invoice():
    invoice_id = request.args.get('id')
    try:
        return jsonify({'Invoice': Invoice.get_invoice(invoice_id)})
    except Exception as e:
        print(e)
        return jsonify({"status" : 400 ,"error_mesage": "Error is :{}".format(e) })

@app.route('/upload_invoice' , methods=['POST'])
def upload_invoice():
    uid = uuid.uuid1()
    Invoice.add_invoice(
        str(uid),
        request.form.get('description'),
        str(datetime.datetime.now().timestamp())
    )

    file = request.files['file']
    filename = "File-"+str(uid)+".pdf"
    file.save(os.path.join(UPLOAD_DIRECTORY ,filename ))
    url = upload_file_to_firebase_storage(filename)
    if(url):
        Invoice.update_invoice_uid(url , str(uid))

    return  jsonify({"success": True , "message": "Invoice Added" }), 200

@app.route('/check_file_status', methods=['GET'] )
def get_file_status():
    try: 
        invoice_id = request.args.get('id')
        if invoice_id : 
            invoice = Invoice.get_invoice(invoice_id)
            print(invoice)
            if(invoice[0].get('digitized') != "False"):
                return jsonify({"success": True , "message": "Invoice digitized"}), 200
            else:
                return jsonify({"success": False , "message": "Invoice not digitized "}), 200
    except Exception as e : 
        print(e)
        return jsonify({"status" : 400 ,"error_mesage": "Error is :{}".format(e) }), 400
     

if __name__ == "__main__":
    db.create_all()
    app.run()