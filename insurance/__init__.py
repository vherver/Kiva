class ApplicationStatus:
    """
    Class representing the status of a job application.

    Constants:
        - SUBMISSION (str): Represents the submission status of an application.
        - REVIEW (str): Represents the review status of an application.
        - APPROVAL (str): Represents the approval status of an application.
        - REJECTION (str): Represents the rejection status of an application.

    Choices:
        - CHOICES (list): A list of tuples containing status choices for
        applications, used for database storage and form display.
          Each tuple consists of the status constant and its corresponding
          display label.

    Methods:
        - for_display(choice): Static method to get the display label for a
        given status choice.

    Usage:
        status = AppliationStatus.SUBMISSION
        display_label = AppliationStatus.for_display(status)
    """

    SUBMISSION = "submission"
    REVIEW = "review"
    APPROVAL = "approval"
    REJECTION = "rejection"

    CHOICES = [
        (SUBMISSION, "Submission"),
        (REVIEW, "Review"),
        (APPROVAL, "Approval"),
        (REJECTION, "Rejection"),
    ]

    @staticmethod
    def for_display(choice):
        """
        Static method to get the display label for a given status choice.

        Args:
            choice (str): The application status choice.

        Returns:
            str: Display label corresponding to the provided status choice.
        """
        return dict(ApplicationStatus.CHOICES).get(choice)
