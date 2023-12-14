'''
Defines the abstract base class for constructing abstract SQL type classes.
'''

from abc import ABCMeta, abstractmethod
from typing import Any
from pysqlquery.types.exceptions.sql_type import InvalidTypeName


class SQLType(metaclass=ABCMeta):
    '''
    Abstract class for construct abstract SQL type classes.

    This class provides the basic structures for construct
    abstract classes for kind of SQL types.

    This class must be inherited by abstract one.
    '''

    def __init__(self, sql_type_name: str) -> None:
        '''
        Parameters
        ----------
        sql_type_name : str
            The name of SQL type.

        Returns
        -------
        None
        '''

        super().__init__()

        self._validate_name(sql_type_name)
        self._name: str = self._format_type_name(sql_type_name)

    def _validate_name(self, type: str) -> None:
        if not self._is_name_valid(type):
            raise InvalidTypeName()

    def _is_name_valid(self, type: str) -> bool:
        return isinstance(type, str) and len(type)

    def _format_type_name(self, type: str) -> str:
        return type.strip().upper()

    @abstractmethod
    def __str__(self) -> str:
        '''
        Returns
        -------
        str
            A string representation of the class instance in SQL format.
        '''

        pass

    @abstractmethod
    def validate_value(self, value: Any) -> bool:
        '''
        Parameters
        ----------
        value : Any
            The value to be validated.

        Returns
        -------
        bool
            True if the value is valid for the SQL type, False otherwise.
        '''

        pass

    @property
    def name(self) -> str:
        return self._name