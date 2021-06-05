from django.utils import timezone
from django.db import models

# Product model
class product(models.Model):
    product_name = models.CharField(max_length=100, help_text='Enter a product name (e.g. Stapler)')
    product_description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        """String for representing the Model object."""
        return str(self.product_name)
