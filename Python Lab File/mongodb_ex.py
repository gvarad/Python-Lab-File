import pymongo
db = pymongo.MongoClient("mongodb://localhost:27017")
database = db["Employee4"]
collection = database["empinfo4"]
# dict1 = {"name": "Rohan", "address": "Sangli"}
# collection.insert_one(dict1)

# dict2 = [{"name": "Sammit", "address": "Sangli"},
#          {"name": "Avadhoot", "address": "Pune"}]
# collection.insert_many(dict2)
# print("Data Inserted")

collection.update_one({"name": "Rohan"}, {
    "$set": {"name": "Varad", "address": "Mumbai", "age": 23}})
# read data
# x = collection.find()
# for i in x:
#     print(i)

# # update data
# prev = {"name": "Rohan"}
# nextt = {"$set": {"address": "Pune"}}
# collection.update_one(prev, nextt)

# # delete Data
# d = {"name": "Sammit"}
# collection.delete_one(d)
