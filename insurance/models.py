from django.db import models
from django_fsm import FSMField, transition

from core.models import TimeStampedMixin
from driver.models import Driver
from vehicle.models import Vehicle


class Application(TimeStampedMixin):
    """
       Django model representing an insurance application.

       Attributes:
           STATE_SUBMISSION (str): Constant representing the submission state
           of the application.
           STATE_REVIEW (str): Constant representing the review state of
           the application.
           STATE_APPROVAL (str): Constant representing the approval state of
           the application.
           STATE_REJECTION (str): Constant representing the rejection state
           of the application.

           STATE_CHOICES (list): A list of tuples containing state choices for
           applications, used for database storage and form display.
             Each tuple consists of the state constant and its corresponding
             display label.

           state (FSMField): A finite state machine field representing the
           current state of the application.

           submitted_at (DateTimeField): Date and time when the application
           was submitted.
           reviewed_at (DateTimeField): Date and time when the application
           was reviewed.
           approved_at (DateTimeField): Date and time when the application
           was approved.
           rejected_at (DateTimeField): Date and time when the application
           was rejected.

           driver (ForeignKey): ForeignKey relationship with the Driver
           model, representing the driver associated with the application.
           vehicle (ForeignKey): ForeignKey relationship with the Vehicle
           model, representing the vehicle associated with the application.

       Methods:
           review(): Transition the application state from submission to
           review.
           approve(): Transition the application state from review to
           approval.
           reject(): Transition the application state from submission or
           review to rejection.

       """
    STATE_SUBMISSION = 'submission'
    STATE_REVIEW = 'review'
    STATE_APPROVAL = 'approval'
    STATE_REJECTION = 'rejection'

    STATE_CHOICES = [
        (STATE_SUBMISSION, 'Submission'),
        (STATE_REVIEW, 'Review'),
        (STATE_APPROVAL, 'Approval'),
        (STATE_REJECTION, 'Rejection'),
    ]

    state = FSMField(default=STATE_SUBMISSION, choices=STATE_CHOICES)
    submitted_at = models.DateTimeField(null=True, blank=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    rejected_at = models.DateTimeField(null=True, blank=True)

    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)

    @transition(field=state, source=STATE_SUBMISSION, target=STATE_REVIEW)
    def review(self):
        self.submitted_at = self.updated
        self.reviewed_at = self.updated

    @transition(field=state, source=STATE_REVIEW, target=STATE_APPROVAL)
    def approve(self):
        self.approved_at = self.updated

    @transition(field=state, source=[STATE_SUBMISSION, STATE_REVIEW],
                target=STATE_REJECTION)
    def reject(self):
        self.rejected_at = self.updated
