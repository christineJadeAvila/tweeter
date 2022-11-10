from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), 
    path('profile', views.profile, name="profile"),
    path('messages', views.messages, name="messages"),
    path('settings', views.user_settings, name="settings"),
    path('bookmarks', views.bookmarks, name="bookmarks"),
    path('notifications', views.notifications, name="notifications"),

    path('user_post/<str:pk>', views.user_post, name="post")
]