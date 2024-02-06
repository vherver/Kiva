from django.db import models

from core.models import TimeStampedMixin


class Brand(TimeStampedMixin):
    """
    A Django model representing a brand with a name and timestamp fields.

    Fields:
        - name: CharField, the name of the brand.

    Inherits:
        - TimeStampedMixin: Provides 'created', 'updated',
        and 'deleted' timestamp fields.

    Example:
        brand = Brand(name='Example Brand')
        brand.save()
        print(brand.created)  # Output: The date and time when the brand
        was created.
    """

    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"
