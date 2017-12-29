from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.


class fileDetails(models.Model):
    title           = models.CharField(max_length=150)
    filetype        = models.CharField(max_length=10, null = False, choices = (('video', "Video"), ('img', 'Image')))
    play_from       = models.DateField()
    play_Till       = models.DateField()
    play_duration   = models.IntegerField(default=20, null= True)
    play_on_tv_id   = models.CharField(max_length=50)
    file_path       = models.FileField(null = False)


class tvDetails(models.Model):
    tv_name         = models.CharField(max_length=150)
    tv_description  = models.CharField(max_length=250)
    tv_location     = models.CharField(max_length=150)


@receiver(pre_delete, sender=fileDetails)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file_path.delete(False)