from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_inn(value):
    if not (10000000000000 <= value <= 99999999999999):
        raise ValidationError(
            _('INN must be a 14-digit number.'),
        )
    if not (str(value)[0] == '1' or str(value)[0] == '2'):
        raise ValidationError(
            _('INN must be start 1 or 2.')
        )
