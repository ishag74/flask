from Code.db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.FLOAT(precision=2))
    name = db.Column(db.String(80))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModels')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return ItemModel.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
