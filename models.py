from pydantic import BaseModel
from typing import Optional


class LoginSignUP(BaseModel):
	username: str
	password: str

class LoginSignUPResponse(BaseModel):
	status: int = 1
	username: Optional[str] = None
	userid: Optional[str] = None

class GetAvatarResponse(BaseModel):
	status: int = 1
	data: Optional[str]	
		
class PostAvatarResponse(BaseModel):
	status: int = 1
		
class GetUsersResponse(BaseModel):
	status: int = 1
	data: list
		
		
		
