from django.shortcuts import render
from .models import Conference, Faculty,Journal
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import RegistrationForm
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView


def home(request):
    return render (request,'home.html')



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.role == "HOD":
                return redirect('hodhomeafterlogin')
            elif user.role == "OTHER":
                return redirect('otherhomeafterlogin')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})




def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('login')                      # redirect user to login page after registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})



def other_home_after_login(request):
    return render(request,'otherhomeafterlogin.html')
    

def hod_home_after_login(request):
    return render (request,'hodhomeafterlogin.html')


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


 
