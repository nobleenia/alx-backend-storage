#!/usr/bin/env python3
"""
Changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the school's name.

    :param mongo_collection: The pymongo collection object
    :param name: The name of the school
    :param topics: The list of new topics to be set for the school
    :return: None
    """
    mongo_collection.update_many(
        {'name': name},  # Query filter to find documents with the given name
        {'$set': {'topics': topics}}  # Update operation to set the 'topics' field
    )
