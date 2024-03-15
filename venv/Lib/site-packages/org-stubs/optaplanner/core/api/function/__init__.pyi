
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import typing



_PentaFunction__A = typing.TypeVar('_PentaFunction__A')  # <A>
_PentaFunction__B = typing.TypeVar('_PentaFunction__B')  # <B>
_PentaFunction__C = typing.TypeVar('_PentaFunction__C')  # <C>
_PentaFunction__D = typing.TypeVar('_PentaFunction__D')  # <D>
_PentaFunction__E = typing.TypeVar('_PentaFunction__E')  # <E>
_PentaFunction__R = typing.TypeVar('_PentaFunction__R')  # <R>
class PentaFunction(typing.Generic[_PentaFunction__A, _PentaFunction__B, _PentaFunction__C, _PentaFunction__D, _PentaFunction__E, _PentaFunction__R]):
    def apply(self, a: _PentaFunction__A, b: _PentaFunction__B, c: _PentaFunction__C, d: _PentaFunction__D, e: _PentaFunction__E) -> _PentaFunction__R: ...

_PentaPredicate__A = typing.TypeVar('_PentaPredicate__A')  # <A>
_PentaPredicate__B = typing.TypeVar('_PentaPredicate__B')  # <B>
_PentaPredicate__C = typing.TypeVar('_PentaPredicate__C')  # <C>
_PentaPredicate__D = typing.TypeVar('_PentaPredicate__D')  # <D>
_PentaPredicate__E = typing.TypeVar('_PentaPredicate__E')  # <E>
class PentaPredicate(typing.Generic[_PentaPredicate__A, _PentaPredicate__B, _PentaPredicate__C, _PentaPredicate__D, _PentaPredicate__E]):
    def and_(self, pentaPredicate: typing.Union['PentaPredicate'[_PentaPredicate__A, _PentaPredicate__B, _PentaPredicate__C, _PentaPredicate__D, _PentaPredicate__E], typing.Callable[[_PentaPredicate__A, _PentaPredicate__B, _PentaPredicate__C, _PentaPredicate__D, _PentaPredicate__E], bool]]) -> 'PentaPredicate'[_PentaPredicate__A, _PentaPredicate__B, _PentaPredicate__C, _PentaPredicate__D, _PentaPredicate__E]: ...
    def negate(self) -> 'PentaPredicate'[_PentaPredicate__A, _PentaPredicate__B, _PentaPredicate__C, _PentaPredicate__D, _PentaPredicate__E]: ...
    def or_(self, pentaPredicate: typing.Union['PentaPredicate'[_PentaPredicate__A, _PentaPredicate__B, _PentaPredicate__C, _PentaPredicate__D, _PentaPredicate__E], typing.Callable[[_PentaPredicate__A, _PentaPredicate__B, _PentaPredicate__C, _PentaPredicate__D, _PentaPredicate__E], bool]]) -> 'PentaPredicate'[_PentaPredicate__A, _PentaPredicate__B, _PentaPredicate__C, _PentaPredicate__D, _PentaPredicate__E]: ...
    def test(self, a: _PentaPredicate__A, b: _PentaPredicate__B, c: _PentaPredicate__C, d: _PentaPredicate__D, e: _PentaPredicate__E) -> bool: ...

_QuadFunction__A = typing.TypeVar('_QuadFunction__A')  # <A>
_QuadFunction__B = typing.TypeVar('_QuadFunction__B')  # <B>
_QuadFunction__C = typing.TypeVar('_QuadFunction__C')  # <C>
_QuadFunction__D = typing.TypeVar('_QuadFunction__D')  # <D>
_QuadFunction__R = typing.TypeVar('_QuadFunction__R')  # <R>
class QuadFunction(typing.Generic[_QuadFunction__A, _QuadFunction__B, _QuadFunction__C, _QuadFunction__D, _QuadFunction__R]):
    def apply(self, a: _QuadFunction__A, b: _QuadFunction__B, c: _QuadFunction__C, d: _QuadFunction__D) -> _QuadFunction__R: ...

