#!/usr/bin/env python3
"""
Returns all students sorted by average score
"""
from pymongo.collection import Collection


def top_students(mongo_collection):
    """
    Returns all students from the specified MongoDB collection,
    sorted by their average score. Each student document includes
    an additional field 'averageScore' with the calculated average.

    @param mongo_collection: The pymongo collection object
    return: A list of student documents including their average scores
    """
    pipeline = [
        {
            "$unwind": "$topics"  # Deconstructs 'topics' array field from each input document
        },
        {
            "$group": {  # Groups input documents by the student's id (and name)
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}  # Computes average score
            }
        },
        {
            "$sort": {"averageScore": -1}  # Sorts documents by 'averageScore' in descending order
        }
    ]

    # Execute the aggregation pipeline
    result = list(mongo_collection.aggregate(pipeline))
    return result
