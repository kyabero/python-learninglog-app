from django.contrib import admin
from .models import EntryModel

# Register your models here.
# 管理画面にEntryModelを表示する
admin.site.register(EntryModel)