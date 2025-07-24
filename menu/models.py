from django.db import models

# Create your models here.
class Bagel(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True) # Optional longer description
    price = models.DecimalField(max_digits=5, decimal_places=2) # e.g., 2.50
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name'] # Order bagels alphabetically by default

    def __str__(self):
        return self.name # How a Bagel object is represented in the admin