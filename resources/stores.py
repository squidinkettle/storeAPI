from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from flask import request,jsonify
from models.store import StoreModel


class Stores(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
    type = str,
    required = True,
    help = 'please fill in this element')

    def get(self,name):
        store = StoreModel.define_by_name(name)
        if store:
            return {"Store":store.json()}
        return {"message":"No such store was found"},404

    def post(self,name):
        store = StoreModel.define_by_name(name)
        if store:
            return {'message':'That store already exists'}
        store = StoreModel(name)
        try:
            store.save_to_db()
            return store.json(),201
        except:
            return {"message": "an error occurred"},500

    def delete(self,name):
        store = StoreModel.define_by_name(name)
        if store:
            store.delete()
            return {"message":"Store succesfully deleted"}
        return {"message":"No such store found"},404


class StoreList(Resource):
    def get(self):
        return {"Stores":[stores.json() for stores in StoreModel.query.all()]}
