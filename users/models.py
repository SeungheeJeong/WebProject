from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    COURSE_BIGDATA = "bigdata"
    COURSE_AI = "ai"
    COURSE_CLOUD = "cloud"
    COURSE_IOT = "iot"
    COURSE_CHOICES = (
        (COURSE_BIGDATA, "BIGDATA"),
        (COURSE_AI, "AI"),
        (COURSE_CLOUD, "CLOUD"),
        (COURSE_IOT, "IOT")
    )
    birthdate = models.DateField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    takencourse = models.CharField(
        choices=COURSE_CHOICES, max_length=20, null=True, blank=True)
    hp = models.CharField(max_length=11, null=True, blank=True)
