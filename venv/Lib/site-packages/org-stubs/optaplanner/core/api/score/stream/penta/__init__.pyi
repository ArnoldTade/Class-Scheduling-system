
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import typing



_PentaJoiner__A = typing.TypeVar('_PentaJoiner__A')  # <A>
_PentaJoiner__B = typing.TypeVar('_PentaJoiner__B')  # <B>
_PentaJoiner__C = typing.TypeVar('_PentaJoiner__C')  # <C>
_PentaJoiner__D = typing.TypeVar('_PentaJoiner__D')  # <D>
_PentaJoiner__E = typing.TypeVar('_PentaJoiner__E')  # <E>
class PentaJoiner(typing.Generic[_PentaJoiner__A, _PentaJoiner__B, _PentaJoiner__C, _PentaJoiner__D, _PentaJoiner__E]):
    def and_(self, pentaJoiner: 'PentaJoiner'[_PentaJoiner__A, _PentaJoiner__B, _PentaJoiner__C, _PentaJoiner__D, _PentaJoiner__E]) -> 'PentaJoiner'[_PentaJoiner__A, _PentaJoiner__B, _PentaJoiner__C, _PentaJoiner__D, _PentaJoiner__E]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.api.score.stream.penta")``.

    PentaJoiner: typing.Type[PentaJoiner]
