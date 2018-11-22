import pymongo
from db.database import Database
from models.user import UserModel
from flask_restful import Resource, reqparse



class UserRegister(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('username', type=str, required=True,
						help="This field cannot be blank.")
	parser.add_argument('password', type=str, required=True,
						help="This field cannot be blank.")

	def post(self):
		data = UserRegister.parser.parse_args()

		if UserModel.find_by_username(data['username']):
			return {"message": "A user with that username already exists"}, 400

		new_user = UserModel(_id = None, username = data['username'], password = data['password'])
		new_user.save_to_db()

		return {"message": "User created successfully."}, 201
