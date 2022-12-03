from datetime import datetime

import pytz
from django_filters import rest_framework as dfilters

from mailing.models import Client

utc = pytz.UTC


class TagOperatorFilter(dfilters.FilterSet):
    tag = dfilters.CharFilter(field_name="tag", method='get_tag')
    operator_code = dfilters.CharFilter(field_name="operator_code", method='get_operator_code')

    def get_tag(self, queryset, name, value):
        tags = list(value.split('-'))
        print(tags)
        if tags:
            return Client.objects.filter(tag__in=tags)
        return queryset
    
    def get_operator_code(self, queryset, name, value):
        cods = list(value.split('-'))
        print(cods)
        if cods:
            return Client.objects.filter(operator_code__in=cods)
        return queryset

    class Meta:
        model = Client
        fields = ('tag', 'operator_code')