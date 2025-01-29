from database import engine, SessionLocal
from models import Base, Post

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database initialized")

def add_sample_posts():
    session = SessionLocal()
    try:
        post1 = Post(title="First Post", content="This is the content of the first post")
        post2 = Post(title="Second Post", content="This is the content of the second post")

        session.add(post1)
        session.add(post2)
        session.commit()
        print("Sample posts added")
    finally:
        session.close()

def fetch_posts():
    session = SessionLocal()
    try:
        posts = session.query(Post).all()
        for post in posts:
            print(post)
    finally:
        session.close()

if __name__ == "__main__":
    init_db()
    add_sample_posts()
    fetch_posts()

Base.metadata.craete_all(bind=engine)
print("Database tables created.")