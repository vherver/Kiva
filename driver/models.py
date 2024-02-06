from django.db import models

from core.models import TimeStampedMixin


class Driver(TimeStampedMixin):
    """
    Django model representing a driver.

    Attributes:
        name (str): Name of the driver.
        email (str): Email address of the driver.
        address (str): Address of the driver.

    Inheritance:
        This class inherits from TimeStampedMixin to include automatic
        timestamp fields.
    """

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256)
    address = models.CharField(max_length=256)

    def __repr__(self):
        """
        Returns a string representation of the Driver object.

        Returns:
            str: String representation of the object.
        """
        return (
            f"{self.__class__.__name__}"
            f"(name={self.name!r}-email={self.email!r})"
        )