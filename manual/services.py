from typing import List

from django.db.models import QuerySet


def get_unique_manuals(queryset: QuerySet) -> List:
    temp = []
    result = []
    for item in queryset:
        value = item.manual_info
        if value not in temp:
            temp.append(value)
            result.append(item)
    return result
