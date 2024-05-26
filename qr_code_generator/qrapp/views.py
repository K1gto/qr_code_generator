import qrcode
from io import BytesIO
from django.shortcuts import render, redirect
from .forms import QRCodeForm
from .models import QRCode
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home(request):
    qr_code_img = None
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            qr_code = form.save(commit=False)
            if request.user.is_authenticated:
                qr_code.user = request.user
            qr_code.save()

            img = qrcode.make(qr_code.link)
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            qr_code.qr_code_image.save(f'qr_{qr_code.id}.png', buffer, save=False)
            qr_code.save()

            qr_code_img = qr_code.qr_code_image.url
    else:
        form = QRCodeForm()
    return render(request, 'home.html', {'form': form, 'qr_code_img': qr_code_img})

@login_required
def history(request):
    qr_codes = QRCode.objects.filter(user=request.user)
    return render(request, 'history.html', {'qr_codes': qr_codes})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


