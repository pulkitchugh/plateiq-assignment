from app import *
import json

db = SQLAlchemy(app)


class Invoice(db.Model):
    __tablename__ = "invoices"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    url = db.Column(db.String(500))
    digitized = db.Column(db.String(5))
    datetime = db.Column(db.String(100))
    mockdata = db.Column(db.String(1000))

    def json(self):
        return {
            "id": self.id,
            "uid":self.uid,
            "description": self.description,
            "url": self.url,
            "digitized": self.digitized,
            "datetime": self.datetime,
            "mockdata": self.mockdata,
        }

    def add_invoice(_uid,  _description, _datetime,):
        new_invoice = Invoice(uid = _uid, description= _description, datetime= _datetime, digitized = "False")
        db.session.add(new_invoice)  
        db.session.commit()

    def get_all_invoice():
        return [Invoice.json(invoice) for invoice in Invoice.query.all()]
    
    def get_invoice(_id):
        return [Invoice.json(Invoice.query.filter_by(id=_id).first())]
    
    def update_invoice(_id, _description, _url, _digitized , _mockdata):
        try:
            invoice_to_update = Invoice.query.filter_by(id=_id).first()
            if _description: 
                invoice_to_update.description = _description
            if _url:
                invoice_to_update.url = _url
            if _digitized:
                invoice_to_update.digitized = _digitized
            if _mockdata:
                invoice_to_update.mockdata = _mockdata
            db.session.commit()

            return True
        except Exception as e:
            print(e)
            return False 

    def update_invoice_uid(_url , _uid):
        invoice_to_update = Invoice.query.filter_by(uid=_uid).first()
        #invoice_to_update.digitized = "False"
        invoice_to_update.url  = _url
        db.session.commit()

    def delete_invoice(_id):
        Invoice.query.filter_by(id=_id).delete()
        db.session.commit()