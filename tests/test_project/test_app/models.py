from django.db import models

import datetime

class FirstObject(models.Model):
    name = models.IntegerField(null=False)


class SecondObject(models.Model):
    big_int = models.BigIntegerField(null=True)
    binary = models.BinaryField(null=True)
    boolean = models.BooleanField(default=False)
    characters = models.CharField(max_length=512, null=True)
    current_date = models.DateField(default=datetime.date(2018, 1, 21))
