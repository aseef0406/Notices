from django.db import models

# Create your models here.


class ContactModel(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sender = models.EmailField()
    cc_myself = models.BooleanField()

    def __str__(self):
        return self.subject

class RegisterModel(models.Model):
    registrationNo = models.CharField(primary_key=True,max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    password_repeat = models.CharField(max_length=64)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    verified=models.BooleanField()
    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

