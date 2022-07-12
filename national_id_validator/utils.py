from django.core.exceptions import ValidationError
import re
from .common import GOVERNORATES
from datetime import datetime


def nid_get_month(nid):
    return int(nid[3:5])


def nid_get_day(nid):
    return int(nid[5:7])


def nid_get_governate_code(nid):
    return nid[7:9]


def nid_get_birth_century(nid):
    return int(nid[0]) + 17


def nid_validation(nid):
    """
    check if the passed enid is valid
    based on its length, and not starts by 0
    """
    if not re.match(r'^([\s\d]+)$', nid):
        raise ValidationError('national id should only contain integers')
    if int(nid[0]) < 1:
        raise ValidationError('leading number of national id may not be 0')
    if len(nid) != 14:
        raise ValidationError('national id should be 14 integers')

    month = nid_get_month(nid)
    if month not in range(1, 13):
        raise ValidationError('Invalid month for national id')

    day = nid_get_day(nid)
    if day not in range(1, 32):
        raise ValidationError('Invalid day for national id')

    governate_code = nid_get_governate_code(nid)
    if governate_code not in GOVERNORATES.keys():
        raise ValidationError('Invalid Governorate code')

    century = nid_get_birth_century(nid)
    if century not in range(10, 22):
        raise ValidationError('Invalid Century code')
    return True
