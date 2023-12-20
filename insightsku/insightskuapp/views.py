from django.shortcuts import render, redirect
from .forms import ClientNameForm
from .models import Client, UserProfile, Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages




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

    # Check if the user was redirected to login while trying to access the dashboard
    next_url = request.GET.get('next')
    if next_url == '/products/':
        messages.info(request, 'Please log in to access the dashboard.')

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
                        return redirect('products')
                except UserProfile.DoesNotExist:
                    form.add_error(None, "Invalid username, password, or client.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form, 'client_name': client_name})


@login_required
def user_dashboard(request):
    # Display user-specific dashboard
    user_profile = UserProfile.objects.get(user=request.user)
    client = user_profile.client  # Replace with your method of getting the client
    products = Product.objects.filter(client=client)
    context = {'products': products}
    return render(request, 'products.html', context)


def custom_logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('/')


def product_search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(title__icontains=query)  # Adjust the filter as needed
    return render(request, 'dashboard.html', {'products': products})

def advanced_product_search(request):
    # Add your advanced search logic here
    return render(request, 'advanced_search.html')