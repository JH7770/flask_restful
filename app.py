from flask import Flask, jsonify

from flask_restful import Api
from flask_jwt_extended import JWTManager

from db import db


from services.index import Index
from services.user import UserRegister, UserLogin



app = Flask(__name__)
app.config.from_pyfile("config.py")

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


db.init_app(app)
jwt = JWTManager(app)


api.add_resource(Index, '/')
api.add_resource(UserRegister, '/user/register')
api.add_resource(UserLogin, '/user/login')



if __name__ == "__main__":

    app.run(port=5000, debug=True)
