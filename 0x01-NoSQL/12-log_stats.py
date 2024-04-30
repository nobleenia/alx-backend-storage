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

    # Fetch and print the total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Display method usage statistics
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_count}")

    # Count and display the number of GET requests to the '/status' path
    status_checks = collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_checks} status check")

    # Display the top 10 most frequent IP addresses (added requirement)
    print("IPs:")
    top_ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    log_stats()
