from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.routers.pages import router as pages_router
from app.routers.ws import router as ws_router
from app.routers import user, event , auth
from app.scheduler import start_scheduler, schedule_alert
from datetime import datetime, timedelta

app = FastAPI(title="FastAPI WebSocket Chat")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(pages_router)
app.include_router(ws_router , prefix="/ws")
app.include_router(user.router, prefix="/user")
app.include_router(auth.router, prefix="/auth")
app.include_router(event.router, prefix="/event")

@app.on_event("startup")
async def startup_event():
    start_scheduler()

    # Test uchun alertlar
    event_time = datetime.utcnow() + timedelta(minutes=2)  # hozirdan 2 daqiqa keyin
    schedule_alert(event_time - timedelta(minutes=1), "event1", offset_seconds=60)  # 1 daqiqa oldin
    schedule_alert(event_time - timedelta(seconds=30), "event1", offset_seconds=30)  # 30s oldin