from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def user_profile(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    context = {
        "user": user,
        "user_profile": user_profile,
        'firstname': user_profile.user.first_name,  # Access first name through the related User model
        "lastname": user_profile.user.last_name,  # Access last name through the related User model
    }
    return render(request, 'myapp/user_profiles.html', context)