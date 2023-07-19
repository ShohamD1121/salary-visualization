import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["data-db"]
salaries = db["Salaries"]
