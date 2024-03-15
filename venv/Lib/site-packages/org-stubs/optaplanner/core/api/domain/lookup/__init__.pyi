
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.lang.annotation
import typing



class LookUpStrategyType(java.lang.Enum['LookUpStrategyType']):
    PLANNING_ID_OR_NONE: typing.ClassVar['LookUpStrategyType'] = ...
    PLANNING_ID_OR_FAIL_FAST: typing.ClassVar['LookUpStrategyType'] = ...
    EQUALITY: typing.ClassVar['LookUpStrategyType'] = ...
    NONE: typing.ClassVar['LookUpStrategyType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LookUpStrategyType': ...
    @staticmethod
    def values() -> typing.MutableSequence['LookUpStrategyType']: ...

class PlanningId(java.lang.annotation.Annotation):
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.api.domain.lookup")``.

    LookUpStrategyType: typing.Type[LookUpStrategyType]
    PlanningId: typing.Type[PlanningId]
