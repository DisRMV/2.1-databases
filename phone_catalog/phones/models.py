from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
