
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.optaplanner.core.api
import org.optaplanner.core.config
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core")``.

    api: org.optaplanner.core.api.__module_protocol__
    config: org.optaplanner.core.config.__module_protocol__
