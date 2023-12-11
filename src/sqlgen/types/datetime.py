from .base import BaseDateType
from datetime import datetime


class DateTime(BaseDateType):
    _TYPE_NAME = 'datetime'

    def __init__(self) -> None:
        DATE_PATTERN = '%Y-%m-%d %H:%M:%S'
        super().__init__(self._TYPE_NAME, DATE_PATTERN)

    def __str__(self) -> str:
        rendered_value = super().name

        return rendered_value

    def validate_value(self, value: str) -> bool:
        try:
            datetime.strptime(value, super().pattern)
        except Exception:
            return False

        return True