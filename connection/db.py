from flask_pymongo import pymongo

client = pymongo.MongoClient('mongodb+srv://koude:123@cluster0.yerxu.mongodb.net/bankDB?retryWrites=true&w=majority')
db = client.test
