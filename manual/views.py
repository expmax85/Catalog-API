import datetime
from typing import Union

from django.db.models import QuerySet
from rest_framework import viewsets

from manual.exceptions import ElementNotExist, WrongDateFormat, WrongQueryParams, \
    ManualNotExist, NotDefinedManualError
from manual.serializers import ManualElemSerializer, ManualVersionSerializer
from manual.models import ManualElem, ManualVersion, Manual
from manual.services import get_unique_manuals


ELEMS_ALLOW_PARAMS = ['manual_id', 'version', 'code', 'value', 'offset', 'limit']
MANUAL_ALLOW_PARAMS = ['from_date', 'offset', 'limit']


class ManualElemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API View for manual elements, read only.
    Allows next parameters for filtering of elements:
     - manual_id: parameter for define a manual, in which need to filter
     - version: define the manual version
     - code, value: parameters allows to check/searching some manual element in all manuals or
     with using previous parameters
         Example: /elems/?manual_id=1&version=1.0&code=1111
    """
    serializer_class = ManualElemSerializer

    def get_queryset(self) -> QuerySet:
        wrong_params = [x for x in self.request.query_params.keys()
                        if x not in ELEMS_ALLOW_PARAMS]
        manual_id = self.request.query_params.get('manual_id')
        version = self.request.query_params.get('version')
        code = self.request.query_params.get('code')
        value = self.request.query_params.get('value')

        if wrong_params:
            raise WrongQueryParams
        if not manual_id and any([version, code, value]):
            raise NotDefinedManualError
        if manual_id:
            params = {}
            if code:
                params['code'] = code
            if value:
                params['value'] = value

            if not Manual.objects.filter(id=manual_id).exists():
                raise ManualNotExist

            if version is None:
                date = datetime.date.today()
                manual = ManualVersion.objects.select_related('manual_info')\
                                              .filter(manual_info_id=manual_id, from_date__lte=date)\
                                              .order_by('from_date')\
                                              .last()
                if not manual:
                    raise ManualNotExist
                queryset = ManualElem.objects.select_related('manual', 'manual__manual_info')\
                                             .filter(manual=manual, **params)
            else:
                queryset = ManualElem.objects.select_related('manual', 'manual__manual_info')\
                                             .filter(manual__manual_info_id=manual_id,
                                                     manual__version=version, **params)

            if not queryset:
                if code or value:
                    raise ElementNotExist
            return queryset

        queryset = ManualElem.objects.select_related('manual', 'manual__manual_info').all()
        return queryset


class ManualVersionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API View for manuals, read only. Allow one query parameter: "from_date"
    for filtering of actual manuals by given date in format: "YYYY-MM-DD".
        Example: /manuals/?from_date=2022-01-01
    """
    serializer_class = ManualVersionSerializer

    def get_queryset(self) -> Union[list, 'QuerySet']:
        wrong_params = [x for x in self.request.query_params.keys()
                        if x not in MANUAL_ALLOW_PARAMS]
        if wrong_params:
            raise WrongQueryParams

        from_date = self.request.query_params.get('from_date')
        if from_date:
            if from_date == 'today':
                from_date = datetime.datetime.today()
            else:
                try:
                    datetime.datetime.strptime(from_date, '%Y-%m-%d')
                except ValueError:
                    raise WrongDateFormat

            queryset = ManualVersion.objects.select_related('manual_info')\
                                            .filter(from_date__lte=from_date)\
                                            .order_by('-from_date')
            queryset = get_unique_manuals(queryset=queryset)
            return queryset

        queryset = ManualVersion.objects.select_related('manual_info').all()
        return queryset
