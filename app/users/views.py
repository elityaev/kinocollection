from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic


def register(request):
    if request.method == 'GET':
        return render(request, 'users/signup.html', {'form': UserCreationForm})

    if request.method == 'POST':
        query_id = request.get_full_path().split('/')[-2]
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            if request.path != request.get_full_path():
                return redirect('selections:query', query_id)
            return redirect('selections:random_tile')