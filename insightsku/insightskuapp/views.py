from django.shortcuts import render, redirect
from .forms import ClientNameForm
from .models import Client, UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def enter_client_name(request):
    if request.method == 'POST':
        form = ClientNameForm(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data['client_name']
            if Client.objects.filter(client_name=client_name).exists():
                request.session['client_name'] = client_name
                return redirect('user_login')
            else:
                # Handle case where client does not exist
                pass
    else:
        form = ClientNameForm()

    return render(request, 'enter_client_name.html', {'form': form})




def user_login(request):
    client_name = request.session.get('client_name')

    if not client_name or not Client.objects.filter(client_name=client_name).exists():
        return redirect('enter_client_name')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                try:
                    profile = UserProfile.objects.get(user=user)
                    if profile.client.client_name == client_name:
                        login(request, user)
                        return redirect('dashboard')
                except UserProfile.DoesNotExist:
                    form.add_error(None, "Invalid username, password, or client.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})





from django.contrib.auth.decorators import login_required

@login_required
def user_dashboard(request):
    # Display user-specific dashboard
    pass

