from django.db import models


class Site(models.Model):
    details = models.CharField(default="Starts", max_length=20)

    def __str__(self):
        return self.details
