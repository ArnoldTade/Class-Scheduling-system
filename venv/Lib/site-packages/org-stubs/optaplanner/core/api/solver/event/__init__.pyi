
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.optaplanner.core.api.score
import org.optaplanner.core.api.solver
import typing



_BestSolutionChangedEvent__Solution_ = typing.TypeVar('_BestSolutionChangedEvent__Solution_')  # <Solution_>
class BestSolutionChangedEvent(java.util.EventObject, typing.Generic[_BestSolutionChangedEvent__Solution_]):
    def __init__(self, solver: org.optaplanner.core.api.solver.Solver[_BestSolutionChangedEvent__Solution_], long: int, solution_: _BestSolutionChangedEvent__Solution_, score: org.optaplanner.core.api.score.Score): ...
    def getNewBestScore(self) -> org.optaplanner.core.api.score.Score: ...
    def getNewBestSolution(self) -> _BestSolutionChangedEvent__Solution_: ...
    def getTimeMillisSpent(self) -> int: ...
    def isEveryProblemChangeProcessed(self) -> bool: ...
    def isEveryProblemFactChangeProcessed(self) -> bool: ...

_SolverEventListener__Solution_ = typing.TypeVar('_SolverEventListener__Solution_')  # <Solution_>
class SolverEventListener(java.util.EventListener, typing.Generic[_SolverEventListener__Solution_]):
    def bestSolutionChanged(self, bestSolutionChangedEvent: BestSolutionChangedEvent[_SolverEventListener__Solution_]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.api.solver.event")``.

    BestSolutionChangedEvent: typing.Type[BestSolutionChangedEvent]
    SolverEventListener: typing.Type[SolverEventListener]
