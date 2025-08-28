from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=3)
    contact = models.CharField(max_length=50)
    last_donation = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.blood_group})"

class Recipient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blood_group_needed = models.CharField(max_length=3)
    urgency = models.CharField(max_length=20)
    contact = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} needs {self.blood_group_needed}"
