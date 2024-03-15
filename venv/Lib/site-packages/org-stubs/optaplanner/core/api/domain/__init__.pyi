
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.optaplanner.core.api.domain.autodiscover
import org.optaplanner.core.api.domain.common
import org.optaplanner.core.api.domain.constraintweight
import org.optaplanner.core.api.domain.entity
import org.optaplanner.core.api.domain.lookup
import org.optaplanner.core.api.domain.solution
import org.optaplanner.core.api.domain.valuerange
import org.optaplanner.core.api.domain.variable
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.api.domain")``.

    autodiscover: org.optaplanner.core.api.domain.autodiscover.__module_protocol__
    common: org.optaplanner.core.api.domain.common.__module_protocol__
    constraintweight: org.optaplanner.core.api.domain.constraintweight.__module_protocol__
    entity: org.optaplanner.core.api.domain.entity.__module_protocol__
    lookup: org.optaplanner.core.api.domain.lookup.__module_protocol__
    solution: org.optaplanner.core.api.domain.solution.__module_protocol__
    valuerange: org.optaplanner.core.api.domain.valuerange.__module_protocol__
    variable: org.optaplanner.core.api.domain.variable.__module_protocol__
