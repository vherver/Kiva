from django.db import models


class TimeStampedMixin(models.Model):
    """
        A Django model mixin that adds timestamp fields to track creation, last update, and deletion.

        Usage:
            class YourModel(TimeStampedMixin):
                # Your other model fields go here

        Fields:
            - created: DateTimeField, automatically set to the current date and time when the object is created.
            - updated: DateTimeField, automatically updated to the current date and time whenever the object is saved.
            - deleted: DateTimeField, defaults to None, can be set to mark the object as deleted with a specific date and time.

    """

    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted = models.DateTimeField(default=None, blank=True, null=True)
