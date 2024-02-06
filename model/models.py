from django.db import models

from brand.models import Brand
from core.models import TimeStampedMixin


class SubBrand(TimeStampedMixin):
    """
    Represents a model with fields for 'name', 'slug',
    and a foreign key 'brand'.
    Inherits from TimeStampedMixin for timestamped fields
    'created' and 'modified'.
    """

    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)

    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        related_name="brand",
        null=True,
        blank=True,
        help_text="The associated brand for this model.",
    )

    def __repr__(self):
        """
        Returns a string representation of the model.
        Example: YourModelName(brand='BrandName'-name='ModelName')
        """
        return (
            f"{self.__class__.__name__}"
            f"(brand={self.brand!r}-name={self.name!r})"
        )
