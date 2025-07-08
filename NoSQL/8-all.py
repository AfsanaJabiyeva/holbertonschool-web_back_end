#!/usr/bin/env python3
"""list all documents"""
import pymongo


def list_all(mongo_collection):
    """list documents"""
    return list(mongo_collection.find())


if __name__ == "__main__":
    list_all()

