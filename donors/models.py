from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class details(models.Model):
    display_name  = models.CharField(max_length = 150)
    display_from  = models.DateField()
    display_until = models.DateField()
    display_on_tv_id   = models.CharField(max_length=50)

@receiver(pre_delete, sender=details)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file_path.delete(False)
# Create your models here.
