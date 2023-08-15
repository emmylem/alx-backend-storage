#!/usr/bin/env python3
from pymongo import MongoClient

def main():
    # Connect to the MongoDB instance
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Get the total number of documents in the collection
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Compute the number of logs for each HTTP method
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in http_methods:
        method_count = collection.count_documents({"method": method})
        print(f"\t{method}: {method_count} logs")

    # Compute the number of logs with method=GET and path=/status
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} logs with method=GET path=/status")

    # Compute the top 10 most frequent IPs
    top_ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print("Top 10 IPs:")
    for ip_data in top_ips:
        ip = ip_data["_id"]
        count = ip_data["count"]
        print(f"\t{ip}: {count} occurrences")

if __name__ == "__main__":
    main()
