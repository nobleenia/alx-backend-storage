#!/usr/bin/env python3
"""
Lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    @mongo_collection: The pymongo collection object
    return: A list of documents, or an empty list if no documents are found
    """
    documents = mongo_collection.find()
    return [document for document in documents]
