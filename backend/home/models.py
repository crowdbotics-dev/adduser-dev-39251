from django.conf import settings
from django.db import models


class Test(models.Model):
    "Generated Model"
    prd = models.BigIntegerField()
class Tested(models.Model):
    'Generated Model'
    newuser = models.UUIDField()
