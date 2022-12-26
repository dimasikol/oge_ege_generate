from django.urls import path
from .views import NewsView,PostListView,PostDetailView
urlpatterns = [
    path('',NewsView.as_view(),name='news_list'),
    path('<slug:category_post>/',PostListView.as_view(),name='news_post'),
    path('<slug:category_post>/<slug:post_slug>/',PostDetailView.as_view(),name='post')
    ]