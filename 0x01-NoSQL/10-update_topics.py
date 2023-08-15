#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def update_topics(mongo_collection, name, topics):
    """ Update topics of a school document based on school name """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result.modified_count
