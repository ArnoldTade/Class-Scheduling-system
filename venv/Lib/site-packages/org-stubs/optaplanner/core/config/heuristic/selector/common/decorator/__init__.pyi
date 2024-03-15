
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import typing



class SelectionSorterOrder(java.lang.Enum['SelectionSorterOrder']):
    ASCENDING: typing.ClassVar['SelectionSorterOrder'] = ...
    DESCENDING: typing.ClassVar['SelectionSorterOrder'] = ...
    @staticmethod
    def resolve(selectionSorterOrder: 'SelectionSorterOrder') -> 'SelectionSorterOrder': ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'SelectionSorterOrder': ...
    @staticmethod
    def values() -> typing.MutableSequence['SelectionSorterOrder']: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.config.heuristic.selector.common.decorator")``.

    SelectionSorterOrder: typing.Type[SelectionSorterOrder]
