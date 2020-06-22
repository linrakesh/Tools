from django.db import models

# Create your models here


class shorturl(class (models.Model):
    original_url=models.URLField(max_length=250)
    short_url=models.URLField(max_length=50)
