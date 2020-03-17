from django.contrib.auth.models import AbstractUser
from django.db import models
import random


class MyUser(AbstractUser):
    birthday_date = models.DateField()
    random_number = random.randint(1, 100)
    random_number_field = models.IntegerField(default=random_number)

