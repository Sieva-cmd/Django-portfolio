from django.shortcuts import render
from .models import Profile, Projects

# Create your views here.
def home(request):
    profile =Profile.objects.all()
    project =Projects.objects.all()

    projects =Projects.filter_projects_by_id(project)
    profiles =Profile.filter_profile_by_id(profile)

    return render(request,'main/home.html',{'projects':projects,'profiles':profiles})
def profile(request):
    profile =Profile.objects.all()
    profiles =Profile.filter_profile_by_id(profile)
    return render(request,'main/profile.html',{"profiles":profiles})