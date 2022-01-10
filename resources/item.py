from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from Code.models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='this field cannot left blank'
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='Every store requires store id'
                        )

    @jwt_required()
    def get(self, name):
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])

        if item.find_by_name(name):
            return item.json()
        else:
            return {'Message': 'Item is not found.'}

    def post(self, name):
        if ItemModel.find_by_name(name):
            # return self.find_by_name(name)
            return {'Message': 'Item with name {} is already exists.'.format(name)}, 404
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])
        try:
            item.save_to_db()
        except:
            return {'Message': 'An error occurred inserting an item'}, 500
        return item.json()

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'Message': 'Item has been deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, data['price'], data['store_id']) # can be simplified to **data
            return item.save_to_db()
        else:
            item.price = data['price']
            item.save_to_db()
            return item.json()


class ItemList(Resource):

    def get(self):
        #return {'item': [item.json() for item in ItemModel.query.all()]}
        return {'item': list(map(lambda x: x.json(), ItemModel.query.all()))}