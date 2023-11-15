from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="E-Posta Adresiniz",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Şifreniz",
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    remember_me = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label="Adınız",
        max_length=30,
        widget=forms.TextInput(attrs={"class": "form-control w-100"}),
        required=True,
    )
    last_name = forms.CharField(
        label="Soyadınız",
        max_length=30,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )
    email = forms.EmailField(
        label="E-Posta Adresiniz",
        max_length=40,
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        required=True,
    )
    password = forms.CharField(
        label="Şifreniz",
        min_length=8,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=True,
    )
    confirm_password = forms.CharField(
        label="Şifrenizi Onaylayın",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=True,
    )
    company = forms.CharField(
        label="Şirketiniz",
        max_length=30,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False,
    )
    position = forms.CharField(
        label="Pozisyonunuz",
        max_length=30,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False,
    )


class contactForm(forms.Form):
    email = forms.EmailField(
        label="E-Posta Adresiniz",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "E-Posta Adresiniz"}
        ),
    )
    name = forms.CharField(
        label="Ad Soyad",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Adınız"}
        ),
    )


class UserProfileForm(forms.Form):
    user_name = forms.CharField(
        label="Adınız",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": ""}),
    )
    user_surname = forms.CharField(
        label="Soyadınız",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": ""}),
    )
    user_email = forms.EmailField(
        label="E-Posta Adresiniz",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": ""}),
    )
    old_password = forms.CharField(
        label="Eski Şifreniz",
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "new-password",
                "aria-autocomplete": "none",
                "placeholder": "",
            }
        ),
    )
    new_password = forms.CharField(
        label="Şifreniz",
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "new-password",
                "aria-autocomplete": "none",
                "placeholder": "",
            }
        ),
    )
    confirm_password = forms.CharField(
        label="Şifrenizi Onaylayın",
        required=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "new-password",
                "aria-autocomplete": "none",
                "placeholder": "",
            }
        ),
    )
    user_company = forms.CharField(
        label="Şirket İsminiz",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": ""}),
    )
    user_position = forms.CharField(
        label="Şirketiniz",
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": ""}),
    )
    system_notifications = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "custom-switch-input"}),
        required=False,
    )
    file_manager_notifications = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "custom-switch-input"}),
        required=False,
    )
    mail_notifications = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "custom-switch-input"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(UserProfileForm, self).__init__(*args, **kwargs)

        self.fields["user_name"].widget.attrs["value"] = user.user_name
        self.fields["user_surname"].widget.attrs["value"] = user.user_surname
        self.fields["user_email"].widget.attrs["value"] = user.user_email
        self.fields["user_company"].widget.attrs["value"] = user.user_company
        self.fields["user_position"].widget.attrs["value"] = user.user_company_role
        if user.system_notifications == 1:
            self.fields["system_notifications"].widget.attrs["checked"] = True
        else:
            self.fields["system_notifications"].widget.attrs["checked"] = False
        if user.file_manager_notifications == 1:
            self.fields["file_manager_notifications"].widget.attrs["checked"] = True
        else:
            self.fields["file_manager_notifications"].widget.attrs["checked"] = False
        if user.mail_notifications == 1:
            self.fields["mail_notifications"].widget.attrs["checked"] = True
        else:
            self.fields["mail_notifications"].widget.attrs["checked"] = False


class ContactForm1(forms.Form):
    name = forms.CharField(
        label="Adınız",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "autocomplete": "off",
                "aria-autocomplete": "none",
            }
        ),
    )
    surname = forms.CharField(
        label="Soyadınız",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "autocomplete": "off",
                "aria-autocomplete": "none",
            }
        ),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "autocomplete": "off",
                "aria-autocomplete": "none",
            }
        ),
    )
    position = forms.CharField(
        label="Position",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "autocomplete": "off",
                "aria-autocomplete": "none",
            }
        ),
    )
    company = forms.CharField(
        label="Company",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "autocomplete": "off",
                "aria-autocomplete": "none",
            }
        ),
    )


class ContactForm2(forms.Form):
    subject = forms.CharField(
        label="subject",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "autocomplete": "off",
                "aria-autocomplete": "none",
            }
        ),
    )
    message = forms.CharField(
        label='Mesajınız',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            "id":"exampleInputname2",
            'aria-autocomplete': 'none',
        })
    )
