from django.db import models
from django.core.validators import RegexValidator

class Mosque(models.Model):
    mosque_name = models.CharField(max_length=150, blank=False)
    mosque_focal_point = models.CharField(max_length=150, blank=False)
    mosque_address = models.CharField(max_length=150, blank=True)
    mosque_email = models.EmailField(max_length=150, blank=True)
    mosque_phone = models.CharField(validators=[RegexValidator(regex='^\1?\d{9,10}$')],max_length=10,blank=True)
    mosque_website = models.URLField(max_length=150, blank=True)
    mosque_city = models.CharField(max_length=150, blank=True)
    mosque_state = models.CharField(max_length=150, blank=False)
    mosque_bank = models.CharField(max_length=150, blank=False)
    mosque_account = models.IntegerField(max_length=10, blank=False)
    mosque_status = models.BooleanField(default=True)
    mosque_date_created = models.DateTimeField(auto_created=True)
    mosque_date_disabled = models.DateTimeField(null=True, blank=True)
    mosque_image = models.ImageField(upload_to='mosques', blank=True)

    def __str__(self):
        return "{} - {} [{}]".format(self.mosque_name, self.mosque_address, self.mosque_focal_point)

# Create your models here.
