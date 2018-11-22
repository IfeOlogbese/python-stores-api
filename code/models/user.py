from db.database import Database
from bson.objectid import ObjectId  # convert string id to BSON object

class UserModel:
	def __init__(self, _id, username, password):
		self.id = str(_id) if _id is not None else _id
		self.username = username
		self.password = password

	@classmethod
	def find_by_username(cls, username):
		row = Database.find_one('users', {'username': username})

		if row is not None:
			user = cls(**row)
			user.id = str(user.id)  # get the actual string id
		else:
			user = None

		return user

	@classmethod
	def find_by_id(cls, _id):
		# convert string id to BSON object
		row = Database.find_one('users', {'_id': ObjectId(_id)})

		if row is not None:
			user = cls(**row)
		else:
			user = None

		return user

	def save_to_db(self):
		Database.insert(
			"users", {'username': self.username, 'password': self.password})