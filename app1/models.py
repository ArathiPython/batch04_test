from django.db import models

# Create your models here.
class log(models.Model):
    user_name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    user_type=models.CharField(max_length=30)

    class meta:
        db_table="log"

class newuser(models.Model):
    name=models.CharField(max_length=30)
    job=models.CharField(max_length=30)
    join_date=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    nobr=models.CharField(max_length=30)
    address=models.CharField(max_length=30)

    class meta:
        db_table="newuser"