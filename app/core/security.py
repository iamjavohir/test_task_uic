from fastapi import Depends, HTTPException, status, WebSocket
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()
VALID_TOKEN = "mysecrettoken123"

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.scheme != "Bearer" or credentials.credentials != VALID_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token"
        )
    return credentials.credentials

async def verify_ws_token(websocket: WebSocket):
    token = websocket.headers.get("authorization")
    if not token or not token.startswith("Bearer ") or token.split(" ")[1] != VALID_TOKEN:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing token")
    return token.split(" ")[1]