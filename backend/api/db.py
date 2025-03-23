import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_PSW = os.getenv("DB_PASSWORD")
DATABASE_URL = f"postgresql://postgres:{DB_PSW}@db.hiknayypstbisgfyltaf.supabase.co:5432/postgres" #os.getenv("DATABASE_URL")
#LOCAL DB DATABASE_URL = "postgresql://postgres:pswww@localhost:5432/postgres"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)