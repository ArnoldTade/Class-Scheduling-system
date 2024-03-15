
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.optaplanner.core.api.domain
import org.optaplanner.core.api.function
import org.optaplanner.core.api.score
import org.optaplanner.core.api.solver
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.api")``.

    domain: org.optaplanner.core.api.domain.__module_protocol__
    function: org.optaplanner.core.api.function.__module_protocol__
    score: org.optaplanner.core.api.score.__module_protocol__
    solver: org.optaplanner.core.api.solver.__module_protocol__
