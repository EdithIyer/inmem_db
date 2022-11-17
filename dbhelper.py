import json
import os


class DatabaseHelper(object):
    def __init__(self , location):
        return

    def load(self , location):
       if os.path.exists(location):
           self._load()
       else:
            self.db = {}
       return True

    def set(self , key , value, ext_db):
        try:
            ext_db[str(key)] = value
        except Exception as e:
            print(f"Error Saving Values to Database : {str(e)}")
            return False

    def get(self, key, ext_db):
        try:
            return ext_db[key]
        except KeyError:
            return 'NULL'

    def delete(self , key, ext_db):
        if not key in ext_db:
            return False
        del ext_db[key]
        return

    def counter(self, value, ext_db):
        if len(ext_db) > 0:
            return sum(val == value for val in ext_db.values())
        else:
            return 'NULL'

    def resetdb(self, ext_db):
        ext_db={}
        return True

    def rollback(self, most_recent_transaction, ext_db):
        if most_recent_transaction.get("function") == 'SET':
            del ext_db[most_recent_transaction.get("name")]
        elif most_recent_transaction.get("function") == 'DELETE':
            ext_db[str(most_recent_transaction.get("name"))] = most_recent_transaction.get("value")
        else:
            return 'TRANSACTION NOT FOUND'

