import motor.motor_asyncio
import asyncio

url="mongodb+srv://test:test@cluster0.x3gat.mongodb.net/account?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(url)
db = client.test
collection = db.test

async def do_insert():
    document = {'key': 'value'}
    await collection.insert_one(document)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(do_insert())
