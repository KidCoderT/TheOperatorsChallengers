import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Score(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    corrects = models.PositiveIntegerField(default=0)
    wrongs = models.PositiveIntegerField(default=0)
    score = models.PositiveIntegerField(default=0)
    count = models.PositiveIntegerField(default=0)
    time_taken = models.TimeField(auto_now_add=False, default=datetime.time, null=True)
    on_which_date = models.DateField(auto_now_add=True, null=True)

    LABEL_DATA = {
        ("T", "todays"),
        ("Y", "yesterday"),
        ("N", "Not needed But usefull information")
    }
    label = models.CharField(null=True, blank=True, max_length=1, default="T", choices=LABEL_DATA)

    def set_label(self):
        if self.on_which_date == datetime.date.today():
            label = "T"
        elif self.on_which_date == (datetime.date.today() - datetime.timedelta(days = 1)):
            label = "Y"
        elif self.on_which_date < (datetime.date.today() - datetime.timedelta(days = 1)) and self.on_which_date > (datetime.date.today() - datetime.timedelta(days = 31)):
            label = "N"
        else:
            self.delete()
            return
        self.save()

    def __str__(self):
        return f'On {self.on_which_date.strftime("%d/%m/%Y")} The user: {self.user} had a total score of {self.score} by doing MA for {self.time_taken.strftime("%H hours %M minutes and %S seconds")}.'
