from django.db import models


#from passlib.hash import pbkdf2_sha256

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=20, unique=True)
    password=models.CharField(max_length=20)
    Email=models.CharField(max_length=20,default=0)
    def __str__(self):
        return self.username

class Member(models.Model):
    firstname=models.CharField(max_length=30, blank=True)
    lastname=models.CharField(max_length=30, blank=True)
    username=models.CharField(max_length=30, unique=True)
    password=models.CharField(max_length=12)

    #def verify_password(self, raw_password):
        #return pbkdf2_sha256.verify(raw_password, self.password)
