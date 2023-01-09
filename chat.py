from typing import Dict
from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[userid,WebSocket] = {}

    async def connect(self, websocket: WebSocket, userid: str):
        await websocket.accept()
        self.active_connections[userid]=websocket

    def disconnect(self, userid: str):
        del self.active_connections[userid]

    async def broadcast(self, data):
        for k in self.active_connections.keys():
            await (self.active_connections[k]).send_json(data)
            
    async def get_active_users(self):
        return [a for a in self.active_connections.keys()]
