from django.core.exceptions import ImproperlyConfigured, ValidationError
from rest_framework.exceptions import ValidationError as RESTValidationError
from rest_framework.generics import GenericAPIView
from datetime import datetime

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

    def get_queryset(self):
        if not self.historical_manager:
            raise ImproperlyConfigured("historical_manager' must be defined")

        as_of_date = self.request.query_params.get(self.as_of_field, None)
        if as_of_date:
            try:
                return self.historical_manager.as_of(as_of_date)
            except ValidationError:
                return self.historical_manager.none()
        else:
            return super().get_queryset()

    def validate_as_of(self, as_of):
        if as_of:
            error_message = "as_of parameter doesn't match YYYY-MM-DD-HH:MM:SS format"
            try:
                datetime.strptime(as_of, "%Y-%m-%d-%H:%M:%S")
            except ValueError:
                raise RESTValidationError(error_message)
