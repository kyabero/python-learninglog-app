from django.db import models
from addounts.models import CustomUser

# Create your models here.
class EntryModel(models.Model): #EntryModelテーブル作成
    title = models.CharField(max_length=50) # titleカラム作成
    entry_text = models.CharField(max_length=500) # entry_textカラム作成
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) # userカラム作成
