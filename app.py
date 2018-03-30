from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserRegistration
from resources.items import Item, Items
from resources.stores import Stores,StoreList
from security import authenticate, identity



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_info.db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'spaguetti_bol'
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth, returns a jwt token

@app.before_first_request#before any request, this will run
def create_tables():
    db.create_all()

#API uses class in order to work

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items,'/items')
api.add_resource(UserRegistration,'/register')
api.add_resource(Stores,'/store/<string:name>')
api.add_resource(StoreList,'/stores')

if __name__ == "__main__":#the file that is run is automatically named name
    from db import db
    db.init_app(app)
    app.run(port=5000, debug = True)
