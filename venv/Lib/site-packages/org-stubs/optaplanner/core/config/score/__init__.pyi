
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.optaplanner.core.config.score.definition
import org.optaplanner.core.config.score.director
import org.optaplanner.core.config.score.trend
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.config.score")``.

    definition: org.optaplanner.core.config.score.definition.__module_protocol__
    director: org.optaplanner.core.config.score.director.__module_protocol__
    trend: org.optaplanner.core.config.score.trend.__module_protocol__
