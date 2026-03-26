import uuid
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"

class Appointment(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    date = models.DateField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name



from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')

    def __str__(self):
        return f"{self.user.username}'s Profile"

class PaymentMethod(models.Model):
    PAYMENT_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    cvv = models.CharField(max_length=4, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=20, blank=True, null=True)
    paypal_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Payment Method"
