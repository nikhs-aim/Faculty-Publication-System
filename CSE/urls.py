from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, PostDeleteView, UpdatePostView, before_login_post_details, conference_details,conferencecreate,journal_details,journalcreate,ConferenceUpdateView,JournalUpdateView,ConferenceDeleteView,JournalDeleteView, post_details


urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.registration_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('hodhomeafterlogin',views.hod_home_after_login,name='hodhomeafterlogin'),
    path('otherhomeafterlogin',views.other_home_after_login,name='otherhomeafterlogin'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('options',views.Options,name='options'),
    path('hodoptions',views.hod_options,name='hodoptions'),
    path('otheroptions',views.other_option,name='otheroptions'),
    path('conferences/', conference_details, name='conferences'),
    path('hodviewotherconf',views.hod_view_other_conference_details,name='hodviewotherconf'),
    path('conf-create/',conferencecreate.as_view(),name='conf-create'),
    path('conferences/<str:pk>/update/', ConferenceUpdateView.as_view(), name='conference_update'),
    path('conferences/<str:pk>/delete/', ConferenceDeleteView.as_view(), name='conference_delete'),
    path('journals/', journal_details, name='journals'),
    path('hodviewotherjourn',views.hod_view_other_journal_details,name='hodviewotherjourn'),
    path('journ-create/',journalcreate.as_view(),name='journ-create'),
    path('journals/<str:pk>/update/', JournalUpdateView.as_view(), name='journal_update'),
    path('journals/<str:pk>/delete/', JournalDeleteView.as_view(), name='journal_delete'),
    path('create_post/', views.create_post, name='create_post'),
    path('post_details', post_details, name='post_details'),
    path('before_login_post_details', before_login_post_details, name='before_login_post_details'),
    path('mypost_details', views.my_post_details, name='mypost_details'),
    path('update_post/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post_delete/<int:pk>',PostDeleteView.as_view(),name='post_delete')

]