#!/usr/bin/env python3
"""
Module provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """
    Prints statistics about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print(f'{collection.estimated_document_count()} logs')

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')

    for req in methods:
        print('\tmethods {}: {}'.format(req,
            collection.count_documents({'method': req})))

    print('{} status check'.format(collection.count_documents(
        {'method': 'GET', 'path': '/status'})))

if __name__ == "__main__":
    log_stats()
