import re


def check_positive_number(value):
    if str(value).isdigit() and value > 0:
        return True
    else:
        return False


print(check_positive_number(1))