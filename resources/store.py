from flask_restful import Resource
from Code.models.store import StoreModels


class Store(Resource):
    def get(self, name):
        store = StoreModels.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store was not found'}, 404

    def post(self, name):
        store = StoreModels.find_by_name(name)
        if store:
            return {'message': "A store with name '{} is already exists".format(name)}, 400

        store = StoreModels(name)
        try:
            store.save_to_db()
        except:
            return {'Message': 'An error occurred while creating store.'}, 500
        return store.json(), 201

    def delete(self, name):
        store = StoreModels.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'Store deleted'}
        return {'Message': "No store with such name '{}'.".format(name)}


class StoreList(Resource):
    def get(self):
        return {'Stores': [store.json() for store in StoreModels.query.all()]}
