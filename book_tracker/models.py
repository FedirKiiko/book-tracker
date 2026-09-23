from django.contrib.auth.models import AbstractUser
from django.db import models


class Reader(AbstractUser):
    birth_date = models.DateField(null=True)
    avatar = models.ImageField(
        upload_to="avatars/", null=True, blank=True, default="avatars/default.jpg"
    )
