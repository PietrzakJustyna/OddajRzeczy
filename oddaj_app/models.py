from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=124)


class Institution(models.Model):
    INSTITUTION_TYPE_CHOICES = [("Fundacja", "Fundacja"),
                                ("Organizacja", "Organizacja pozarządowa"),
                                ("Zbiorka", "Zbiórka lokalna")
                                ]

    name = models.CharField(max_length=124)
    description = models.TextField()
    type = models.CharField(max_length=12, choices=INSTITUTION_TYPE_CHOICES, default="Fundacja")
    categories = models.ManyToManyField(Category)


class Donations(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=124)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=62)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
