
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import typing



class AutoDiscoverMemberType(java.lang.Enum['AutoDiscoverMemberType']):
    NONE: typing.ClassVar['AutoDiscoverMemberType'] = ...
    FIELD: typing.ClassVar['AutoDiscoverMemberType'] = ...
    GETTER: typing.ClassVar['AutoDiscoverMemberType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AutoDiscoverMemberType': ...
    @staticmethod
    def values() -> typing.MutableSequence['AutoDiscoverMemberType']: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.api.domain.autodiscover")``.

    AutoDiscoverMemberType: typing.Type[AutoDiscoverMemberType]
