import json
import os


class DatabaseHelper(object):
    def __init__(self):
        self.create_db()

    def create_db(self):
        self.db = {}
        return True

    def set(self , key , value):
        try:
            self.db[str(key)] = value
        except Exception as e:
            print(f"Error Saving Values to Database : {str(e)}")
            return False

    def get(self , key):
        try:
            return self.db[key]
        except KeyError:
            return 'NULL'

    def delete(self , key):
        if not key in self.db:
            return False
        del self.db[key]
        return ##True

    def counter(self, value):
        if len(self.db) > 0:
            return sum(val == value for val in self.db.values())
        else:
            return 'NULL'

    def resetdb(self):
        self.db={}
        return True

    def rollback(self, most_recent_transaction):
        if most_recent_transaction.get("function") == 'SET':
            print('Looking at a set command')
            del self.db[most_recent_transaction.get("name")]
            # self.dumpdb()
        elif most_recent_transaction.get("function") == 'DELETE':
            print('Looking at a del command')
            self.db[str(most_recent_transaction.get("name"))] = most_recent_transaction.get("value")
            # self.dumpdb()
        else:
            return 'TRANSACTION NOT FOUND'

    def show_db(self):
        return self.db

