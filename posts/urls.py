from django.urls import path
from .views import UserDetailView, UserListCreate, PostListCreate, CommentListCreate, PostDetailView, UserCreateAndAssignGroup, UserLogin
from . import views
urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/create-and-assign-group/', UserCreateAndAssignGroup.as_view(), name='user-create-assign-group'),
    path('users/login/', UserLogin.as_view(), name='user-login'),
    path('posts/', PostListCreate.as_view(), name='post-list-create'), # For creating and listing posts
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail-view'),# For updating, viewing, and deleting a specific post
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:id>/', views.UserDetailView.as_view(), name='user-detail'),
    path('posts/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail-update-delete'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail-update-delete'),
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
