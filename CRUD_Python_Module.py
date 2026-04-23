# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password):  
        # Connection Variables 
        USER = username 
        PASS = password  # No longer hardcode user and pw
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 

        # Initialize Connection 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client[DB] #Directly used variables for DB and COL to improve readability
        self.collection = self.database[COL] 

    # Create a method to return the next available record number for use in the create method
    
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            try: 
                # Use the collection variable defined in __init__
                self.collection.insert_one(data)
                return True
            except Exception as e: 
                # catch an error and return False
                print(f"An error occurred: {e}")
                return False
        else: 
            # The data was empty/None, so we return False per the prompt
            return False

    # Create method to implement the R in CRUD.
    def read(self, criteria):
        # If criteria is None, find() usually returns everything
        if criteria is not None:
            try:
                # Use find() as specified 
                cursor = self.collection.find(criteria)
                
                # Exhaust the cursor and give the user actual data
                result_list = list(cursor)
                return result_list
            
            except Exception as e:
                print(f"An error occurred during the read operation: {e}")
                return []
        else:
            # Return an empty list if criteria is missing
            return []
        
    # Create method to implement the U in CRUD.
    def update(self, criteria, data):
        if criteria is not None and data is not None:
            try:
                result = self.collection.update_many(criteria, {"$set": data})
                
                # Return the number of objects modified 
                return result.modified_count
            except Exception as e:
                print(f"An error occurred during update: {e}")
                return 0
        else:
            # If arguments are missing
            return 0

    # Delete method to implement the D in CRUD.
    def delete(self, criteria):
        if criteria is not None:
            try:
                # delete_many removes all documents matching the criteria
                result = self.collection.delete_many(criteria)
                
                # Return the number of objects removed as requested by the prompt
                return result.deleted_count
            except Exception as e:
                print(f"An error occurred during deletion: {e}")
                return 0
        else:
            # If criteria is missing, return 0 (no records removed)
            return 0