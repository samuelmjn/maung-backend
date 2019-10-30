from django.db import models

# Create your models here.
class Member(models.Model):
    full_name = models.CharField(max_length=60, blank=False)
    first_name = models.CharField(max_length=60, blank=False)
    birth_date_place = models.CharField(max_length=60, blank=False)
    absence_code = models.CharField(max_length=60, blank=False)
    major = models.CharField(max_length=60, blank=False)
    high_school = models.CharField(max_length=60, blank=False)
    line_id = models.CharField(max_length=60, blank=False)
    instagram = models.CharField(max_length=60, blank=False)
    email = models.CharField(max_length=60, blank=False)
    interest = models.CharField(max_length=60, blank=False)
    hope = models.CharField(max_length=60, blank=False)
    description = models.TextField()
    image_url = models.CharField(max_length=200, blank=True)