from django.core.exceptions import ValidationError


def first_name_min_length_validator(value):
    if len(value) < 3:
        raise ValidationError("First name must be at least 3 characters long.")

def last_name_min_length_validator(value):
    if len(value) < 2:
        raise ValidationError("Last name must be at least 2 characters long.")

def first_letter_upper_case(value):
    if not value[0].isupper():
        raise ValidationError("First letter must be upper case.")