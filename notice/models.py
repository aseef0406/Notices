from django.db import models

# Create your models here.
class Notices(models.Model):
    n_date=models.DateTimeField()
    n_title=models.CharField(max_length=255)
    n_data=models.TextField()

    def __str__(self):
        return self.n_title

class Events(models.Model):
    e_date=models.DateTimeField()
    e_title=models.CharField(max_length=255)
    e_data=models.TextField()

    def __str__(self):
        return self.e_title
