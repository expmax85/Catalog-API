from rest_framework.exceptions import APIException


class WrongDateFormat(APIException):
    status_code = 406
    default_detail = 'Wrong date Format. You should to write the date in format: YYYY-MM-DD'
    default_code = 'WrongDateFormat'


class ElementNotExist(APIException):
    status_code = 404
    default_detail = 'Element with this code/value is not exist'
    default_code = 'ElementNotExist'


class ManualNotExist(APIException):
    status_code = 404
    default_detail = 'Manual not exist or wrong manual version. Check the parameters.'
    default_code = 'ManualNotExist'


class WrongQueryParams(APIException):
    status_code = 405
    default_detail = 'Wrong filter parameters or not specified manual_id. ' \
                     'You need to use only next parameters: manual_id, version, code, value.'
    default_code = 'WrongQueryParams'


class NotDefinedManualError(APIException):
    status_code = 428
    default_detail = 'Parameter manual_id is required.'
    default_code = 'NotDefinedManualError'
