from django.db import models
from core import models as core_models


class Challenge(core_models.TimeStampedModel):
    """ Challenge Model Definition """
    STATUS_BEFORE = "before"
    STATUS_START = "start"
    STATUS_FINISH = "finish"

    STATUS_CHOICES = (
        (STATUS_BEFORE, "모집중"),
        (STATUS_START, "도전시작"),
        (STATUS_FINISH, "도전종료")
    )

    ROUTINE_EVERYDAY = "everyday"
    ROUTINE_WEEKENDONLY = "weekend_only"
    ROUTINE_FIVETIMES = "5times_a_week"
    ROUTINE_THREETIMES = "3times_a_week"
    ROUTINE_TWICE = "twice_a_week"
    ROUTINE_ONCE = "once_a_week"

    ROUTINE_CHOICES = (
        (ROUTINE_EVERYDAY, "매일"),
        (ROUTINE_WEEKENDONLY, "주말만"),
        (ROUTINE_FIVETIMES, "월화수목금"),
        (ROUTINE_THREETIMES, "주3회"),
        (ROUTINE_TWICE, "주2회"),
        (ROUTINE_ONCE, "주1회")
    )

    subject = models.CharField(max_length=140)
    description = models.TextField()
    status = models.CharField(
        max_length=8, choices=STATUS_CHOICES, default=STATUS_BEFORE)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    routine = models.CharField(
        max_length=15, choices=ROUTINE_CHOICES, default=ROUTINE_EVERYDAY)
    num_of_auth_per_day = models.IntegerField(default=1)
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()
    created = models.DateField()
    modified = models.DateField()

    def __str__(self):
        return f'{self.subject} - {self.status}'


class Photo(core_models.TimeStampedModel):
    """Photo Model Definition"""
    caption = models.CharField(max_length=150)
    file = models.ImageField(upload_to="challenge_photo")
    challenger = models.ForeignKey("users.User", on_delete=models.CASCADE)
    challenge = models.ForeignKey(
        "Challenge", related_name="selfauth", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
