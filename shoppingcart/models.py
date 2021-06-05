from django.db import models
from django.utils import timezone

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    home_phone = models.CharField(max_length=12, blank=True)
    work_phone = models.CharField(max_length=12, blank=True)
    cell_phone = models.CharField(max_length=12, blank=True)
    addr_line1 = models.CharField(max_length=200)
    addr_line2 = models.CharField(max_length=200, blank=True)
    addr_line3 = models.CharField(max_length=200, blank=True)
    addr_line4 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.first_name + ', ' + self.last_name)
