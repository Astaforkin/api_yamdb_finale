from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year(value):
    if timezone.now().year < value:
        raise ValidationError(
            "The year of publication cannot be greater than the current year"
        )
