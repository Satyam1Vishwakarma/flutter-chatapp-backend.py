from distutils.log import debug
from fastapi import FastAPI, File, UploadFile, WebSocket
from starlette.middleware.cors import CORSMiddleware
from db2 import account
from chat import ConnectionManager
from models import *
import uvicorn
import os

mdb=account()
manager = ConnectionManager()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.websocket("/ws/{userid}")
async def websocket_endpoint(websocket: WebSocket, userid: str):
    await manager.connect(websocket,userid)
    await manager.broadcast({'event':'online','userid':userid})
    try:
        while True:
            data = await websocket.receive_json()
            await manager.broadcast(data)
    except Exception as e:
        manager.disconnect(userid)
        await manager.broadcast({'event':'offline','userid':userid})

@app.post("/signup", response_model=LoginSignUPResponse)
async def signup(data: LoginSignUP):
    username,userid = await mdb.signup(data.username,data.password)
    if username != None or userid != None:
        return {"status":1,"username":username,"userid":userid}
    else:return {"status":0}        
        
@app.post("/login", response_model=LoginSignUPResponse)
async def login(data: LoginSignUP):
    username,userid=await mdb.login(data.username,data.password)
    if username != None or userid != None:
        return {"status":1,"username":username,"userid":userid}
    else:return {"status":0}

@app.get("/getavatar/{userid}")
async def getavatar(userid: str):
    idata=await mdb.getavatar(userid)
    if idata != None:
        return {"status":1,"data":idata}
    else:return {"status":0}

@app.post("/postavatar/{userid}", response_model=PostAvatarResponse)
async def postavatar(userid: str,img: UploadFile = File(...)):
    byt=await img.read()
    await mdb.postavatar(byt,userid)
    return {"status":1}

@app.get("/getusers", response_model=GetUsersResponse)
async def getusers():
    idata = await manager.get_active_users()
    return {"status":1,"data":idata}
    
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    print(port)
    uvicorn.run("main:app", host="0.0.0.0", port=port, workers=1, loop='asyncio', http='httptools', log_level="warning")
