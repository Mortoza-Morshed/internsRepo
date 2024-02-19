from django.db import models
import uuid
# Create your models here.

class servicesModel(models.Model):
    services_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    iconUrl = models.CharField(max_length = 100)
    iconText = models.CharField(max_length = 100)
    iconHeight = models.IntegerField()
    iconWidth = models.IntegerField()
