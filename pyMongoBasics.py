''' https://www.geeksforgeeks.org/mongodb-and-python/

'''
# importing module
from pymongo import MongoClient

# creation of MongoClient

# Connect with the portnumber and host

try:
    cluster = MongoClient("mongodb://localhost:27017/")

    # cluster = MongoClient("mongodb+srv://ameya:<pwd>@cluster0.csmbw.mongodb.net/<dbname>?retryWrites=true&w=majority")
    # Access database
    db = cluster['testDb']

    # Access collection of the database
    collection = db['testCollection']

    # dictionary to be added in the database: called as post or document
    post1 = {"name": "John", "role": "tester"}

    post2 = {
    "title": 'MongoDB and Python',
    "description": 'MongoDB is no SQL database',
    "tags": ['mongodb', 'database', 'NoSQL'],
    "viewers": 104
    }

    post3 = {"_id": 5, "name": "Akshay", "role": "developer"}

    # inserting the data in the database

    # collection.insert_one(post1)

    # collection.insert_many([post2, post3])

    # find specific data

    results = collection.find({"name": "John"})
    print("\nQuried data")
    for result in results:
        print(result)
        print(result["_id"])

    record = collection.find({"_id": 5})
    print(record)
    for i in record:
        print(i["_id"])

    one_result = collection.find_one({"name": "John"})
    print("\none_result")
    print(one_result)

    # To find() all the entries inside collection name 'footprint'

    cursor = collection.find()
    print("\nAll records in collection")
    for record in cursor:
        print(record)

    # deleting data
    
    # deleted_result = collection.delete_one({"_id": 5})
    # deleted_results = collection.delete_many({})
    # print(deleted_results)
    
    # updating data using $set operator

    # update_result = collection.update_one({"_id": 5}, {"$set":{"name": "Tiem"}})
    # update_result = collection.update_one({"_id": 5}, {"$set":{"address": "141 B"}}) # updating post with field 
    # print(update_result)

    # update_results = collection.update_many({"title": "MongoDB and Python"}, {"$inc": {"viewers": 10}})
    # print(update_results)

    # counting documents

    post_counts = collection.count_documents({})
    print(post_counts)

except Exception as error:
    print(str(error))  
    print("Could not connect to MongoDB")
