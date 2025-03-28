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
    user_data = models.ManyToManyField("DataGurdata", related_name="users", blank=True)

    class Meta:
        db_table = "user_gurdata"

    def __str__(self):
        return f"{self.user_name} {self.user_surname}"


class DataCategoryGurdata(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    category_description = models.TextField()
    category_image = models.ImageField(upload_to="./gurdataApp/static/category_images")
    svg_chocies = [
        (
            "M10.3125 1.375C5.38721 1.375 1.375 5.38721 1.375 10.3125C1.375 15.2378 5.38721 19.25 10.3125 19.25C15.2378 19.25 19.25 15.2378 19.25 10.3125C19.25 5.38721 15.2378 1.375 10.3125 1.375ZM9.625 2.78223V10.5972L15.1519 16.124C13.8413 17.2144 12.1548 17.875 10.3125 17.875C6.12842 17.875 2.75 14.4966 2.75 10.3125C2.75 6.35938 5.76318 3.13135 9.625 2.78223ZM11 2.78223C14.6309 3.10986 17.5151 5.99414 17.8374 9.625H11V2.78223ZM11.9722 11H17.8374C17.6978 12.5737 17.0801 14.0078 16.124 15.1519L11.9722 11Z",
            "Demografi",
        ),
        (
            "M6.93945 4.125C6.23671 4.125 5.5804 4.48531 5.2019 5.07568L2.92993 8.46216C1.31329 8.74016 0 9.99468 0 11.6875V13.0625C0 14.1937 0.925302 15.1275 2.05713 15.1357L2.75269 15.1411C2.76172 16.6442 3.9949 17.875 5.5 17.875C7.01064 17.875 8.25 16.6356 8.25 15.125H13.75C13.75 16.6356 14.9894 17.875 16.5 17.875C18.0106 17.875 19.25 16.6356 19.25 15.125H20.625C21.3765 15.125 22 14.5015 22 13.75V11.8674C22 10.6425 21.1819 9.56121 20.0046 9.22485L16.8921 8.33594L14.2092 5.11597C13.6872 4.48956 12.9142 4.125 12.0984 4.125H6.93945ZM6.93945 5.5H8.25V8.25H4.72656L6.35669 5.82227L6.35938 5.81689C6.48688 5.61802 6.70445 5.5 6.93945 5.5ZM9.625 5.5H12.0984C12.5063 5.5 12.8921 5.68004 13.1538 5.99414L15.0337 8.25H9.625V5.5ZM3.4375 9.625H3.60938H3.80273H16.4087L19.6287 10.5461C20.2224 10.7158 20.625 11.2499 20.625 11.8674V13.75H18.8633C18.3845 12.9339 17.5081 12.375 16.5 12.375C15.4919 12.375 14.6155 12.9339 14.1367 13.75H7.86328C7.38449 12.9339 6.50808 12.375 5.5 12.375C4.48424 12.375 3.60212 12.9424 3.12598 13.7688L2.06787 13.7607C1.6872 13.758 1.375 13.4438 1.375 13.0625V11.6875C1.375 10.5394 2.28935 9.625 3.4375 9.625ZM5.5 13.75C6.26753 13.75 6.875 14.3575 6.875 15.125C6.875 15.8925 6.26753 16.5 5.5 16.5C4.73247 16.5 4.125 15.8925 4.125 15.125C4.125 14.3575 4.73247 13.75 5.5 13.75ZM16.5 13.75C17.2675 13.75 17.875 14.3575 17.875 15.125C17.875 15.8925 17.2675 16.5 16.5 16.5C15.7325 16.5 15.125 15.8925 15.125 15.125C15.125 14.3575 15.7325 13.75 16.5 13.75Z",
            "Araç",
        ),
        (
            "M9.625 1.375C8.87305 1.375 8.25 1.99805 8.25 2.75V4.125H3.4375C2.3042 4.125 1.375 5.0542 1.375 6.1875V15.8125C1.375 16.9458 2.3042 17.875 3.4375 17.875H18.5625C19.6958 17.875 20.625 16.9458 20.625 15.8125V6.1875C20.625 5.0542 19.6958 4.125 18.5625 4.125H13.75V2.75C13.75 1.99805 13.127 1.375 12.375 1.375H9.625ZM9.625 2.75H12.375V4.125H9.625V2.75ZM3.4375 5.5H5.5V15.125H6.875V5.5H15.125V15.125H16.5V5.5H18.5625C18.9492 5.5 19.25 5.80078 19.25 6.1875V15.8125C19.25 16.1992 18.9492 16.5 18.5625 16.5H3.4375C3.05078 16.5 2.75 16.1992 2.75 15.8125V6.1875C2.75 5.80078 3.05078 5.5 3.4375 5.5Z",
            "Finans",
        ),
        (
            "M7.5625 1.375C6.43152 1.375 5.5 2.30652 5.5 3.4375V18.5625C5.5 19.6935 6.43152 20.625 7.5625 20.625H14.4375C15.5685 20.625 16.5 19.6935 16.5 18.5625V3.4375C16.5 2.30652 15.5685 1.375 14.4375 1.375H7.5625ZM7.5625 2.75H14.4375C14.8245 2.75 15.125 3.05048 15.125 3.4375V18.5625C15.125 18.9495 14.8245 19.25 14.4375 19.25H7.5625C7.17548 19.25 6.875 18.9495 6.875 18.5625V3.4375C6.875 3.05048 7.17548 2.75 7.5625 2.75ZM11 4.125C10.6353 4.125 10.2856 4.26987 10.0277 4.52773C9.76987 4.78559 9.625 5.13533 9.625 5.5C9.625 5.86467 9.76987 6.21441 10.0277 6.47227C10.2856 6.73013 10.6353 6.875 11 6.875C11.3647 6.875 11.7144 6.73013 11.9723 6.47227C12.2301 6.21441 12.375 5.86467 12.375 5.5C12.375 5.13533 12.2301 4.78559 11.9723 4.52773C11.7144 4.26987 11.3647 4.125 11 4.125ZM11 9.625C10.6353 9.625 10.2856 9.76987 10.0277 10.0277C9.76987 10.2856 9.625 10.6353 9.625 11C9.625 11.3647 9.76987 11.7144 10.0277 11.9723C10.2856 12.2301 10.6353 12.375 11 12.375C11.3647 12.375 11.7144 12.2301 11.9723 11.9723C12.2301 11.7144 12.375 11.3647 12.375 11C12.375 10.6353 12.2301 10.2856 11.9723 10.0277C11.7144 9.76987 11.3647 9.625 11 9.625ZM11 15.125C10.6353 15.125 10.2856 15.2699 10.0277 15.5277C9.76987 15.7856 9.625 16.1353 9.625 16.5C9.625 16.8647 9.76987 17.2144 10.0277 17.4723C10.2856 17.7301 10.6353 17.875 11 17.875C11.3647 17.875 11.7144 17.7301 11.9723 17.4723C12.2301 17.2144 12.375 16.8647 12.375 16.5C12.375 16.1353 12.2301 15.7856 11.9723 15.5277C11.7144 15.2699 11.3647 15.125 11 15.125Z",
            "Trafik",
        ),
        (
            "M11 2.75C8.48096 2.75 6.28955 4.50098 5.68262 6.90723C4.2002 7.12744 3.02393 8.30908 2.79297 9.84521C1.14941 10.4038 0 11.9722 0 13.75C0 16.022 1.85303 17.875 4.125 17.875H8.25V16.5H4.125C2.61035 16.5 1.375 15.2646 1.375 13.75C1.375 12.4448 2.3042 11.3115 3.57715 11.0537L4.14111 10.8926L4.125 10.3125C4.125 9.17383 5.04883 8.25 6.11768 8.24463L6.85352 8.26074L6.93945 7.66455C7.22412 5.64502 8.96973 4.125 11 4.125C12.6597 4.125 14.1528 5.11328 14.8027 6.63867L15.0444 7.22949L15.646 7.02539C15.9575 6.92334 16.2368 6.875 16.5 6.875C18.0146 6.875 19.25 8.11035 19.25 9.625C19.25 9.94727 19.1855 10.2749 19.0566 10.6025L18.8633 11.1289L19.3359 11.4297C20.1416 11.9399 20.625 12.8047 20.625 13.75C20.625 15.0552 19.7065 16.1509 18.4819 16.4302C18.7773 16.79 18.9922 17.2036 19.1157 17.6602C20.7808 17.1338 22 15.5923 22 13.75C22 12.5146 21.4522 11.3599 20.5068 10.5811C20.5874 10.2642 20.625 9.9419 20.625 9.625C20.625 7.12207 18.4121 5.08106 15.8018 5.56445C14.835 3.84033 13.0142 2.75 11 2.75ZM13.0625 11C12.1655 11 11.4082 11.5747 11.1289 12.375H13.0625C13.4438 12.375 13.75 12.6812 13.75 13.0625C13.75 13.4438 13.4438 13.75 13.0625 13.75H6.875V15.125H13.0625C14.2012 15.125 15.125 14.2012 15.125 13.0625C15.125 11.9238 14.2012 11 13.0625 11ZM9.625 16.5V17.875H15.8125C16.1938 17.875 16.5 18.1812 16.5 18.5625C16.5 18.9438 16.1938 19.25 15.8125 19.25H13.8789C14.1582 20.0503 14.9155 20.625 15.8125 20.625C16.9512 20.625 17.875 19.7012 17.875 18.5625C17.875 17.4238 16.9512 16.5 15.8125 16.5H9.625Z",
            "Hava",
        ),
        (
            "M10,1.375c-3.17,0-5.75,2.548-5.75,5.682c0,6.685,5.259,11.276,5.483,11.469c0.152,0.132,0.382,0.132,0.534,0c0.224-0.193,5.481-4.784,5.483-11.469C15.75,3.923,13.171,1.375,10,1.375 M10,17.653c-1.064-1.024-4.929-5.127-4.929-10.596c0-2.68,2.212-4.861,4.929-4.861s4.929,2.181,4.929,4.861C14.927,12.518,11.063,16.627,10,17.653 M10,3.839c-1.815,0-3.286,1.47-3.286,3.286s1.47,3.286,3.286,3.286s3.286-1.47,3.286-3.286S11.815,3.839,10,3.839 M10,9.589c-1.359,0-2.464-1.105-2.464-2.464S8.641,4.661,10,4.661s2.464,1.105,2.464,2.464S11.359,9.589,10,9.589",
            "konum",
        ),
    ]

    category_svg = models.CharField(max_length=2000, choices=svg_chocies, default="1")

    def __str__(self):
        return self.category_name


class DataGurdata(models.Model):
    data_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(
        "DataCategoryGurdata", on_delete=models.CASCADE, default=1
    )
    data_name = models.CharField(max_length=40)
    data_description = models.TextField(null=True)
    data_path = models.CharField(max_length=100)
    data_demo_path = models.CharField(max_length=100)
    data_download_count = models.IntegerField()
    data_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_time = models.DateTimeField(default=timezone.now)
    data_time_minute = models.IntegerField(default = 5000)

    class Meta:
        db_table = "data_gurdata"

    def __str__(self):
        return self.data_name


class DataDownloadGurdata(models.Model):
    download_id = models.AutoField(primary_key=True)
    data_id = models.ForeignKey(DataGurdata, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserGurdata, on_delete=models.CASCADE)
    download_datatime = models.DateTimeField()
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
