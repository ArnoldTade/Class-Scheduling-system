
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.optaplanner.core.config.localsearch.decider.acceptor
import org.optaplanner.core.config.localsearch.decider.forager
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.config.localsearch.decider")``.

    acceptor: org.optaplanner.core.config.localsearch.decider.acceptor.__module_protocol__
    forager: org.optaplanner.core.config.localsearch.decider.forager.__module_protocol__
