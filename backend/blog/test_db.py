from sqlalchemy import SQLColumnExpression
from database import SessionLocal, engine
from models import Post
def test_database():
    db = SessionLocal()
    try:
        posts = db.query(Post).all()
        print(posts)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()