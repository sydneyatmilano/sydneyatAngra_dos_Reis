# backend/blog/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Post

def index(request):
    return HttpResponse("Welcome to the Blog")

class PostListView(APIView):
    def get(self, request, *args, **kwargs):
        session=SessionLocal()
        try:
            posts = session.query(Post).all()
            post_data = [
                {"id": post.id, "title": post.title, "content": post.content}
                for post in posts
            ]
            return Response(post_data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        finally:
            session.close()
            
    def post(self, request, *args, **kwargs):
        session = SessionLocal()
        data = request.data
        try:
            new_post = Post(title=data['title'], content=data['content'])
            session.add(new_post)
            session.commit()
            return Response({"message": "Post created successfully"})
        except Exception as e:
            session.rollback()
            return Response({"error": str(e)}, status=500)
        finally:
            session.close()

class PostDetailView(APIView):
    def get(self, request, post_id, *args, **kwargs):
        session = SessionLocal()
        try:
            post = session.query(Post).filter(Post.id == post_id).first()
            if post:
                return Response({"id": post.id, "title": post.title, "content": post.content})
            else:
                return Response({"error": "Post not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        finally:
            session.close()

    def put(self, request, post_id, *args, **kwargs):
        session = SessionLocal()
        data = request.data
        try:
            post = session.query(Post).filter(Post.id == post_id).first()
            if post:
                post.title = data.get('title', post.title)
                post.content = data.get('content', post.content)
                session.commit()
                return Response({"message": "Post updated successfully"})
            else:
                return Response({"error": "Post not found"}, status=404)
        except Exception as e:
            session.rollback()
            return Response({"error": str(e)}, status=500)
        finally:
            session.close()

    def delete(self, request, post_id, *args, **kwargs):
        session = SessionLocal()
        try:
            post = session.query(Post).filter(Post.id == post_id).first()
            if post:
                session.delete(post)
                session.commit()
                return Response({"message": "Post deleted succesfully!"})
            else:
                return Response({"error": "Post not found"}, status=404)
        except Exception as e:
            session.rollback()
            return Response({"error": str(e)}, status=500)
        finally:
            session.close()