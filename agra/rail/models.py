from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class User(models.Model):
    email_id = models.EmailField(primary_key=True)
    fullname = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    mobile = models.IntegerField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


    def __str__(self):
        return self.username

class Train(models.Model):
    trno=models.IntegerField(primary_key=True)
    trname=models.CharField(max_length=30)
    def __str__(self):
        return self.trname
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.trno})

class Station(models.Model):
    stationC=models.IntegerField(primary_key=True)
    Stname=models.CharField(max_length=20)
    def __str__(self):
        return self.Stname
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.stationC})


class Tinfo(models.Model):
    trno = models.ForeignKey(Train, on_delete=models.CASCADE)
    pid=models.AutoField(primary_key=True)
    ordn0=models.IntegerField()
    stationC=models.ForeignKey(Station, on_delete=models.CASCADE)
    sA=models.TimeField(blank=True)
    aD=models.TimeField( blank=True)
    A=models.TimeField( blank=True)
    D=models.TimeField(blank=True)
    late=models.TimeField( blank=True)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pid})

    def __str__(self):
        return str(self.ordn0)
