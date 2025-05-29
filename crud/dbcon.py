from pymongo import MongoClient
Client=MongoClient("mongodb+srv://matheshmatheshd07:20060904@matheshwaren.3iuyeo1.mongodb.net/")
db=Client["datas"]
col=db["users"]