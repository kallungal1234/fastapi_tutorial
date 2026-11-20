
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus

MYSQL_USER = "anu"
MYSQL_PASSWORD = "Anu@2222"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DATABASE = "fastapi_db"

DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USER}:"
    f"{quote_plus(MYSQL_PASSWORD)}"
    f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
)

# Database connection
engine = create_engine(DATABASE_URL)

# Database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Dependency for database sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Base model
Base = declarative_base()
