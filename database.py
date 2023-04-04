
from mongoengine import *

def db_connection():
    connect(host="mongodb://localhost:27017/ecommerce")

def db_disconnect():
    disconnect()