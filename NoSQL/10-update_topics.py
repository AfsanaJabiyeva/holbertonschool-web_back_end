#!/usr/bin/env python3

"""update topics based on name"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """comment"""
    myqueries = {"name": name}
    newvalues = {"$set": {"topics": topics}}
    mongo_collection.update_many(myqueries, newvalues)

