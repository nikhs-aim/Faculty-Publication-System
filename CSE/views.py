from urllib import request
from django.shortcuts import render
from .models import Conference, Faculty,Journal, Post
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import PostForm, RegistrationForm
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from django.contrib.auth.views import LoginView       # view for handling user authentication and login.
from .models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin







class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm         # handles the logic for validating the login form and authenticating the user.

    def get_success_url(self):         # overridden to check the role of the user after login
        user = self.request.user
        if user.role == "HOD":
            return reverse_lazy('post_details')      # reverse_lazy - determine the URL to redirect the user
        elif user.role == "OTHER":
            return reverse_lazy('post_details')




def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('login')                      # redirect user to login page after registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})



def to_add_publications(request):
    return render(request,'toaddpublications.html')

def Options(request):
    return render(request,'options.html')


def other_option(request):
    return render(request,'otheroption.html')


def hod_options(request):
    return render (request,'hodoption.html')




def conference_details(request):
    if request.user.is_authenticated:
        conferences = Conference.objects.filter(fac_id=request.user.fac_id)
    return render(request, 'conferencedetail.html', {'conferences': conferences})



def hod_view_other_conference_details(request):
    if request.user.is_authenticated:
        conferences=Conference.objects.exclude(fac_id=request.user.fac_id)
    return render(request, 'hodviewconferencedetail.html', {'conferences': conferences})




class conferencecreate(CreateView):
    model=Conference
    fields = ['conference_id', 'conference_name', 'conference_article', 'conference_doi', 'ugc_listed']
    template_name='conferencecreate.html'
    success_url=reverse_lazy('conferences')
   
    def form_valid(self, form):
        fac = Faculty.objects.get(username=self.request.user)
        form.instance.fac_id = fac
        return super().form_valid(form)




class ConferenceUpdateView(UpdateView):
    model = Conference
    fields = [ 'conference_name', 'conference_article', 'conference_doi', 'ugc_listed']
    template_name = 'conferenceupdate.html'
    success_url = reverse_lazy('conferences')
    pk_url_kwarg = 'pk'
    
    def form_valid(self, form):
        conference = self.get_object()
        form.save()
        return HttpResponseRedirect(self.get_success_url())




class ConferenceDeleteView(DeleteView):
    model = Conference
    template_name = 'conferencedelete.html'
    success_url = reverse_lazy('conferences')





def journal_details(request):
    if request.user.is_authenticated:
        journals = Journal.objects.filter(fac_id=request.user.fac_id)
    return render(request, 'journaldetail.html', {'journals': journals})





def hod_view_other_journal_details(request):
    if request.user.is_authenticated:
        journals=Journal.objects.exclude(fac_id=request.user.fac_id)
    return render(request, 'hodviewjournaldetail.html', {'journals':journals})




class journalcreate(CreateView):
    model=Journal
    fields = ['journal_id', 'journal_name', 'journal_article', 'journal_doi', 'ugc_listed']
    template_name='journalcreate.html'
    success_url=reverse_lazy('journals')
   
    def form_valid(self, form):
        fac = Faculty.objects.get(username=self.request.user)
        form.instance.fac_id = fac
        return super().form_valid(form)



class JournalUpdateView(UpdateView):
    model = Journal
    fields = [ 'journal_name', 'journal_article', 'journal_doi', 'ugc_listed']
    template_name = 'journalupdate.html'
    success_url = reverse_lazy('journals')
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        conference = self.get_object()
        form.save()
        return HttpResponseRedirect(self.get_success_url())




class JournalDeleteView(DeleteView):
    model = Journal
    template_name = 'journaldelete.html'
    success_url = reverse_lazy('journals')


 


def create_post(request):
     if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.fac_id = request.user
            post.save()
            return redirect('post_details')
     else:
        form = PostForm()
     return render(request, 'postcreate.html', {'form': form})



def post_details(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, 'postdetail.html', {'posts': posts})


def before_login_post_details(request):
        posts = Post.objects.all()
        return render(request, 'beforeloginpostdetail.html', {'posts': posts})


def my_post_details(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(fac_id=request.user.fac_id)
    return render(request, 'mypostdetail.html', {'posts': posts})




class UpdatePostView(UpdateView):
    model = Post
    fields = ['post_title', 'post_snap', 'post_details', 'post_category']
    template_name = 'postupdate.html'
    success_url = reverse_lazy('mypost_details')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'postdelete.html'
    success_url = reverse_lazy('mypost_details')




class eventcreate(CreateView):
    model=Event
    fields = ['event_Name','event_Location','event_details','event_Date']
    template_name='eventcreate.html'
    success_url=reverse_lazy('event-details')

    def form_valid(self, form):
        fac = Faculty.objects.get(username=self.request.user)
        form.instance.fac_id = fac
        return super().form_valid(form)


def event_details(request):
    if request.user.is_authenticated:
        events = Event.objects.all()
        return render(request, 'eventdetail.html', {'events': events})

def my_event_details(request):
    if request.user.is_authenticated:
        events = Event.objects.filter(fac_id=request.user.fac_id)
    return render(request, 'myeventdetail.html', {'events': events})

def before_login_event_details(request):
        events = Event.objects.all()
        return render(request, 'beforelogineventdetail.html', {'events': events})


class UpdateEventView(UpdateView):
    model = Event
    fields = ['event_Name','event_Location','event_details','event_Date']
    template_name = 'eventupdate.html'
    success_url = reverse_lazy('myevent_details')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'eventdelete.html'
    success_url = reverse_lazy('myevent_details')

