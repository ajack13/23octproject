import os
import re

# for validating an Email
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

# for validating an Email
def email_validator(email_list):

    if len(email_list) == 0:
        return True

    for email in email_list:
        if not (re.search(regex, email)):
            return False

    return True

def validate_file_extension(value, valid_extensions):
    """
    :param valid_extensions: valid file extensions to be checked.
    :param value: filename
    :return: True if file extension matched else False.
    """
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    if not ext.lower() in valid_extensions:
        return False
    return True
