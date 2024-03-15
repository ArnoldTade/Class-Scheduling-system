
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.time
import java.util
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java")``.

    lang: java.lang.__module_protocol__
    time: java.time.__module_protocol__
    util: java.util.__module_protocol__
