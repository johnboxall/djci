from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.core.urlresolvers import reverse

from .forms import SignupForm

def home(request, template_name='home.html'):
    return render(request, template_name)

def signup(request, template_name='signup.html'):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            next = reverse('home')
            return HttpResponseRedirect(next)
    else:
        form = SignupForm()

    context = {'form': form}

    assert False


    return render(request, template_name, context)




