from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from .models import UserGurdata
from django.contrib.auth import authenticate, login

import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
    return render(request, "0_index.html", {"user_data": user_data})


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


def confirm_email(request):
    
    if request.method == "POST":
        codes = request.POST.getlist('code[]')  
        input_code = ""
        for code in codes:
            input_code += str(code)
        
        if int(request.session.get("random_code")) == int(input_code):
            user = UserGurdata.objects.get(user_email=request.session.get("email"))
            user.user_confirmed = 1
            user.save()

            return redirect("home")
        else:
            return render(request, "0_confirm_email.html")
    else:
        request.session["random_code"] = random.randint(1000, 9999)
        mail_from = "Ekrem Gurdal <ekremgurdal@gmail.com>"
        mail_to = "Ekrem Gurdal <{}>".format(request.session.get('email'))

        msg = MIMEMultipart()
        msg["From"] = mail_from
        msg["To"] = mail_to
        msg["Subject"] = "Sending mails with Python"
        mail_body = """
        Hey,

        This is a test.
        {}
        Regards,\nRuan

        """.format(request.session.get("random_code"))
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
        return render(request, "0_confirm_email.html")
        


    
