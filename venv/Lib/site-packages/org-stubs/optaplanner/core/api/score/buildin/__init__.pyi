
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.optaplanner.core.api.score.buildin.bendable
import org.optaplanner.core.api.score.buildin.bendablebigdecimal
import org.optaplanner.core.api.score.buildin.bendablelong
import org.optaplanner.core.api.score.buildin.hardmediumsoft
import org.optaplanner.core.api.score.buildin.hardmediumsoftbigdecimal
import org.optaplanner.core.api.score.buildin.hardmediumsoftlong
import org.optaplanner.core.api.score.buildin.hardsoft
import org.optaplanner.core.api.score.buildin.hardsoftbigdecimal
import org.optaplanner.core.api.score.buildin.hardsoftlong
import org.optaplanner.core.api.score.buildin.simple
import org.optaplanner.core.api.score.buildin.simplebigdecimal
import org.optaplanner.core.api.score.buildin.simplelong
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.api.score.buildin")``.

    bendable: org.optaplanner.core.api.score.buildin.bendable.__module_protocol__
    bendablebigdecimal: org.optaplanner.core.api.score.buildin.bendablebigdecimal.__module_protocol__
    bendablelong: org.optaplanner.core.api.score.buildin.bendablelong.__module_protocol__
    hardmediumsoft: org.optaplanner.core.api.score.buildin.hardmediumsoft.__module_protocol__
    hardmediumsoftbigdecimal: org.optaplanner.core.api.score.buildin.hardmediumsoftbigdecimal.__module_protocol__
    hardmediumsoftlong: org.optaplanner.core.api.score.buildin.hardmediumsoftlong.__module_protocol__
    hardsoft: org.optaplanner.core.api.score.buildin.hardsoft.__module_protocol__
    hardsoftbigdecimal: org.optaplanner.core.api.score.buildin.hardsoftbigdecimal.__module_protocol__
    hardsoftlong: org.optaplanner.core.api.score.buildin.hardsoftlong.__module_protocol__
    simple: org.optaplanner.core.api.score.buildin.simple.__module_protocol__
    simplebigdecimal: org.optaplanner.core.api.score.buildin.simplebigdecimal.__module_protocol__
    simplelong: org.optaplanner.core.api.score.buildin.simplelong.__module_protocol__
