from anyio import run_async_from_thread
import motor.motor_asyncio as motor
from image2 import *
import secrets
import time

accimg="mongodb+srv://image:image@image.amecp0w.mongodb.net/?retryWrites=true&w=majority"
accinfo="mongodb+srv://account:account@account.rqtv0qs.mongodb.net/?retryWrites=true&w=majority"

defaultimg="https://ik.imagekit.io/yriztiyh8jv/avatar/guest"

class acountimage:
	def __init__(self):
		client = motor.AsyncIOMotorClient(accimg)
		db = client.avatar
		self.collect=db.image

	async def insert_default_avatar(self,userid):
		await self.collect.insert_one({"userid":userid,"avatar":'default',"fid":"0",})

	async def update_avatar(self,byt,userid):
		data=await self.find_avatar(userid)
	
		await byt_img(byt,userid)
		
		fid,furl=image_upload(userid)
		
		query={"userid":userid}
		newvalue={"$set":{"avatar":furl,"fid":fid}}
		await self.collect.update_one(query,newvalue)
		
		if data["avatar"] != 'default':
			await image_delete(fid)
		return {"status":1}

	async def find_avatar(self,userid):
		return await self.collect.find_one({"userid":userid})


		

class account(object):
	def __init__(self):
		client = motor.AsyncIOMotorClient(accinfo)
		db = client.account
		self.collect=db.info
		self.img=acountimage()

	async def signup(self,username,password):
		data=await self.collect.find_one({"username":username})
		if data == None:
			userid=secrets.token_hex(16)
			await self.collect.insert_one({"userid":userid,"username":username,"password":password})
			await self.img.insert_default_avatar(userid)
			return username,userid
		return None, None

	async def login(self,username,password):
		data=await self.collect.find_one({"username":username,"password":password})
		if data != None:
			return data["username"],data["userid"]
		return None, None

	async def getavatar(self,userid):
		data = await self.img.find_avatar(userid)
		if data != None:
			if data["avatar"] == 'default':
				return defaultimg
			else:
				return data["avatar"]
		else:return None

	async def postavatar(self,byt,userid):
		return await self.img.update_avatar(byt,userid)
