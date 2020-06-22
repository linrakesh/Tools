from django.db import models

# Create your models here


class shorturl(models.Model):
    original_url = models.URLField(max_length=250)
    short_url = models.CharField(max_length=10)

    def __str__(self):
        return self.original_url
