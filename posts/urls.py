from django.urls import path
from .views import UserDetailView, UserListCreate, PostListCreate, CommentListCreate, PostDetailView, UserCreateAndAssignGroup, UserLogin, PostLikeToggle
from . import views

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/create-and-assign-group/', UserCreateAndAssignGroup.as_view(), name='user-create-assign-group'),
    path('users/login/', UserLogin.as_view(), name='user-login'),

    # Post-related endpoints
    path('posts/', PostListCreate.as_view(), name='post-list-create'),  # For creating and listing posts
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail-view'),  # For updating, viewing, and deleting a specific post
    path('posts/<int:pk>/like/', PostLikeToggle.as_view(), name='post-like-toggle'),  # For liking/unliking a post

    # Comment-related endpoints
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),

    # User detail endpoints
    path('users/<int:id>/', views.UserDetailView.as_view(), name='user-detail'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail-update-delete'),

    # Post detail redundancy cleanup
    path('posts/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail-update-delete'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
