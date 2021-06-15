from django.db import models

# Create your models here.
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64,null=False)