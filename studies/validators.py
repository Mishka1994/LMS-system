import re

from rest_framework import serializers


class LinkValidator:
    def __call__(self, value):

        if 'http' in value or 'www' in value:
            list_of_matches = re.findall(r"\byoutube\.com\b", value)
            if len(list_of_matches) == 0:
                raise serializers.ValidationError('Ссылка указана некорректно или ведёт на сторонний ресурс!')


