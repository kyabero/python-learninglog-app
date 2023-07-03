from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# AbstractUserはユーザーを管理するテーブル作成
class CustomUser(AbstractUser):
    pass