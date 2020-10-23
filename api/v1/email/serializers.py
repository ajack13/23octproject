from django.conf import settings
from django.core.validators import ValidationError
from rest_framework import serializers
from . import validators


class FileUploadSerializer(serializers.Serializer):
    """
    This class is used to serialize the file received from user
    and check whether the file extension supplied is valid or not.
    """
    file = serializers.FileField()
    from_email = serializers.EmailField()
    body = serializers.CharField(allow_blank=False)
    subject = serializers.CharField(allow_blank=False)

    def validate(self, attrs):
        """
        :param attrs: csv
        :return: raises exception if file extension does not match.
        """
        file_extension_valid = validators.validate_file_extension(attrs['file'], ['.csv'])
        if file_extension_valid is False:
            raise ValidationError('Sorry! You have provided invalid file type.')
        return attrs

    class Meta:
        fields = ("file",)

class EmailSerializer(serializers.Serializer):
    """
    This class is used to serialize the file received from user
    and check whether the file extension supplied is valid or not.
    """
    to = serializers.ListField()
    cc = serializers.ListField(allow_empty=True)
    bcc = serializers.ListField(allow_empty=True)
    subject = serializers.CharField(allow_blank=False)
    body = serializers.CharField(allow_blank=False)

    def validate(self, attrs):
        """
        :param attrs: pdf
        :return: raises exception if file extension does not match.
        """

        if len(attrs['to']) == 0:
            raise ValidationError('Sorry! You have to provided atleast one email')

        email_valid = validators.email_validator(attrs['to'])
        if email_valid is False:
            raise ValidationError(
                'Sorry! You have provided invalid email in to address.')

        email_valid = validators.email_validator(attrs['cc'])
        if email_valid is False:
            raise ValidationError(
                'Sorry! You have provided invalid email in cc.')

        email_valid = validators.email_validator(attrs['bcc'])
        if email_valid is False:
            raise ValidationError(
                'Sorry! You have provided invalid email in bcc.')
        return attrs
