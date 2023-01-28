from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, conference_details,conferencecreate,journal_details,journalcreate,ConferenceUpdateView,JournalUpdateView,ConferenceDeleteView,JournalDeleteView


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
]