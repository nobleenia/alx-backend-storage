#!/usr/bin/env python3
"""
Returns the list of school having a specific topic
"""
from pymongo.collection import Collection


def schools_by_topic(mongo_collection: Collection, topic: str):
    """
    Returns a list of school documents that include
    a specific topic in their topics array.

    @param mongo_collection: The pymongo collection object
    @param topic: The topic to search for
    return: A list of school documents with the specific topic
    """
    # Query to find schools with the specified topic in their topics list
    schools = list(mongo_collection.find({'topics': topic}))
    return schools 
