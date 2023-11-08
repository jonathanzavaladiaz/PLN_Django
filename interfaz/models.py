from django.db import models

# Create your models here.


class Narrativa(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(
        max_length=30000, verbose_name="descripcion")
