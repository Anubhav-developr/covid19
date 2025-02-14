from django.db import models
from django.utils import timezone
from django.conf import settings


class Shop(models.Model):
    class ShopObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(verified=True)

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    published = models.DateTimeField(default=timezone.now)
    resources = models.CharField(max_length=200, default="")
    special_remarks = models.CharField(max_length=200, default="")
    objects = models.Manager()

    verifiedObjects = ShopObjects()

    class Meta:
        ordering = ('state',)

    def __str__(self):
        return self.name
