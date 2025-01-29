from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from .database import engine

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(String(1000), nullable=False)

    def __repr__(self):
        return f"<Post(id={self.id}, title={self.title}, content={self.content})"