_QuadPredicate__A = typing.TypeVar('_QuadPredicate__A')  # <A>
_QuadPredicate__B = typing.TypeVar('_QuadPredicate__B')  # <B>
_QuadPredicate__C = typing.TypeVar('_QuadPredicate__C')  # <C>
_QuadPredicate__D = typing.TypeVar('_QuadPredicate__D')  # <D>
class QuadPredicate(typing.Generic[_QuadPredicate__A, _QuadPredicate__B, _QuadPredicate__C, _QuadPredicate__D]):
    def and_(self, quadPredicate: typing.Union['QuadPredicate'[_QuadPredicate__A, _QuadPredicate__B, _QuadPredicate__C, _QuadPredicate__D], typing.Callable[[_QuadPredicate__A, _QuadPredicate__B, _QuadPredicate__C, _QuadPredicate__D], bool]]) -> 'QuadPredicate'[_QuadPredicate__A, _QuadPredicate__B, _QuadPredicate__C, _QuadPredicate__D]: ...
    def negate(self) -> 'QuadPredicate'[_QuadPredicate__A, _QuadPredicate__B, _QuadPredicate__C, _QuadPredicate__D]: ...
    def or_(self, quadPredicate: typing.Union['QuadPredicate'[_QuadPredicate__A, _QuadPredicate__B, _QuadPredicate__C, _QuadPredicate__D], typing.Callable[[_QuadPredicate__A, _QuadPredicate__B, _QuadPredicate__C, _QuadPredicate__D], bool]]) -> 'QuadPredicate'[_QuadPredicate__A, _QuadPredicate__B, _QuadPredicate__C, _QuadPredicate__D]: ...
    def test(self, a: _QuadPredicate__A, b: _QuadPredicate__B, c: _QuadPredicate__C, d: _QuadPredicate__D) -> bool: ...

_ToIntQuadFunction__A = typing.TypeVar('_ToIntQuadFunction__A')  # <A>
_ToIntQuadFunction__B = typing.TypeVar('_ToIntQuadFunction__B')  # <B>
_ToIntQuadFunction__C = typing.TypeVar('_ToIntQuadFunction__C')  # <C>
_ToIntQuadFunction__D = typing.TypeVar('_ToIntQuadFunction__D')  # <D>
class ToIntQuadFunction(typing.Generic[_ToIntQuadFunction__A, _ToIntQuadFunction__B, _ToIntQuadFunction__C, _ToIntQuadFunction__D]):
    def applyAsInt(self, a: _ToIntQuadFunction__A, b: _ToIntQuadFunction__B, c: _ToIntQuadFunction__C, d: _ToIntQuadFunction__D) -> int: ...

_ToIntTriFunction__A = typing.TypeVar('_ToIntTriFunction__A')  # <A>
_ToIntTriFunction__B = typing.TypeVar('_ToIntTriFunction__B')  # <B>
_ToIntTriFunction__C = typing.TypeVar('_ToIntTriFunction__C')  # <C>
class ToIntTriFunction(typing.Generic[_ToIntTriFunction__A, _ToIntTriFunction__B, _ToIntTriFunction__C]):
    def applyAsInt(self, a: _ToIntTriFunction__A, b: _ToIntTriFunction__B, c: _ToIntTriFunction__C) -> int: ...

_ToLongQuadFunction__A = typing.TypeVar('_ToLongQuadFunction__A')  # <A>
_ToLongQuadFunction__B = typing.TypeVar('_ToLongQuadFunction__B')  # <B>
_ToLongQuadFunction__C = typing.TypeVar('_ToLongQuadFunction__C')  # <C>
_ToLongQuadFunction__D = typing.TypeVar('_ToLongQuadFunction__D')  # <D>
class ToLongQuadFunction(typing.Generic[_ToLongQuadFunction__A, _ToLongQuadFunction__B, _ToLongQuadFunction__C, _ToLongQuadFunction__D]):
    def applyAsLong(self, a: _ToLongQuadFunction__A, b: _ToLongQuadFunction__B, c: _ToLongQuadFunction__C, d: _ToLongQuadFunction__D) -> int: ...

