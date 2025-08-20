from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SERVER = "192.168.56.1,1433"
DATABASE = "TestDB"
USERNAME = "sa"
PASSWORD = "yakine123"
DRIVER = "ODBC+Driver+18+for+SQL+Server"

# Adding `TrustServerCertificate=yes` to bypass SSL cert check
CONNECTION_STRING = (
    f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}"
    f"?driver={DRIVER}&TrustServerCertificate=yes"
)

engine = create_engine(CONNECTION_STRING, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
