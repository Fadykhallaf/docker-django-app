from django.db import models

class country(models.Model):
    name = models.CharField(max_length=50)
    continent = models.CharField(max_length=20)


    def __str__(self) -> str:
        return self.name
