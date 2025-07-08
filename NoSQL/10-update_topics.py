#!/usr/bin/env python3
import pymongo
"""update topics based on name"""


def update_topics(mongo_collection, name, topics):
    """comment"""
    myqueries = {"name": name}
    newvalues = {"$set": {"topics": topics}}
    mongo_collection.update_many(myqueries, newvalues)

