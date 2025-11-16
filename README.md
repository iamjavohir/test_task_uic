# ===============================
# FastAPI Project - Complete Setup
# ===============================

# 1. Loyihaga kirish
cd /path/to/your/project   # o'z loyihang papkasiga kirish

# 2. Virtual environment yaratish va aktivlashtirish
python3 -m venv .venv
source .venv/bin/activate   # Windowsda: .venv\Scripts\activate

# 3. Pip yangilash va dependencies o‘rnatish
pip install --upgrade pip
pip install -r requirements.txt

# 4. .env faylini yaratish (misol uchun)
cp .env.example .env        # Windows: copy .env.example .env

# 5. Alembic papkasini yaratish va konfiguratsiya (faqat birinchi marta)
alembic init alembic

# 6. Alembic migration yaratish va upgrade
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

# 7. Docker Compose build va run
docker compose up --build -d   # -d detach mode

# 8. Docker Compose to‘xtatish (kerak bo‘lsa)
# docker compose down

# 9. Alembic migrations Docker ichida (agar kerak bo‘lsa)
# docker compose exec web alembic revision --autogenerate -m "Migration name"
# docker compose exec web alembic upgrade head

# 10. FastAPI serverni Docker ichida ishga tushirish
# docker compose exec web uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# 11. Loyiha URLlari
echo "FastAPI docs: http://localhost:8000/docs"
echo "ReDoc: http://localhost:8000/redoc"

# ===============================
# END OF SCRIPT
# ===============================
