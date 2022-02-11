from django.urls import path
from . import views

app_name='testproject'

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('post/post-list', views.PostListView.as_view(), name="post-list"),
    path('<int:id>', views.click, name='click'),
]