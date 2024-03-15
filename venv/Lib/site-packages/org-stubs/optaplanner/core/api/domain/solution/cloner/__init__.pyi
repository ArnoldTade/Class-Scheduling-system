
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang.annotation
import typing



class DeepPlanningClone(java.lang.annotation.Annotation):
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    def toString(self) -> str: ...

_SolutionCloner__Solution_ = typing.TypeVar('_SolutionCloner__Solution_')  # <Solution_>
class SolutionCloner(typing.Generic[_SolutionCloner__Solution_]):
    def cloneSolution(self, solution_: _SolutionCloner__Solution_) -> _SolutionCloner__Solution_: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.api.domain.solution.cloner")``.

    DeepPlanningClone: typing.Type[DeepPlanningClone]
    SolutionCloner: typing.Type[SolutionCloner]
