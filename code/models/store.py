from db.database import Database
from models.item import ItemModel
from bson.objectid import ObjectId

class StoreModel:
	COLLECTION = "stores"

	def __init__(self, _id, name):
		self.id = str(_id) if _id is not None else _id
		self.name = name

	def json(self):
		return {"name": self.name}

	def load_json(self):
		return {"name": self.name, "items": self.items}

	@property
	def items(self):
		items = []
		if self.id:
			items = ItemModel.find_all({"store_id": ObjectId(self.id)})

		return items

	@classmethod
	def find_by_name(cls, name):  # get method for this resource
		row = Database.find_one(StoreModel.COLLECTION, {"name": name})

		if row:
			return cls(**row)

	@staticmethod
	def find_all():
		stores = Database.find(StoreModel.COLLECTION, {})
		return [StoreModel(**store).load_json() for store in stores]

	def save_to_db(self):
		Database.insert(StoreModel.COLLECTION, self.json())

	def update(self):
		Database.update(StoreModel.COLLECTION, {"_id": self.id}, self.json())

	def destroy(self):
		Database.remove(StoreModel.COLLECTION, {"name": self.name})
