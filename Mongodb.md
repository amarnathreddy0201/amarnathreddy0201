# 📘 MongoDB with Python (`pymongo`)

This README provides a **complete reference** to using **MongoDB with Python** via the `pymongo` library.  
It includes installation, connection, CRUD, queries, operators, aggregations, indexing, transactions, bulk operations, schema validation, utilities, and admin commands.

---

## 🐍 Full Python Example (All Functionalities in One File)

```python
# ==============================================
# 🔧 Setup & Connection
# ==============================================
# pip install pymongo dnspython

from pymongo import MongoClient, InsertOne, DeleteOne, ReplaceOne, ASCENDING, DESCENDING
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/")
# client = MongoClient("mongodb+srv://<username>:<password>@cluster.mongodb.net/")

print("Databases:", client.list_database_names())

db = client["mydatabase"]
collection = db["users"]

# ==============================================
# 🟢 Create (Insert)
# ==============================================
collection.insert_one({"name": "Alice", "age": 25, "city": "New York"})
collection.insert_many([
    {"name": "Bob", "age": 30, "city": "London"},
    {"name": "Charlie", "age": 28, "city": "Paris"}
])

# ==============================================
# 🔵 Read (Find)
# ==============================================
print("Find one:", collection.find_one())
for doc in collection.find():
    print(doc)

# Projection
for doc in collection.find({}, {"name": 1, "_id": 0}):
    print("Only name:", doc)

# Sorting & limiting
for doc in collection.find().sort("age", DESCENDING).limit(2):
    print("Sorted + limit:", doc)

# ==============================================
# 🔎 Query Operators
# ==============================================
# Comparison
for doc in collection.find({"age": {"$gt": 25}}): print("Age > 25:", doc)
for doc in collection.find({"age": {"$gte": 28}}): print("Age >= 28:", doc)
for doc in collection.find({"age": {"$lt": 30}}): print("Age < 30:", doc)
for doc in collection.find({"age": {"$ne": 25}}): print("Age != 25:", doc)

# Logical
for doc in collection.find({"$or": [{"city": "London"}, {"city": "Paris"}]}):
    print("OR condition:", doc)

for doc in collection.find({"$and": [{"age": {"$gt": 20}}, {"city": "London"}]}):
    print("AND condition:", doc)

# Membership
for doc in collection.find({"city": {"$in": ["London", "Paris"]}}):
    print("IN list:", doc)

# Regex
for doc in collection.find({"name": {"$regex": "^A"}}):
    print("Name starts with A:", doc)

# Exists / Type
for doc in collection.find({"city": {"$exists": True}}):
    print("Has city field:", doc)

for doc in collection.find({"age": {"$type": "int"}}):
    print("Age type int:", doc)

# ==============================================
# 🟠 Update
# ==============================================
collection.update_one({"name": "Alice"}, {"$set": {"city": "San Francisco"}})
collection.update_many({"city": "London"}, {"$inc": {"age": 1}})
collection.replace_one({"name": "Charlie"}, {"name": "Charlie", "age": 29, "city": "Berlin"})

# Update operators
collection.update_one({"name": "Alice"}, {"$push": {"hobbies": "Reading"}})
collection.update_one({"name": "Alice"}, {"$addToSet": {"hobbies": "Travel"}})
collection.update_one({"name": "Alice"}, {"$pop": {"hobbies": 1}})
collection.update_one({"name": "Alice"}, {"$unset": {"old_field": ""}})

# ==============================================
# 🔴 Delete
# ==============================================
collection.delete_one({"name": "Charlie"})
collection.delete_many({"age": {"$lt": 26}})
# collection.delete_many({})  # remove all

# ==============================================
# 📊 Aggregation Framework
# ==============================================
pipeline = [
    {"$match": {"age": {"$gte": 25}}},
    {"$group": {"_id": "$city", "avg_age": {"$avg": "$age"}, "count": {"$sum": 1}}},
    {"$sort": {"avg_age": -1}}
]
for result in collection.aggregate(pipeline):
    print("Aggregation:", result)

# Common stages
collection.aggregate([{"$project": {"name": 1, "age": 1, "city": 1, "_id": 0}}])
collection.aggregate([{"$match": {"city": "San Francisco"}}])
collection.aggregate([{"$count": "total_users"}])
collection.aggregate([{"$sort": {"age": -1}}])
collection.aggregate([{"$limit": 2}])
collection.aggregate([{"$skip": 1}])

# Advanced
collection.aggregate([
    {"$bucket": {"groupBy": "$age", "boundaries": [20, 25, 30, 35], "default": "Other", "output": {"count": {"$sum": 1}}}}
])
collection.aggregate([
    {"$facet": {
        "byCity": [{"$group": {"_id": "$city", "count": {"$sum": 1}}}],
        "byAge": [{"$group": {"_id": "$age", "count": {"$sum": 1}}}]
    }}
])
# $lookup (join)
orders = db["orders"]
orders.insert_one({"user": "Alice", "product": "Laptop"})
collection.aggregate([
    {"$lookup": {
        "from": "orders",
        "localField": "name",
        "foreignField": "user",
        "as": "orders"
    }}
])

# ==============================================
# 📌 Indexing
# ==============================================
collection.create_index("name")
collection.create_index([("name", ASCENDING), ("age", DESCENDING)])
print("Indexes:", list(collection.list_indexes()))
collection.drop_index("name_1")

# ==============================================
# 🔒 Transactions (replica set / Atlas only)
# ==============================================
# with client.start_session() as session:
#     with session.start_transaction():
#         collection.insert_one({"name": "Eve", "age": 35}, session=session)
#         collection.update_one({"name": "Bob"}, {"$set": {"age": 32}}, session=session)

# ==============================================
# ⚡ Bulk Operations
# ==============================================
requests = [
    InsertOne({"name": "Sam", "age": 22}),
    DeleteOne({"name": "Charlie"}),
    ReplaceOne({"name": "Alice"}, {"name": "Alice", "age": 26, "city": "SF"})
]
result = collection.bulk_write(requests)
print("Bulk result:", result.bulk_api_result)

# ==============================================
# 🛠 Utilities
# ==============================================
print("Count all:", collection.count_documents({}))
print("Count age >= 30:", collection.count_documents({"age": {"$gte": 30}}))
print("Distinct cities:", collection.distinct("city"))

collection.rename("people")
print("Collections after rename:", db.list_collection_names())

# ==============================================
# 🧾 Schema Validation
# ==============================================
validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name", "age"],
        "properties": {
            "name": {"bsonType": "string"},
            "age": {"bsonType": "int", "minimum": 18}
        }
    }
}
db.create_collection("validated_users", validator=validator)

# ==============================================
# 🖥 Admin & Info
# ==============================================
print("Server Info:", client.server_info())
print("Database Stats:", db.command("dbstats"))
print("Collection Stats:", db.command("collstats", "people"))

# ==============================================
# 🧹 Cleanup
# ==============================================
collection.drop()
client.drop_database("mydatabase")
client.close()
