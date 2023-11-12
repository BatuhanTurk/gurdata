from django.shortcuts import render, redirect,get_object_or_404
from .forms import LoginForm, RegistrationForm,contactForm,UserProfileForm
from .models import UserGurdata,ContactGurdata
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.core.signing import dumps, loads
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.auth.views import PasswordResetConfirmView


def get_user_data_by_id(user_id):
    user_data = UserGurdata.objects.filter(user_id=user_id)
    return user_data


def logout(request):
    request.session["user_id"] = None
    return render(request, "0_index.html")


def home(request):
    user_data = get_user_data_by_id(request.session.get("user_id"))
    try:
        user_data = user_data[0]
    except:
        user_data = None
    form = contactForm(request.POST)
    if request.method == "POST":
        email = request.POST["email"]
        name = request.POST["name"]
        
        ContactGurdata.objects.create(
            name = name, email = email,
        )

        return redirect("home")
    else:
        return render(request, "0_index.html", {"user_data": user_data,"form": form})


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
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            remember_me = request.POST["remember_me"]

            user = authenticate_user(email=email, password=password)
            if user is not None:
                request.session["user_id"] = user.user_id
                return redirect("home")
            else:
                alert = "Email ve şifre eşleşmiyor."
                return render(request, "0_login.html", {"form": form, "alert": alert})

        else:
            print(form.errors)
    else:
        form = LoginForm()

    return render(request, "0_login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            password = request.POST["password"]
            confirm_password = request.POST["confirm_password"]
            company = request.POST["company"]
            position = request.POST["position"]

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
            request.method = "GET"
            request.session["email"] = email
            return confirm_email(request)

    else:
        form = RegistrationForm()

    return render(request, "0_register.html", {"form": form})

def send_email(email,subject, content):
    mail_from = "Ekrem Gurdal <ekremgurdal@gmail.com>"
    mail_to = f"Ekrem Gurdal <{email}>"

    msg = MIMEMultipart()
    msg["From"] = mail_from
    msg["To"] = mail_to
    msg["Subject"] = subject
    mail_body = content
    msg.attach(MIMEText(mail_body))

    try:
        server = smtplib.SMTP_SSL("smtp.sendgrid.net", 465)
        server.ehlo()
        server.login(
            "apikey",
            "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",
        )
        server.sendmail(mail_from, mail_to, msg.as_string())
        server.close()
        print("mail sent")
    except:
        print("issue")


def confirm_email(request):
    if request.method == "POST":
        codes = request.POST.getlist("code[]")
        input_code = "".join(map(str, codes))

        if int(request.session.get("random_code")) == int(input_code):
            user = UserGurdata.objects.get(user_email=request.session.get("email"))
            user.user_confirmed = 1
            user.save()
            request.session["random_code"] = None
            return redirect("home")
        else:
            return render(request, "0_confirm_email.html")
    else:
        request.session["random_code"] = random.randint(1000, 9999)
        subject = "Account confirmation"
        content = f"""
            Hello,

            Thank you for signing up with Gurdata! To complete your registration, please enter the following code on the confirmation page:

            {request.session["random_code"]}

            If you did not sign up for Gurdata, please ignore this email.

            Best regards,
            Gurdata Team
        """
        
        send_email(request.session.get("email"),subject,content)
        return render(request, "0_confirm_email.html")

def forgot_password(request):
    
    if request.method == "POST":
        email = request.POST.getlist("email")[0]
        user = UserGurdata.objects.get(user_email=email)
        
        user_id = user.user_id
        if user:
            user_data = {'user': str(user), 'email': str(email)}
            token = dumps(user_data)
            reset_link = reverse('reset_password', kwargs={'uidb64': user_id, 'token': token})
            subject = "Password Reset"
            content = f"""
                Hello,

                To reset your Gurdata password, please use the following link:

                {reset_link}

                Please note that this link is valid for a single use only. If you did not request a password reset, you can safely ignore this email.

                Best regards,
                Gurdata Team
            """
            send_email(email,subject,content)
            return redirect('home')
        else:
            return render(request,"0_forgot_pass.html")
    else:
        return render(request,"0_forgot_pass.html")
    
    
def reset_password(request,uidb64, token):
    user = UserGurdata.objects.get(pk=uidb64)
    
    if request.method == "POST":
        passwords = request.POST.getlist("password")
        if all(password == passwords[0] for password in passwords):
            user.user_password = passwords[0]
            user.save()
        return render(request,"0_success_new_pass.html")
    else:
        return render(request,"0_new_password.html",{"uidb64":uidb64,"token":token})

def account(request):
    user_id = request.session["user_id"]
    user = UserGurdata.objects.get(user_id=user_id)
    form = UserProfileForm(request.POST, user=user)
    
    if request.method == "POST":
        user_name = request.POST["user_name"]
        user_surname = request.POST["user_surname"]
        user_email = request.POST["user_email"]
        new_password = request.POST["new_password"]
        old_password = request.POST["old_password"]
        user_company = request.POST["user_company"]
        user_position = request.POST["user_position"]

        if new_password == old_password:
            user.user_name = user_name
            user.user_surname = user_surname
            user.user_email = user_email
            user.user_password = new_password
            user.user_company = user_company
            user.user_company_role = user_position
            user.save()
        else:
            print("hata")

        return redirect("account")
    else:
        return render(request,"_account.html",{"form":form,"user":user})