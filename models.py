from pydantic import BaseModel
from typing import Optional


class LoginSignUP(BaseModel):
	username: str
	password: str

class LoginSignUPResponse(BaseModel):
	status: int = 1
	username: Optional[str]
	userid: Optional[str]
	userpfp: Optional[str]

class GetAvatarResponse(BaseModel):
	status: int = 1
	data: Optional[str]	
		
class PostAvatarResponse(BaseModel):
	status: int = 1
		
class GetUsersResponse(BaseModel):
	status: int = 1
	data: list
		
		
		
