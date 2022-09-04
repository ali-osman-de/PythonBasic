
import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["node-app"]
mycollection = mydb["products"]



# delete

for i in mycollection.find():
    print(i)

result = mycollection.delete_one({'name':'Samsung S20 FE'})
# mycollection.delete_many()
print('*'*50)

for i in mycollection.find():
    print(i)


# update

# for i in mycollection.find():
#     print(i)

# result = mycollection.update_one({'name':'Samsung S22'},{'$set':{'name': 'IPHONE 13 PRO MAX'}})
# # mycollection.update_many

# for i in mycollection.find():
#     print(i)

# sorting

# result = mycollection.find().sort('Price',-1) #1 desc -1 asc

# for i in result:
#     print(i)




# filter

# filter = {"name":"Samsung S22"}

# result = mycollection.find_one(filter)
# result = mycollection.find_one({"_id":ObjectId("6314ac6f7f8bcfb14008c1a1")})

# # result = mycollection.find(filter)

# # for i in result:
# #     print(i)

# print(result)


# find

# result = mycollection.find_one()

# for i in mycollection.find(): # all columns and rows
    # print(i)

# for i in mycollection.find({},{"_id":0,"name":1,"price":1}): #without _id columns
    # print(i)
# print(result)



# print(myclient.list_database_name())

# insert one item

# product = {"name":"Samsung S22", "Price": 10000}

# result = mycollection.insert_one(product)

# print(mydb.list_collection_names())

# print(result)
# print(type(result))
# print(result.inserted_id)

# insert many item

# productList = [
#     {"name":"Samsung S22", "Price": 10000, "Discount": "%10"},
#     {"name":"Samsung S20", "Price": 8000, "Discount": "%22"},
#     {"name":"Samsung S20 FE", "Price": 6000},
#     {"name":"Samsung S10 Lite", "Price": 5000}
# ]

# result = mycollection.insert_many(productList)

# print(result.inserted_ids)