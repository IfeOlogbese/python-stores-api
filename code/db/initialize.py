import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = None

""" Create users collection """
collections = mydb.list_collection_names()
users_collection = mydb["users"]

""" Insert default user """
user = {"username": "admin", "password": "password"}

# add admin user if the user hasn't been created already
if user['username'] not in [u['username'] for u in users_collection.find({}, user)]:
    users_collection.insert_one(user)

# show all users in user collection
print([u for u in users_collection.find()])

print(myclient.list_database_names())  # show all databases

# mydb["items"].update_many({}, {'$set': {"store_id": 1}}, upsert=True)
# mydb["items"].update_many({"store_id": 1}, {'$set': {"store_id": ObjectId('5bf1f60a9c31ecbbb89d0d66')}}, upsert=True)
# mydb["stores"].delete_many({})
