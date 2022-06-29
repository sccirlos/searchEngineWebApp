from django.db import models



# Create your models here.
class Router(models.Model):
    specifications = models.FileField(upload_to='router_specifications')

class Docs(models.Model):
    urldoc = models.FileField(upload_to='Docs')

# class testDoc(models.Model):
#     text = models.CharField(max_length=255)

#     class Meta:
#         verbose_name_plural = "testDocs"