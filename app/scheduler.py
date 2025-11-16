from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger
from datetime import datetime
import asyncio
import logging
from app.websocket.manager import manager

logger = logging.getLogger("scheduler")
sched = AsyncIOScheduler()
_started = False

def start_scheduler():
    global _started
    if not _started:
        try:
            sched.start()
            _started = True
            logger.info("Scheduler started")
        except Exception as e:
            logger.exception("Failed to start scheduler: %s", e)

def schedule_alert(alert_time: datetime, event_id: str, offset_seconds: int):
    if not isinstance(alert_time, datetime):
        raise ValueError("alert_time must be datetime")
    job_id = f"alert-{event_id}-{offset_seconds}"
    try:
        trigger = DateTrigger(run_date=alert_time)
        # async jobni asyncio.create_task orqali ishga tushiramiz
        sched.add_job(
            lambda: asyncio.create_task(_alert_job(event_id, offset_seconds)),
            trigger=trigger,
            id=job_id,
            replace_existing=True
        )
        logger.info("Scheduled alert %s at %s", job_id, alert_time.isoformat())
    except Exception as e:
        logger.exception("Failed to schedule alert %s: %s", job_id, e)

async def _alert_job(event_id: str, offset: int):
    try:
        await manager.broadcast({"type": "alert_fired", "event_id": event_id, "offset": offset})
        logger.info("Alert sent to websocket for event %s", event_id)
    except Exception:
        logger.exception("Error in alert job for event %s", event_id)