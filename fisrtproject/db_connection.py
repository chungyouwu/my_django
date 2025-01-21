import pymongo
url = "mongodb://myroot:0000@localhost:27001/admin"

# 初始化全域 MongoClient
client = pymongo.MongoClient(url)
db = client['django_mongo']