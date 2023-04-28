from pymongo.mongo_client import MongoClient
import os
from config import logger
from dotenv import load_dotenv

load_dotenv()

class DB:
    
    def __init__(self) -> None:
        self.uri = os.environ['MONGO_DB_URL']
        self.client = MongoClient(self.uri)
        self.db_name = os.environ['MONGO_DB_NAME']
        
        try:
            # Send a ping to confirm a successful connection
            self.client.admin.command('ping')
            logger.info("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            logger.error(e)
            raise Exception("Unable to connect to the database. Check your uri.")
        
    def get_db(self):
        return self.client[self.db_name]
        

db = DB().get_db()
