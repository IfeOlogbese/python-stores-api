from db.database import Database
from bson.objectid import ObjectId  # convert string id to BSON object

class ItemModel:
    COLLECTION = "items"

    def __init__(self, _id, name, price, store_id):
        self.id = str(_id) if _id is not None else _id
        self.name = name
        self.price = price
        self.store_id = str(store_id) if store_id else None

    def json(self):
        return {"name": self.name, "price": self.price, "store_id": ObjectId(self.store_id)}

    def load_json(self):
        return {"name": self.name, "price": self.price, "store_id": self.store_id}



    @classmethod
    def find_by_name(cls, name):  # get method for this resource
        row = Database.find_one(ItemModel.COLLECTION, {"name": name})

        if row:
            return cls(**row)

    @staticmethod
    def find_all(query = {}):
        items = Database.find(ItemModel.COLLECTION, query)
        if items:
            return [ItemModel(**item).load_json() for item in items]
        return []

    def save_to_db(self):
        Database.insert(ItemModel.COLLECTION, self.json())

    def update(self):
        Database.update(ItemModel.COLLECTION, {"_id": self.id}, self.json())

    def destroy(self):
        Database.remove(ItemModel.COLLECTION, {"name": self.name})
