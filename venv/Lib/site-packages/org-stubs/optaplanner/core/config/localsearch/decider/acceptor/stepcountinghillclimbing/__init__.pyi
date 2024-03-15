
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import typing



class StepCountingHillClimbingType(java.lang.Enum['StepCountingHillClimbingType']):
    SELECTED_MOVE: typing.ClassVar['StepCountingHillClimbingType'] = ...
    ACCEPTED_MOVE: typing.ClassVar['StepCountingHillClimbingType'] = ...
    STEP: typing.ClassVar['StepCountingHillClimbingType'] = ...
    EQUAL_OR_IMPROVING_STEP: typing.ClassVar['StepCountingHillClimbingType'] = ...
    IMPROVING_STEP: typing.ClassVar['StepCountingHillClimbingType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'StepCountingHillClimbingType': ...
    @staticmethod
    def values() -> typing.MutableSequence['StepCountingHillClimbingType']: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.config.localsearch.decider.acceptor.stepcountinghillclimbing")``.

    StepCountingHillClimbingType: typing.Type[StepCountingHillClimbingType]
