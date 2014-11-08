from django.db import models

# Create your models here.


class List(models.Model):
    title = models.CharField(maxlength=250, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    class Admin:
        pass
