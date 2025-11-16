from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.websocket.manager import manager

router = APIRouter()

@router.websocket("/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal(websocket, {"msg": f"You wrote: {data}"})
            await manager.broadcast({"client_id": client_id, "msg": data})
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        await manager.broadcast({"client_id": client_id, "msg": "disconnected"})