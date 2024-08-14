from sqlmodel import create_engine, SQLModel
from sqlalchemy.orm import sessionmaker
from typing import Generator

# URL tidak dimasukkan ke env untuk memudahkan testing
DATABASE_URL = "postgresql://rewashdb_owner:qHIo3F0pxdry@ep-divine-firefly-a109rpce.ap-southeast-1.aws.neon.tech/rewashdb?sslmode=require"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[SessionLocal, None, None]:
    with SessionLocal() as session:
        yield session
