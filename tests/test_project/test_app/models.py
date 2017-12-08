from django.db import models


class NewName(models.Model):
    null_field = models.IntegerField(null=True)
    new_not_null_field = models.IntegerField(null=False)

    #myauto = models.AutoField()
    #mybigauto = models.BigAutoField()
    mybinary = models.BinaryField(null=True)
    myboolean = models.BooleanField(default=False)
    mychar = models.CharField(max_length=256, null=True)
    mydecimal = models.DecimalField(max_digits=20, decimal_places=5, null=True)
    myduration = models.DurationField(null=True)
    myemail = models.EmailField(null=True)
    myfile = models.FileField(null=True)
    myfilepath = models.FilePathField(null=True)
    myfloat = models.FloatField(null=True)
    myimage = models.ImageField(null=True)
    mybiginteger = models.BigIntegerField(null=True)
    #myipaddress = models.IPAddressField()
    mygenericipaddress = models.GenericIPAddressField()
    mynullboolean = models.NullBooleanField()
    mypositiveinteger = models.PositiveIntegerField(default=5)
    mypositivesmallinteger = models.PositiveSmallIntegerField(null=True)
    myslug = models.SlugField(null=True)
    mytext = models.TextField(unique=True, null=False)
    myuuid = models.UUIDField(unique=True, null=True)
    myurl = models.URLField(null=True)
