# CRUD Python Module for the AAC animal database

import os

from pymongo import MongoClient


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB."""

    def __init__(self, username=None, password=None):
        # Connection variables
        USER = username if username is not None else 'aacuser'
        PASS = password if password is not None else os.environ.get("AAC_MONGO_PASSWORD")
        if not PASS:
            raise ValueError("Set AAC_MONGO_PASSWORD or pass a MongoDB password.")
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize MongoDB connection
        self.client = MongoClient(
            host=HOST, port=PORT, username=USER, password=PASS
        )
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Implement the C in CRUD.
    def create(self, data):
        """Insert a document into the animals collection."""
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception:
                print("Create operation failed. Check database connectivity and permissions.")
                return False
        else:
            return False

    # Implement the R in CRUD.
    def read(self, query):
        """Query documents from the animals collection."""
        if query is not None:
            try:
                results = self.collection.find(query)
                return list(results)
            except Exception:
                print("Read operation failed. Check database connectivity and permissions.")
                return []
        else:
            return []
        
    # Implement the U in CRUD.
    def update(self, query, new_data):
        """Update documents in the animals collection."""
        if query is not None and new_data is not None:
            try:
                result = self.collection.update_many(
                    query,
                    {"$set": new_data}
                )
                return result.modified_count
            except Exception:
                print("Update operation failed. Check database connectivity and permissions.")
                return 0
        else:
            return 0
        
    # Implement the D in CRUD.
    def delete(self, query):
        """Delete documents from the animals collection."""
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception:
                print("Delete operation failed. Check database connectivity and permissions.")
                return 0
        else:
            return 0