from django.db import models

import datetime


class FirstObject(models.Model):
    name = models.IntegerField(null=False)


class SecondObject(models.Model):
    big_int = models.BigIntegerField(null=True)
    binary = models.BinaryField(null=True)
    boolean = models.BooleanField(default=False)
    characters = models.CharField(max_length=512, null=True)
    current_date = models.DateField(default=datetime.date(2018, 1, 21), unique_for_date=False)
    datetime_f = models.DateTimeField(null=True)
    dec = models.DecimalField(max_digits=30, decimal_places=20, null=True)
    elapsed = models.DurationField(null=True)
    mail = models.EmailField(null=False, default='test@example.com', db_column='email_address')
    attachments = models.FileField(null=True)
    filepath = models.FilePathField(null=True, unique=False)
    floating = models.FloatField(default=0.)
    generic_ip = models.GenericIPAddressField(null=True)
    null_bool = models.NullBooleanField()
    positive_int = models.PositiveIntegerField(default=0)
    small_pos_int = models.PositiveSmallIntegerField(default=1234)
    slug = models.SlugField(null=True)
    small_int = models.SmallIntegerField(default=-54)
    texty = models.TextField(null=True)
    time = models.TimeField(default=datetime.time(18, 7))
    url = models.URLField(null=True)
    uuid = models.UUIDField(null=True)
    floating_second = models.FloatField(default=5.673)

    class Meta:
        unique_together = (('big_int', 'floating'))
