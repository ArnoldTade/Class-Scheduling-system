
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util.function
import org.optaplanner.core.config.constructionheuristic
import org.optaplanner.core.config.exhaustivesearch
import org.optaplanner.core.config.heuristic
import org.optaplanner.core.config.localsearch
import org.optaplanner.core.config.partitionedsearch
import org.optaplanner.core.config.phase
import org.optaplanner.core.config.score
import org.optaplanner.core.config.solver
import org.optaplanner.core.config.util
import typing



_AbstractConfig__Config_ = typing.TypeVar('_AbstractConfig__Config_', bound='AbstractConfig')  # <Config_>
class AbstractConfig(typing.Generic[_AbstractConfig__Config_]):
    def __init__(self): ...
    def copyConfig(self) -> _AbstractConfig__Config_: ...
    def inherit(self, config_: _AbstractConfig__Config_) -> _AbstractConfig__Config_: ...
    def toString(self) -> str: ...
    def visitReferencedClasses(self, consumer: typing.Union[java.util.function.Consumer[typing.Type[typing.Any]], typing.Callable[[typing.Type[typing.Any]], None]]) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.config")``.

    AbstractConfig: typing.Type[AbstractConfig]
    constructionheuristic: org.optaplanner.core.config.constructionheuristic.__module_protocol__
    exhaustivesearch: org.optaplanner.core.config.exhaustivesearch.__module_protocol__
    heuristic: org.optaplanner.core.config.heuristic.__module_protocol__
    localsearch: org.optaplanner.core.config.localsearch.__module_protocol__
    partitionedsearch: org.optaplanner.core.config.partitionedsearch.__module_protocol__
    phase: org.optaplanner.core.config.phase.__module_protocol__
    score: org.optaplanner.core.config.score.__module_protocol__
    solver: org.optaplanner.core.config.solver.__module_protocol__
    util: org.optaplanner.core.config.util.__module_protocol__
