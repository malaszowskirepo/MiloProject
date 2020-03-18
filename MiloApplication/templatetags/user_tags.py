from datetime import date
from django import template

register = template.Library()


@register.simple_tag
def is_under_13(birthdate):
    if calculate_age(birthdate) > 13:
        return "allowed"
    return "blocked"


@register.simple_tag
def bizz_fuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "BizzFuzz"
    elif number % 3 == 0:
        return "Bizz"
    elif number % 5 == 0:
        return "Fuzz"
    else:
        return str(number)


def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