_ToLongTriFunction__A = typing.TypeVar('_ToLongTriFunction__A')  # <A>
_ToLongTriFunction__B = typing.TypeVar('_ToLongTriFunction__B')  # <B>
_ToLongTriFunction__C = typing.TypeVar('_ToLongTriFunction__C')  # <C>
class ToLongTriFunction(typing.Generic[_ToLongTriFunction__A, _ToLongTriFunction__B, _ToLongTriFunction__C]):
    def applyAsLong(self, a: _ToLongTriFunction__A, b: _ToLongTriFunction__B, c: _ToLongTriFunction__C) -> int: ...

_TriConsumer__A = typing.TypeVar('_TriConsumer__A')  # <A>
_TriConsumer__B = typing.TypeVar('_TriConsumer__B')  # <B>
_TriConsumer__C = typing.TypeVar('_TriConsumer__C')  # <C>
class TriConsumer(typing.Generic[_TriConsumer__A, _TriConsumer__B, _TriConsumer__C]):
    def accept(self, a: _TriConsumer__A, b: _TriConsumer__B, c: _TriConsumer__C) -> None: ...
    def andThen(self, triConsumer: typing.Union['TriConsumer'[_TriConsumer__A, _TriConsumer__B, _TriConsumer__C], typing.Callable[[_TriConsumer__A, _TriConsumer__B, _TriConsumer__C], None]]) -> 'TriConsumer'[_TriConsumer__A, _TriConsumer__B, _TriConsumer__C]: ...

_TriFunction__A = typing.TypeVar('_TriFunction__A')  # <A>
_TriFunction__B = typing.TypeVar('_TriFunction__B')  # <B>
_TriFunction__C = typing.TypeVar('_TriFunction__C')  # <C>
_TriFunction__R = typing.TypeVar('_TriFunction__R')  # <R>
class TriFunction(typing.Generic[_TriFunction__A, _TriFunction__B, _TriFunction__C, _TriFunction__R]):
    def apply(self, a: _TriFunction__A, b: _TriFunction__B, c: _TriFunction__C) -> _TriFunction__R: ...

_TriPredicate__A = typing.TypeVar('_TriPredicate__A')  # <A>
_TriPredicate__B = typing.TypeVar('_TriPredicate__B')  # <B>
_TriPredicate__C = typing.TypeVar('_TriPredicate__C')  # <C>
class TriPredicate(typing.Generic[_TriPredicate__A, _TriPredicate__B, _TriPredicate__C]):
    def and_(self, triPredicate: typing.Union['TriPredicate'[_TriPredicate__A, _TriPredicate__B, _TriPredicate__C], typing.Callable[[_TriPredicate__A, _TriPredicate__B, _TriPredicate__C], bool]]) -> 'TriPredicate'[_TriPredicate__A, _TriPredicate__B, _TriPredicate__C]: ...
    def negate(self) -> 'TriPredicate'[_TriPredicate__A, _TriPredicate__B, _TriPredicate__C]: ...
    def or_(self, triPredicate: typing.Union['TriPredicate'[_TriPredicate__A, _TriPredicate__B, _TriPredicate__C], typing.Callable[[_TriPredicate__A, _TriPredicate__B, _TriPredicate__C], bool]]) -> 'TriPredicate'[_TriPredicate__A, _TriPredicate__B, _TriPredicate__C]: ...
    def test(self, a: _TriPredicate__A, b: _TriPredicate__B, c: _TriPredicate__C) -> bool: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.api.function")``.

    PentaFunction: typing.Type[PentaFunction]
    PentaPredicate: typing.Type[PentaPredicate]
    QuadFunction: typing.Type[QuadFunction]
    QuadPredicate: typing.Type[QuadPredicate]
    ToIntQuadFunction: typing.Type[ToIntQuadFunction]
    ToIntTriFunction: typing.Type[ToIntTriFunction]
    ToLongQuadFunction: typing.Type[ToLongQuadFunction]
    ToLongTriFunction: typing.Type[ToLongTriFunction]
    TriConsumer: typing.Type[TriConsumer]
    TriFunction: typing.Type[TriFunction]
    TriPredicate: typing.Type[TriPredicate]
