from invoice import *

@app.route('/admin/get_invoice', methods=['GET'])
def admin_get_invoice():
    invoice_id = request.args.get('id')
    if invoice_id: 
        try:
            return jsonify({'Invoice': Invoice.get_invoice(invoice_id)})
        except Exception as e:
            print(e)
            return jsonify({"status" : 400 ,"error_mesage": "Error is :{}".format(e) })
    else:
        try:
             return jsonify({'Invoices': Invoice.get_all_invoice()})
        except Exception as e: 
            print(e)
            return jsonify({"status" : 400 ,"error_mesage": "Error is :{}".format(e) })   

@app.route('/admin/update_invoice', methods=['POST'] )
def admin_update_data():
    invoice_id = request.form.get('id')
    status = Invoice.update_invoice(invoice_id,request.form.get('description')  ,request.form.get('url') ,request.form.get('digitized'),request.form.get('mockdata'))
    if(status):
        return jsonify({"success": True , "message": "Data Updated"}), 200
    else:
        return jsonify({"success": False , "message": "Data Not Updated"})
