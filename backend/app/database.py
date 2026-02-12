import os
from sqlmodel import create_engine, SQLModel, Session


sqlite_url = os.getenv("SQLITE_URL", "sqlite:///data/database")

engine = create_engine(sqlite_url, connect_args={"check_same_thread": False}, echo=True)#マルチスレッドでのエラーを防ぐ, echo=TrueSQLのログが出る

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session