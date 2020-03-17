from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
import random


def random_int():
    random_number = random.randint(1, 100)
    return random_number


class MyUser(AbstractUser):
    birthday_date = models.DateField()
    random_number_field = models.IntegerField(default=random_int)

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})
