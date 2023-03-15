from dateutil.parser import isoparse
from django.core.exceptions import ImproperlyConfigured, ValidationError
from rest_framework.exceptions import ValidationError as RESTValidationError
from rest_framework.generics import GenericAPIView


class OptionallyHistoricalView(GenericAPIView):
    """
    View mix-in for time travel.
    Shows current state if "as_of" query param is unspecified.
    Shows historical states if "as_of" contains a valid date-time string.
    """
    historical_manager = None
    as_of_field = "as_of"

    def get(self, request, *args, **kwargs):
        self.validate_as_of(request.query_params.get(self.as_of_field))
        return super().get(self, request, *args, **kwargs)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.historical_manager:
            raise ImproperlyConfigured("historical_manager' must be defined")

    def get_queryset(self):
        as_of = self.request.query_params.get(self.as_of_field, None)

        if not as_of:
            return super().get_queryset()
        try:
            return self.historical_manager.as_of(as_of)
        except ValidationError:
            return self.historical_manager.none()

    def validate_as_of(self, as_of):
        error_message = "as_of parameter doesn't match ISO date format"
        if not as_of:
            return
        try:
            isoparse(as_of)
        except ValueError as e:
            raise RESTValidationError(error_message + ": " + str(e))
