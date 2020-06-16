from django.db import models

class BusinessType(models.Model):

    name = models.CharField(max_length=55)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name