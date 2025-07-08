#!/usr/bin/env python3
"""insert new document"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """comment"""
    document = kwargs
    result = mongo_collection.insert_one(document)
    return result.inserted_id

