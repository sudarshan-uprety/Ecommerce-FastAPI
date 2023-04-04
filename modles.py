from mongoengine import *
import datetime
from passlib.hash import pbkdf2_sha1

class User(Document):
    first_name=StringField(max_length=30,required=True)
    last_name=StringField(max_length=30,required=True)
    email=EmailField(unique=True,required=True)
    phone=IntField(unique=True,required=True)
    password=StringField(required=True,password=True)
    confirm_password=StringField(password=True)
    created_at=DateTimeField(default=datetime.datetime.now)


    def set_password(self,password):
        self.password=pbkdf2_sha1.hash(password)

    def check_password(self,password):
        return pbkdf2_sha1.verify(password,self.password)
    
    meta={'collection':'User','strict':False}
    