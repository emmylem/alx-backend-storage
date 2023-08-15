#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """

def list_all(mongo_collection):
    """ List all documents in Python """
    documents = list(mongo_collection.find())

    if len(documents) == 0:
        return []

    return documents
