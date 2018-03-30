import sqlite3
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from flask import request,jsonify
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()#Alows control over which contents are passed through json
    parser.add_argument('price',
    type = float,
    required=True,
    help = 'This field cannot be left in blank'
    )
    parser.add_argument('store_id',
    type = int,
    required=True,
    help = 'Every item requires a store id'
    )

    #@jwt_required()#gate-keeper which requires a token
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(),200

        return {'message': 'no such item was found'},404

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {"message": "That item {} already exists".format(name)},400
        data=Item.parser.parse_args()
        item = ItemModel(name,**data)
        try:
            item.save_to_db()
        except:
            return{"message":"an error occurred when inserting {}".format(name)},500
        return item.json(), 201

    @jwt_required()
    def delete (self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"Message:": "Item deleted"}
        return {"Message:":"Item not found"}

    def put (self,name):
        data=Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item==None:
            item = ItemModel(name,**data)
        else:
            item.price=data['price']
        item.save_to_db()

        return item.json(),200




class Items(Resource):
    #@jwt_required()
    def get(self):
        return {"Items":list(map(lambda x: x.json(), ItemModel.query.all()))}
