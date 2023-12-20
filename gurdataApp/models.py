from django.db import models
from django.utils import timezone

class UserGurdata(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    user_surname = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=40, unique=True)
    user_company = models.CharField(max_length=30)
    user_company_role = models.CharField(max_length=30)
    user_password = models.CharField(max_length=200)
    user_balance = models.IntegerField()
    user_confirmed = models.IntegerField()
    user_deleted = models.IntegerField()
    system_notifications = models.IntegerField(default=1)
    file_manager_notifications = models.IntegerField(default=0)
    mail_notifications = models.IntegerField(default=0)

    class Meta:
        db_table = "user_gurdata"

    def __str__(self):
        return f"{self.user_name} {self.user_surname}"


class DataCategoryGurdata(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    category_description = models.TextField()
    category_image = models.ImageField(upload_to="category_images/")

    def __str__(self):
        return self.category_name


class DataGurdata(models.Model):
    data_id = models.AutoField(primary_key=True)
    category_id= models.ForeignKey('DataCategoryGurdata', on_delete=models.CASCADE,default = 1)
    data_name = models.CharField(max_length=40)
    data_description = models.TextField(null=True)
    data_path = models.CharField(max_length=100)
    data_demo_path = models.CharField(max_length=100)
    data_download_count = models.IntegerField()
    data_price = models.DecimalField(max_digits=10, decimal_places=2,default = 0)
    data_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "data_gurdata"

    def __str__(self):
        return self.data_name


class DataDownloadGurdata(models.Model):
    download_id = models.AutoField(primary_key=True)
    data_id = models.ForeignKey(DataGurdata, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserGurdata, on_delete=models.CASCADE)
    download_datatime = models.DateTimeField()
    download_time_minute = models.IntegerField()
    data_active = models.IntegerField(default=0)

    class Meta:
        db_table = "data_download_gurdata"

    def __str__(self):
        return f"{self.user_id} downloaded {self.data_id} at {self.download_datatime}"


class ContactGurdata(models.Model):
    contact_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "contact_gurdata"

    def __str__(self):
        return f"{self.email}"


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} {self.surname} - {self.subject}"
