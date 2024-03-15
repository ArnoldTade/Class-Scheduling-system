
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import java.util.function
import typing



_ProblemChange__Solution_ = typing.TypeVar('_ProblemChange__Solution_')  # <Solution_>
class ProblemChange(typing.Generic[_ProblemChange__Solution_]):
    def doChange(self, solution_: _ProblemChange__Solution_, problemChangeDirector: 'ProblemChangeDirector') -> None: ...

class ProblemChangeDirector:
    _addEntity__Entity = typing.TypeVar('_addEntity__Entity')  # <Entity>
    def addEntity(self, entity: _addEntity__Entity, consumer: typing.Union[java.util.function.Consumer[_addEntity__Entity], typing.Callable[[_addEntity__Entity], None]]) -> None: ...
    _addProblemFact__ProblemFact = typing.TypeVar('_addProblemFact__ProblemFact')  # <ProblemFact>
    def addProblemFact(self, problemFact: _addProblemFact__ProblemFact, consumer: typing.Union[java.util.function.Consumer[_addProblemFact__ProblemFact], typing.Callable[[_addProblemFact__ProblemFact], None]]) -> None: ...
    _changeProblemProperty__EntityOrProblemFact = typing.TypeVar('_changeProblemProperty__EntityOrProblemFact')  # <EntityOrProblemFact>
    def changeProblemProperty(self, entityOrProblemFact: _changeProblemProperty__EntityOrProblemFact, consumer: typing.Union[java.util.function.Consumer[_changeProblemProperty__EntityOrProblemFact], typing.Callable[[_changeProblemProperty__EntityOrProblemFact], None]]) -> None: ...
    _changeVariable__Entity = typing.TypeVar('_changeVariable__Entity')  # <Entity>
    def changeVariable(self, entity: _changeVariable__Entity, string: str, consumer: typing.Union[java.util.function.Consumer[_changeVariable__Entity], typing.Callable[[_changeVariable__Entity], None]]) -> None: ...
    _lookUpWorkingObject__EntityOrProblemFact = typing.TypeVar('_lookUpWorkingObject__EntityOrProblemFact')  # <EntityOrProblemFact>
    def lookUpWorkingObject(self, entityOrProblemFact: _lookUpWorkingObject__EntityOrProblemFact) -> java.util.Optional[_lookUpWorkingObject__EntityOrProblemFact]: ...
    _lookUpWorkingObjectOrFail__EntityOrProblemFact = typing.TypeVar('_lookUpWorkingObjectOrFail__EntityOrProblemFact')  # <EntityOrProblemFact>
    def lookUpWorkingObjectOrFail(self, entityOrProblemFact: _lookUpWorkingObjectOrFail__EntityOrProblemFact) -> _lookUpWorkingObjectOrFail__EntityOrProblemFact: ...
    _removeEntity__Entity = typing.TypeVar('_removeEntity__Entity')  # <Entity>
    def removeEntity(self, entity: _removeEntity__Entity, consumer: typing.Union[java.util.function.Consumer[_removeEntity__Entity], typing.Callable[[_removeEntity__Entity], None]]) -> None: ...
    _removeProblemFact__ProblemFact = typing.TypeVar('_removeProblemFact__ProblemFact')  # <ProblemFact>
    def removeProblemFact(self, problemFact: _removeProblemFact__ProblemFact, consumer: typing.Union[java.util.function.Consumer[_removeProblemFact__ProblemFact], typing.Callable[[_removeProblemFact__ProblemFact], None]]) -> None: ...
    def updateShadowVariables(self) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.api.solver.change")``.

    ProblemChange: typing.Type[ProblemChange]
    ProblemChangeDirector: typing.Type[ProblemChangeDirector]
