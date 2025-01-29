from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

DATABASE_URL = "mysql+pymysql://root:0000@localhost:3306/fastapi_blog"

try:
    engine = create_engine(DATABASE_URL, echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False,)
    with engine.connect() as connection:
        print("Database connection successfully!")
except Exception as e:
    print(f"Database connection failed: {e}")   