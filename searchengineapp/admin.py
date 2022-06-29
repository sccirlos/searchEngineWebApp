from django.contrib import admin
from searchengineapp import models

# Register your models here.
admin.site.register(models.Router)
admin.site.register(models.Docs)