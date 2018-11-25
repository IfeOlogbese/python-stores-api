from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required  # import JWT
from db.database import Database
from models.item import ItemModel


class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price', type=float, required=True,
						help="This field cannot be left blank")
	parser.add_argument('store_id', type=str, required=True,
						help="Every item needs a store id")

	@jwt_required
	def get(self, name):  # get method for this resource
		item = ItemModel.find_by_name(name)

		if item:
			return item.load_json()

		return {'message': 'Item not found'}, 404

	def post(self, name):  # post method for this resource
		if ItemModel.find_by_name(name):
			# bad request
			return {'message': 'An item with name {} already exists'.format(name)}, 400

		data = Item.parser.parse_args()
		item = ItemModel(None, name, **data)

		try:
			item.save_to_db()
		except:
			return {"message": "An error occurred while inserting the client."}, 500

		return item.json(), 201  # return 201 if item has been created

	@jwt_required
	def delete(self, name):
		item = ItemModel.find_by_name(name)
		if item:
			item.destroy()
			return {'message': 'Item deleted'}

		return {'message': 'Item could not be found'}

	def put(self, name):
		data = Item.parser.parse_args()

		item = ItemModel.find_by_name(name)

		if item is None:
			item = ItemModel(None, name, **data)
			item.save_to_db()
		else:
			item.price = data['price']
			item.update()

		return item.json()


class ItemList(Resource):
	def get(self):  # get method for this resource
		items = ItemModel.find_all()

		return {'items': items}
