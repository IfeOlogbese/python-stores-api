from app import app
from db.database import Database

@app.before_first_request # initialize database connection
def init_db():
    Database.initialize()