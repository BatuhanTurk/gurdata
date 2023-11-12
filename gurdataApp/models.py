from django.db import models

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

    class Meta:
        db_table = 'user_gurdata'

    def __str__(self):
        return f"{self.user_name} {self.user_surname} {self.user_id}"
    
class DataGurdata(models.Model):
    data_id = models.AutoField(primary_key=True)
    data_name = models.CharField(max_length=40)
    data_path = models.CharField(max_length=100)
    data_demo_path = models.CharField(max_length=100)
    data_download_count = models.IntegerField()

    class Meta:
        db_table = 'data_gurdata'

    def __str__(self):
        return self.data_name
    

class DataDownloadGurdata(models.Model):
    download_id = models.AutoField(primary_key=True)
    data_id = models.ForeignKey(DataGurdata, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserGurdata, on_delete=models.CASCADE)
    download_datatime = models.DateTimeField()
    download_time_minute = models.IntegerField()

    class Meta:
        db_table = 'data_download_gurdata'

    def __str__(self):
        return f"{self.user_id} downloaded {self.data_id} at {self.download_datatime}"
