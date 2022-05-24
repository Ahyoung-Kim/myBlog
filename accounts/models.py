from django.db import models

# Create your models here.


class Login(models.Model):
    userid = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.userid
