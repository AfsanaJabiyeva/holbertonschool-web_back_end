#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient
def log_stats(mongo_collection):
    """comment"""
    total = collection.count_documents({})
    print(f"{total} logs")
    """count each method"""
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    """count status checks"""
    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")

if __name__=="__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    log_stats(collection)

