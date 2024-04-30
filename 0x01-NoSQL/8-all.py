#!/usr/bin/python3
"""
Lists all documents in a collection
"""
from pymongo.collection import Collection


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    @mongo_collection: The pymongo collection object
    return: A list of documents, or an empty list if no documents are found
    """
    documents = list(mongo_collection.find())
    return documents if documents else []
