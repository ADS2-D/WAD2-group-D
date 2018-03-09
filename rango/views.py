from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def home(request):
    response = render(request, 'wwworkout/index.html')
    return response


def about(request):
    return render(request, 'wwworkout/about.html')


def user_redirect(request):
    # TODO: redirect to user's profile at /user/<username>
    if request.user.is_authenticated():
        username = request.user.username
        # redirect here
    else:
        return HttpResponseRedirect(reverse('home'))


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(usename=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                # TODO: redirect user to their own profile
                return HttpResponseRedirect(reverse('user_redirect'))


def user_profile():
    context_dict = None
    return render(request, 'wwworkout/user_profile.html', context_dict)


def user_timeline():
    context_dict = None
    return render(request, 'wwworkout/user_timeline.html', context_dict)
