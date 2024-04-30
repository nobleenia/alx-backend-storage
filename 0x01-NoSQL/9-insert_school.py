#!/usr/bin/env python3
"""
Inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection 
    based on provided keyword arguments.

    @param mongo_collection: The pymongo collection object
    @param kwargs: Keyword arguments that define the document to insert
    return: The _id of the new document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
