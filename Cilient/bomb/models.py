from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data=((1,"Administrator"),(2,"Financial"),(3,"Author"),(4,"Participant"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)


class AdminCIIS(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Financials(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Authors(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    phoneno=models.CharField(max_length=255,null=False)
    passportid=models.CharField(max_length=255,null=False)
    affiliation=models.CharField(max_length=255,null=False)
    country=models.CharField(max_length=255,null=False)
    nationality=models.CharField(max_length=255,null=False)
    status=models.CharField(max_length=255,null=False)

    #updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Participants(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    phoneno=models.CharField(max_length=255,null=False)
    passportid=models.CharField(max_length=255,null=False)
    affiliation=models.CharField(max_length=255,null=False)
    country=models.CharField(max_length=255,null=False)
    nationality=models.CharField(max_length=255,null=False)
    status=models.CharField(max_length=255,null=False)
    
    #updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


#paper
class DataCIIS(models.Model):
    id=models.AutoField(primary_key=True)
    paper_id = models.CharField(max_length=255)
    paper_title=models.CharField(max_length=255)
    author_name=models.CharField(max_length=255)
    author_email=models.CharField(max_length=255)
    paper_type=models.CharField(max_length=255)


#AddPaper author
class paperauthor(models.Model):
    id=models.AutoField(primary_key=True)
    paper_id = models.CharField(max_length=255)
    paper_title=models.CharField(max_length=255)
    author_name=models.CharField(max_length=255)
    paper_type=models.CharField(max_length=255)
    email_add=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    objects = models.Manager()


def filename(self):
    return os.path.basename(self.file.name)



@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminCIIS.objects.create(admin=instance)
        if instance.user_type==2:
            Financials.objects.create(admin=instance,address="")
        if instance.user_type==3:
            Authors.objects.create(admin=instance)
        if instance.user_type==4:
            Participants.objects.create(admin=instance)

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminciis.save()
    if instance.user_type==2:
        instance.financials.save()
    if instance.user_type==3:
        instance.authors.save()
    if instance.user_type==4:
        instance.participants.save()
