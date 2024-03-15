
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import typing



class InitializingScoreTrendLevel(java.lang.Enum['InitializingScoreTrendLevel']):
    ANY: typing.ClassVar['InitializingScoreTrendLevel'] = ...
    ONLY_UP: typing.ClassVar['InitializingScoreTrendLevel'] = ...
    ONLY_DOWN: typing.ClassVar['InitializingScoreTrendLevel'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'InitializingScoreTrendLevel': ...
    @staticmethod
    def values() -> typing.MutableSequence['InitializingScoreTrendLevel']: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.config.score.trend")``.

    InitializingScoreTrendLevel: typing.Type[InitializingScoreTrendLevel]
