from django.shortcuts import render,redirect
from .forms import LoginForm,RegistrationForm
from .models import UserGurdata
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, '0_index.html')

def authenticate_user(email, password):
    try:
        user = UserGurdata.objects.get(user_email=email)
    except UserGurdata.DoesNotExist:
        user = None

    if user is not None and user.user_password == password:
        return user
    else:
        return None

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            remember_me = request.POST['remember_me']

            user = authenticate_user(email=email, password=password)
            if user is not None:
                request.session["user_id"] = user.user_id
                return redirect('home')
            else:
                # Kullanıcı doğrulanamadı, hata mesajı ekle
                print("Geçersiz e-posta veya şifre.")
                form.add_error(None, "Geçersiz e-posta veya şifre.")
        else:
            # Form geçerli değilse, hataları göster
            print(form.errors)
    else:
        form = LoginForm()

    return render(request, '0_login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            company = request.POST['company']
            position = request.POST['position']

            user = UserGurdata.objects.create(
                user_name=first_name,
                user_surname=last_name,
                user_email=email,
                user_company=company,
                user_company_role=position,
                user_password=password,
                user_balance=0,
                user_confirmed=0,  
                user_deleted=0,  
            )

            return redirect('home')  

    else:
        form = RegistrationForm()

    return render(request, '0_register.html', {'form': form})