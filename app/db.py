import motor.motor_asyncio
import os
from config import logger
from dotenv import load_dotenv
from bson.objectid import ObjectId

load_dotenv()

class DB:
    
    def __init__(self) -> None:
        self.uri = os.environ['MONGO_DB_URL']
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.uri)
        self.db_name = os.environ['MONGO_DB_NAME']
        self.db = getattr(self.client.db, self.db_name)
        
        try:
            # Send a ping to confirm a successful connection
            self.client.admin.command('ping')
            logger.info("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            logger.error(e)
            raise Exception("Unable to connect to the database. Check your uri.")
    
    def weeding_helper(self, wedding) -> dict:
        # return {
        #     "id": str(wedding["_id"]),
        #     "main_event_name": wedding["fullname"],
        #     "main_event_host": wedding["email"],
        #     "host_contact": wedding["course_of_study"],
        #     "main_event_start": wedding["year"],
        #     "main_event_end": wedding["gpa"],
        #     "main_event_city": wedding["gpa"],
        #     "main_event_location": wedding["gpa"],
        #     "guest_airport": wedding["gpa"],
        #     "recommended_hotels": wedding["gpa"],
        #     "recommended_activities": wedding["gpa"],
        #     "confirmation_method": wedding["gpa"],
        #     "cancellation_method": wedding["gpa"],
        #     "event_agenda": wedding["gpa"],
        #     "contact_email": wedding["gpa"],
        # }
        return wedding
    
    async def add_wedding(self, wedding_data: dict) -> dict:
        try:
            wedding = await self.db.weddings.insert_one(wedding_data)
            new_wedding = await self.db.weddings.find_one({"_id": wedding.inserted_id})
            return new_wedding
        except Exception as e:
            logger.error(str(e))
            raise Exception(str(e))
    
        

db = DB()
