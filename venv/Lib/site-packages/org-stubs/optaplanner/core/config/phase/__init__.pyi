
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util.function
import org.optaplanner.core.config
import org.optaplanner.core.config.phase.custom
import org.optaplanner.core.config.solver.termination
import typing



_PhaseConfig__Config_ = typing.TypeVar('_PhaseConfig__Config_', bound='PhaseConfig')  # <Config_>
class PhaseConfig(org.optaplanner.core.config.AbstractConfig[_PhaseConfig__Config_], typing.Generic[_PhaseConfig__Config_]):
    def __init__(self): ...
    def getTerminationConfig(self) -> org.optaplanner.core.config.solver.termination.TerminationConfig: ...
    def inherit(self, config_: _PhaseConfig__Config_) -> _PhaseConfig__Config_: ...
    def setTerminationConfig(self, terminationConfig: org.optaplanner.core.config.solver.termination.TerminationConfig) -> None: ...
    def toString(self) -> str: ...
    def withTerminationConfig(self, terminationConfig: org.optaplanner.core.config.solver.termination.TerminationConfig) -> _PhaseConfig__Config_: ...

class NoChangePhaseConfig(PhaseConfig['NoChangePhaseConfig']):
    XML_ELEMENT_NAME: typing.ClassVar[str] = ...
    def __init__(self): ...
    def copyConfig(self) -> 'NoChangePhaseConfig': ...
    def inherit(self, noChangePhaseConfig: 'NoChangePhaseConfig') -> 'NoChangePhaseConfig': ...
    def visitReferencedClasses(self, consumer: typing.Union[java.util.function.Consumer[typing.Type[typing.Any]], typing.Callable[[typing.Type[typing.Any]], None]]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.config.phase")``.

    NoChangePhaseConfig: typing.Type[NoChangePhaseConfig]
    PhaseConfig: typing.Type[PhaseConfig]
    custom: org.optaplanner.core.config.phase.custom.__module_protocol__
