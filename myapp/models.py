from django.db import models

# Create your models here.
class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return self.uname

class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=25)
    age = models.IntegerField()
    addr = models.CharField(max_length=500)
    pin = models.IntegerField()
    contact = models.IntegerField()
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.fname


class architect_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=25)
    age = models.IntegerField()
    addr = models.CharField(max_length=250)
    pin = models.CharField(max_length=25)
    contact = models.CharField(max_length=25)
    image = models.CharField(max_length=250)
    descrp = models.CharField(max_length=250)
    email = models.CharField(max_length=150)
    status = models.CharField(max_length=25)

class plan_settings(models.Model):
    plan_type = models.CharField(max_length=50)

class architect_plans(models.Model):
    plan_id = models.IntegerField()
    arch_id = models.IntegerField()
    title = models.CharField(max_length=250)
    descrp = models.CharField(max_length=250)
    amount = models.FloatField()
    dt = models.CharField(max_length=25)
    tm = models.CharField(max_length=25)

class plan_details(models.Model):
    ar_plan_id = models.IntegerField()
    title = models.CharField(max_length=250)
    image = models.CharField(max_length=150)
    descrp = models.CharField(max_length=250)

class user_search(models.Model):
    user_id = models.IntegerField()
    query = models.CharField(max_length=250)
    dt = models.CharField(max_length=25)
    tm = models.CharField(max_length=25)

class user_proposal(models.Model):
    user_id = models.IntegerField()
    arch_id = models.IntegerField()
    requirments = models.CharField(max_length=250)
    filepath = models.CharField(max_length=250)
    remark = models.CharField(max_length=250)
    dt = models.CharField(max_length=25)
    tm = models.CharField(max_length=25)
    status = models.CharField(max_length=25)

class user_rating(models.Model):
    user_id = models.IntegerField()
    plan_id = models.IntegerField()
    remarks = models.CharField(max_length=250)
    rating = models.IntegerField()
    dt = models.CharField(max_length=25)
    tm = models.CharField(max_length=25)

class sales_master(models.Model):
    plan_id = models.IntegerField()
    user_id = models.IntegerField()
    arch_id = models.IntegerField()
    commision = models.FloatField()
    card = models.CharField(max_length=25)
    number = models.CharField(max_length=25)
    cvv = models.CharField(max_length=25)
    dt = models.CharField(max_length=25)
    tm = models.CharField(max_length=25)


