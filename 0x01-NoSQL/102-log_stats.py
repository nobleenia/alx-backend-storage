#!/usr/bin/env python3
"""
Module provides some stats about Nginx logs stored in MongoDB,
including the most frequent IP addresses.
"""
from pymongo import MongoClient


def log_stats():
    """
    Prints statistics about Nginx logs stored in MongoDB,
    including the top 10 most frequent IP addresses.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Get the counts for different HTTP methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    counts = {method: nginx_collection.count_documents({"method": method}) for method in methods}

    # Count foar GET method with path "/status"
    status_check_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})

    # Displaying the results
    print(f"{sum(counts.values())} logs")  # Total logs are the sum of all method counts
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {counts[method]}")
    print(f"{status_check_count} status check")

    # Top 10 most present IPs
    print("IPs:")
    ip_counts = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}  # Limiting to top 10 results within the aggregation pipeline
    ])

    for ip in ip_counts:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    log_stats()
