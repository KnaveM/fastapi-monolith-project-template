# app/api/routes/websocket_route.py
from fastapi import WebSocket, APIRouter

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"You sent: {data}")
