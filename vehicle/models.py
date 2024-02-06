from django.db import models

from core.models import TimeStampedMixin
from model.models import SubBrand


class Vehicle(TimeStampedMixin):
    """
    Django model representing a vehicle.

    Attributes:
        year (int): Manufacturing year of the vehicle.
        serial (str): Serial number or identifier of the vehicle.
        model (SubBrand): ForeignKey relationship with the SubBrand model,
                          representing the specific model of the vehicle.

    """

    year = models.IntegerField()
    serial = models.CharField(max_length=100)
    model = models.ForeignKey(SubBrand, on_delete=models.SET_NULL, null=True)

    def __repr__(self):
        """
        Returns a string representation of the Vehicle object.

        Returns:
            str: String representation of the object.
        """
        return (
            f"{self.__class__.__name__}"
            f"(model={self.model!r}-serial={self.serial!r})"
        )
