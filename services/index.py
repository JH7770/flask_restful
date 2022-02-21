from flask_restful import Resource, reqparse
from models.user import UserModel

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_jwt,
)

class Index(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        print("user_id : ", user_id)
        if user_id:
            user_data = UserModel.find_by_id(user_id)
            return f"This is Memo Application. User name : {user_data['username']}", 200
        return 'This is Memo Application. Please log in ', 200
