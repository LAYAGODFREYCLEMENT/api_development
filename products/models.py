from django.db import models
from django.utils.translation import gettext_lazy
from django.contrib.postgres import fields as PostgresFields

# Create your models here.
class ProductCatergory(models.models):
    name = models.CharField(max_length=256)
    icon_url = models.URLField(blank=True)
    description = models.TextField(blank=False)
    parent_catergory = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="children_catergories",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
