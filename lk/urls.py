from django.urls import path
from .views.lk_view import LkView,LKDetailView, LkDetailQuizView,LkViewEdit
from .views.frendship_view import FollowerFriendshipView,FolowingFriendshipView
from .views.image_all_view import ImagesView
urlpatterns = [
    path('',LkView.as_view(),name='home'),

    path('accounts/profile/',LkView.as_view(),name='personal_account'),
    path('lk/<str:user_name>/',LKDetailView.as_view(),name = 'lk_for_look2'),
    path('lk/<str:user_name>/edit/',LkViewEdit.as_view(),name = 'lk_for_look_edit'),
    path('lk/<str:user_name>/quiz/<int:number>/', LkDetailQuizView.as_view(), name='lk_detail_quiz'),
    path('lk/follower/<str:user_name>/', FollowerFriendshipView.as_view(), name='lk_friendships'),
    path('lk/following/<str:user_name>/',FolowingFriendshipView.as_view(),name='lk_followings'),
    path('lk/albom/<str:user_name>',ImagesView.as_view(),name='lk_albom'),


]