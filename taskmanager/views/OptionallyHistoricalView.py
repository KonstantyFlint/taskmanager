from django.core.exceptions import ImproperlyConfigured


class OptionallyHistoricalView:
    historical_manager = None
    as_of_field = "as_of"

    def get_queryset(self):
        if not self.historical_manager:
            raise ImproperlyConfigured("historical_manager' must be defined")

        as_of_date = self.request.query_params.get(self.as_of_field, None)
        if as_of_date:
            return self.historical_manager.as_of(as_of_date)
        else:
            return super().get_queryset()
