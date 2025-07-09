#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB"""
import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
collection = client.logs.nginx
total = collection.count_documents({})
print(f"{total} logs")
print("Methods:")
for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")
status = collection.count_documents({"method": "GET", "path": "/status" })
print(f"{status} status check")

