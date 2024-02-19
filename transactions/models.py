from django.db import models
import uuid
# Create your models here.

class transactionsModel(models.Model):
    transaction_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    transactionAmount = models.IntegerField()
    timestamp = models.IntegerField()
    transferOrReceiveIconUrl = models.CharField(max_length = 100)
    
