
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import decimal
import java.lang
import java.math
import java.time
import java.util
import java.util.function
import org.optaplanner.core.api.function
import org.optaplanner.core.api.score
import org.optaplanner.core.api.score.stream.bi
import org.optaplanner.core.api.score.stream.penta
import org.optaplanner.core.api.score.stream.quad
import org.optaplanner.core.api.score.stream.tri
import org.optaplanner.core.api.score.stream.uni
import typing



class Constraint:
    def getConstraintFactory(self) -> 'ConstraintFactory': ...
    def getConstraintId(self) -> str: ...
    def getConstraintName(self) -> str: ...
    def getConstraintPackage(self) -> str: ...

class ConstraintBuilder:
    @typing.overload
    def asConstraint(self, string: str) -> Constraint: ...
    @typing.overload
    def asConstraint(self, string: str, string2: str) -> Constraint: ...

class ConstraintCollectors:
    _average_0__A = typing.TypeVar('_average_0__A')  # <A>
    _average_0__B = typing.TypeVar('_average_0__B')  # <B>
    _average_1__A = typing.TypeVar('_average_1__A')  # <A>
    _average_1__B = typing.TypeVar('_average_1__B')  # <B>
    _average_1__C = typing.TypeVar('_average_1__C')  # <C>
    _average_1__D = typing.TypeVar('_average_1__D')  # <D>
    _average_2__A = typing.TypeVar('_average_2__A')  # <A>
    _average_2__B = typing.TypeVar('_average_2__B')  # <B>
    _average_2__C = typing.TypeVar('_average_2__C')  # <C>
    _average_3__A = typing.TypeVar('_average_3__A')  # <A>
    @typing.overload
    @staticmethod
    def average(toIntBiFunction: typing.Union[java.util.function.ToIntBiFunction[_average_0__A, _average_0__B], typing.Callable[[_average_0__A, _average_0__B], int]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_average_0__A, _average_0__B, typing.Any, float]: ...
    @typing.overload
    @staticmethod
    def average(toIntQuadFunction: typing.Union[org.optaplanner.core.api.function.ToIntQuadFunction[_average_1__A, _average_1__B, _average_1__C, _average_1__D], typing.Callable[[_average_1__A, _average_1__B, _average_1__C, _average_1__D], int]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_average_1__A, _average_1__B, _average_1__C, _average_1__D, typing.Any, float]: ...
    @typing.overload
    @staticmethod
    def average(toIntTriFunction: typing.Union[org.optaplanner.core.api.function.ToIntTriFunction[_average_2__A, _average_2__B, _average_2__C], typing.Callable[[_average_2__A, _average_2__B, _average_2__C], int]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_average_2__A, _average_2__B, _average_2__C, typing.Any, float]: ...
    @typing.overload
    @staticmethod
    def average(toIntFunction: typing.Union[java.util.function.ToIntFunction[_average_3__A], typing.Callable[[_average_3__A], int]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_average_3__A, typing.Any, float]: ...
    _averageBigDecimal_0__A = typing.TypeVar('_averageBigDecimal_0__A')  # <A>
    _averageBigDecimal_0__B = typing.TypeVar('_averageBigDecimal_0__B')  # <B>
    _averageBigDecimal_1__A = typing.TypeVar('_averageBigDecimal_1__A')  # <A>
    _averageBigDecimal_1__B = typing.TypeVar('_averageBigDecimal_1__B')  # <B>
    _averageBigDecimal_1__C = typing.TypeVar('_averageBigDecimal_1__C')  # <C>
    _averageBigDecimal_1__D = typing.TypeVar('_averageBigDecimal_1__D')  # <D>
    _averageBigDecimal_2__A = typing.TypeVar('_averageBigDecimal_2__A')  # <A>
    _averageBigDecimal_2__B = typing.TypeVar('_averageBigDecimal_2__B')  # <B>
    _averageBigDecimal_2__C = typing.TypeVar('_averageBigDecimal_2__C')  # <C>
    _averageBigDecimal_3__A = typing.TypeVar('_averageBigDecimal_3__A')  # <A>
    @typing.overload
    @staticmethod
    def averageBigDecimal(biFunction: typing.Union[java.util.function.BiFunction[_averageBigDecimal_0__A, _averageBigDecimal_0__B, typing.Union[java.math.BigDecimal, decimal.Decimal]], typing.Callable[[_averageBigDecimal_0__A, _averageBigDecimal_0__B], typing.Union[java.math.BigDecimal, decimal.Decimal]]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_averageBigDecimal_0__A, _averageBigDecimal_0__B, typing.Any, java.math.BigDecimal]: ...
    @typing.overload
    @staticmethod
    def averageBigDecimal(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_averageBigDecimal_1__A, _averageBigDecimal_1__B, _averageBigDecimal_1__C, _averageBigDecimal_1__D, typing.Union[java.math.BigDecimal, decimal.Decimal]], typing.Callable[[_averageBigDecimal_1__A, _averageBigDecimal_1__B, _averageBigDecimal_1__C, _averageBigDecimal_1__D], typing.Union[java.math.BigDecimal, decimal.Decimal]]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_averageBigDecimal_1__A, _averageBigDecimal_1__B, _averageBigDecimal_1__C, _averageBigDecimal_1__D, typing.Any, java.math.BigDecimal]: ...
    @typing.overload
    @staticmethod
    def averageBigDecimal(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_averageBigDecimal_2__A, _averageBigDecimal_2__B, _averageBigDecimal_2__C, typing.Union[java.math.BigDecimal, decimal.Decimal]], typing.Callable[[_averageBigDecimal_2__A, _averageBigDecimal_2__B, _averageBigDecimal_2__C], typing.Union[java.math.BigDecimal, decimal.Decimal]]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_averageBigDecimal_2__A, _averageBigDecimal_2__B, _averageBigDecimal_2__C, typing.Any, java.math.BigDecimal]: ...
    @typing.overload
    @staticmethod
    def averageBigDecimal(function: typing.Union[java.util.function.Function[_averageBigDecimal_3__A, typing.Union[java.math.BigDecimal, decimal.Decimal]], typing.Callable[[_averageBigDecimal_3__A], typing.Union[java.math.BigDecimal, decimal.Decimal]]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_averageBigDecimal_3__A, typing.Any, java.math.BigDecimal]: ...
    _averageBigInteger_0__A = typing.TypeVar('_averageBigInteger_0__A')  # <A>
    _averageBigInteger_0__B = typing.TypeVar('_averageBigInteger_0__B')  # <B>
    _averageBigInteger_1__A = typing.TypeVar('_averageBigInteger_1__A')  # <A>
    _averageBigInteger_1__B = typing.TypeVar('_averageBigInteger_1__B')  # <B>
    _averageBigInteger_1__C = typing.TypeVar('_averageBigInteger_1__C')  # <C>
    _averageBigInteger_1__D = typing.TypeVar('_averageBigInteger_1__D')  # <D>
    _averageBigInteger_2__A = typing.TypeVar('_averageBigInteger_2__A')  # <A>
    _averageBigInteger_2__B = typing.TypeVar('_averageBigInteger_2__B')  # <B>
    _averageBigInteger_2__C = typing.TypeVar('_averageBigInteger_2__C')  # <C>
    _averageBigInteger_3__A = typing.TypeVar('_averageBigInteger_3__A')  # <A>
    @typing.overload
    @staticmethod
    def averageBigInteger(biFunction: typing.Union[java.util.function.BiFunction[_averageBigInteger_0__A, _averageBigInteger_0__B, java.math.BigInteger], typing.Callable[[_averageBigInteger_0__A, _averageBigInteger_0__B], java.math.BigInteger]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_averageBigInteger_0__A, _averageBigInteger_0__B, typing.Any, java.math.BigDecimal]: ...
    @typing.overload
    @staticmethod
    def averageBigInteger(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_averageBigInteger_1__A, _averageBigInteger_1__B, _averageBigInteger_1__C, _averageBigInteger_1__D, java.math.BigInteger], typing.Callable[[_averageBigInteger_1__A, _averageBigInteger_1__B, _averageBigInteger_1__C, _averageBigInteger_1__D], java.math.BigInteger]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_averageBigInteger_1__A, _averageBigInteger_1__B, _averageBigInteger_1__C, _averageBigInteger_1__D, typing.Any, java.math.BigDecimal]: ...
    @typing.overload
    @staticmethod
    def averageBigInteger(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_averageBigInteger_2__A, _averageBigInteger_2__B, _averageBigInteger_2__C, java.math.BigInteger], typing.Callable[[_averageBigInteger_2__A, _averageBigInteger_2__B, _averageBigInteger_2__C], java.math.BigInteger]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_averageBigInteger_2__A, _averageBigInteger_2__B, _averageBigInteger_2__C, typing.Any, java.math.BigDecimal]: ...
    @typing.overload
    @staticmethod
    def averageBigInteger(function: typing.Union[java.util.function.Function[_averageBigInteger_3__A, java.math.BigInteger], typing.Callable[[_averageBigInteger_3__A], java.math.BigInteger]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_averageBigInteger_3__A, typing.Any, java.math.BigDecimal]: ...
    _averageDuration_0__A = typing.TypeVar('_averageDuration_0__A')  # <A>
    _averageDuration_0__B = typing.TypeVar('_averageDuration_0__B')  # <B>
    _averageDuration_1__A = typing.TypeVar('_averageDuration_1__A')  # <A>
    _averageDuration_1__B = typing.TypeVar('_averageDuration_1__B')  # <B>
    _averageDuration_1__C = typing.TypeVar('_averageDuration_1__C')  # <C>
    _averageDuration_1__D = typing.TypeVar('_averageDuration_1__D')  # <D>
    _averageDuration_2__A = typing.TypeVar('_averageDuration_2__A')  # <A>
    _averageDuration_2__B = typing.TypeVar('_averageDuration_2__B')  # <B>
    _averageDuration_2__C = typing.TypeVar('_averageDuration_2__C')  # <C>
    _averageDuration_3__A = typing.TypeVar('_averageDuration_3__A')  # <A>
    @typing.overload
    @staticmethod
    def averageDuration(biFunction: typing.Union[java.util.function.BiFunction[_averageDuration_0__A, _averageDuration_0__B, java.time.Duration], typing.Callable[[_averageDuration_0__A, _averageDuration_0__B], java.time.Duration]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_averageDuration_0__A, _averageDuration_0__B, typing.Any, java.time.Duration]: ...
    @typing.overload
    @staticmethod
    def averageDuration(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_averageDuration_1__A, _averageDuration_1__B, _averageDuration_1__C, _averageDuration_1__D, java.time.Duration], typing.Callable[[_averageDuration_1__A, _averageDuration_1__B, _averageDuration_1__C, _averageDuration_1__D], java.time.Duration]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_averageDuration_1__A, _averageDuration_1__B, _averageDuration_1__C, _averageDuration_1__D, typing.Any, java.time.Duration]: ...
    @typing.overload
    @staticmethod
    def averageDuration(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_averageDuration_2__A, _averageDuration_2__B, _averageDuration_2__C, java.time.Duration], typing.Callable[[_averageDuration_2__A, _averageDuration_2__B, _averageDuration_2__C], java.time.Duration]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_averageDuration_2__A, _averageDuration_2__B, _averageDuration_2__C, typing.Any, java.time.Duration]: ...
    @typing.overload
    @staticmethod
    def averageDuration(function: typing.Union[java.util.function.Function[_averageDuration_3__A, java.time.Duration], typing.Callable[[_averageDuration_3__A], java.time.Duration]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_averageDuration_3__A, typing.Any, java.time.Duration]: ...
    _averageLong_0__A = typing.TypeVar('_averageLong_0__A')  # <A>
    _averageLong_0__B = typing.TypeVar('_averageLong_0__B')  # <B>
    _averageLong_1__A = typing.TypeVar('_averageLong_1__A')  # <A>
    _averageLong_1__B = typing.TypeVar('_averageLong_1__B')  # <B>
    _averageLong_1__C = typing.TypeVar('_averageLong_1__C')  # <C>
    _averageLong_1__D = typing.TypeVar('_averageLong_1__D')  # <D>
    _averageLong_2__A = typing.TypeVar('_averageLong_2__A')  # <A>
    _averageLong_2__B = typing.TypeVar('_averageLong_2__B')  # <B>
    _averageLong_2__C = typing.TypeVar('_averageLong_2__C')  # <C>
    _averageLong_3__A = typing.TypeVar('_averageLong_3__A')  # <A>
    @typing.overload
    @staticmethod
    def averageLong(toLongBiFunction: typing.Union[java.util.function.ToLongBiFunction[_averageLong_0__A, _averageLong_0__B], typing.Callable[[_averageLong_0__A, _averageLong_0__B], int]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_averageLong_0__A, _averageLong_0__B, typing.Any, float]: ...
    @typing.overload
    @staticmethod
    def averageLong(toLongQuadFunction: typing.Union[org.optaplanner.core.api.function.ToLongQuadFunction[_averageLong_1__A, _averageLong_1__B, _averageLong_1__C, _averageLong_1__D], typing.Callable[[_averageLong_1__A, _averageLong_1__B, _averageLong_1__C, _averageLong_1__D], int]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_averageLong_1__A, _averageLong_1__B, _averageLong_1__C, _averageLong_1__D, typing.Any, float]: ...
    @typing.overload
    @staticmethod
    def averageLong(toLongTriFunction: typing.Union[org.optaplanner.core.api.function.ToLongTriFunction[_averageLong_2__A, _averageLong_2__B, _averageLong_2__C], typing.Callable[[_averageLong_2__A, _averageLong_2__B, _averageLong_2__C], int]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_averageLong_2__A, _averageLong_2__B, _averageLong_2__C, typing.Any, float]: ...
    @typing.overload
    @staticmethod
    def averageLong(toLongFunction: typing.Union[java.util.function.ToLongFunction[_averageLong_3__A], typing.Callable[[_averageLong_3__A], int]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_averageLong_3__A, typing.Any, float]: ...
    _compose_0__A = typing.TypeVar('_compose_0__A')  # <A>
    _compose_0__B = typing.TypeVar('_compose_0__B')  # <B>
    _compose_0__Result_ = typing.TypeVar('_compose_0__Result_')  # <Result_>
    _compose_0__SubResultContainer1_ = typing.TypeVar('_compose_0__SubResultContainer1_')  # <SubResultContainer1_>
    _compose_0__SubResultContainer2_ = typing.TypeVar('_compose_0__SubResultContainer2_')  # <SubResultContainer2_>
    _compose_0__SubResult1_ = typing.TypeVar('_compose_0__SubResult1_')  # <SubResult1_>
    _compose_0__SubResult2_ = typing.TypeVar('_compose_0__SubResult2_')  # <SubResult2_>
    _compose_1__A = typing.TypeVar('_compose_1__A')  # <A>
    _compose_1__B = typing.TypeVar('_compose_1__B')  # <B>
    _compose_1__Result_ = typing.TypeVar('_compose_1__Result_')  # <Result_>
    _compose_1__SubResultContainer1_ = typing.TypeVar('_compose_1__SubResultContainer1_')  # <SubResultContainer1_>
    _compose_1__SubResultContainer2_ = typing.TypeVar('_compose_1__SubResultContainer2_')  # <SubResultContainer2_>
    _compose_1__SubResultContainer3_ = typing.TypeVar('_compose_1__SubResultContainer3_')  # <SubResultContainer3_>
    _compose_1__SubResult1_ = typing.TypeVar('_compose_1__SubResult1_')  # <SubResult1_>
    _compose_1__SubResult2_ = typing.TypeVar('_compose_1__SubResult2_')  # <SubResult2_>
    _compose_1__SubResult3_ = typing.TypeVar('_compose_1__SubResult3_')  # <SubResult3_>
    _compose_2__A = typing.TypeVar('_compose_2__A')  # <A>
    _compose_2__B = typing.TypeVar('_compose_2__B')  # <B>
    _compose_2__Result_ = typing.TypeVar('_compose_2__Result_')  # <Result_>
    _compose_2__SubResultContainer1_ = typing.TypeVar('_compose_2__SubResultContainer1_')  # <SubResultContainer1_>
    _compose_2__SubResultContainer2_ = typing.TypeVar('_compose_2__SubResultContainer2_')  # <SubResultContainer2_>
    _compose_2__SubResultContainer3_ = typing.TypeVar('_compose_2__SubResultContainer3_')  # <SubResultContainer3_>
    _compose_2__SubResultContainer4_ = typing.TypeVar('_compose_2__SubResultContainer4_')  # <SubResultContainer4_>
    _compose_2__SubResult1_ = typing.TypeVar('_compose_2__SubResult1_')  # <SubResult1_>
    _compose_2__SubResult2_ = typing.TypeVar('_compose_2__SubResult2_')  # <SubResult2_>
    _compose_2__SubResult3_ = typing.TypeVar('_compose_2__SubResult3_')  # <SubResult3_>
    _compose_2__SubResult4_ = typing.TypeVar('_compose_2__SubResult4_')  # <SubResult4_>
    _compose_3__A = typing.TypeVar('_compose_3__A')  # <A>
    _compose_3__B = typing.TypeVar('_compose_3__B')  # <B>
    _compose_3__C = typing.TypeVar('_compose_3__C')  # <C>
    _compose_3__D = typing.TypeVar('_compose_3__D')  # <D>
    _compose_3__Result_ = typing.TypeVar('_compose_3__Result_')  # <Result_>
    _compose_3__SubResultContainer1_ = typing.TypeVar('_compose_3__SubResultContainer1_')  # <SubResultContainer1_>
    _compose_3__SubResultContainer2_ = typing.TypeVar('_compose_3__SubResultContainer2_')  # <SubResultContainer2_>
    _compose_3__SubResult1_ = typing.TypeVar('_compose_3__SubResult1_')  # <SubResult1_>
    _compose_3__SubResult2_ = typing.TypeVar('_compose_3__SubResult2_')  # <SubResult2_>
    _compose_4__A = typing.TypeVar('_compose_4__A')  # <A>
    _compose_4__B = typing.TypeVar('_compose_4__B')  # <B>
    _compose_4__C = typing.TypeVar('_compose_4__C')  # <C>
    _compose_4__D = typing.TypeVar('_compose_4__D')  # <D>
    _compose_4__Result_ = typing.TypeVar('_compose_4__Result_')  # <Result_>
    _compose_4__SubResultContainer1_ = typing.TypeVar('_compose_4__SubResultContainer1_')  # <SubResultContainer1_>
    _compose_4__SubResultContainer2_ = typing.TypeVar('_compose_4__SubResultContainer2_')  # <SubResultContainer2_>
    _compose_4__SubResultContainer3_ = typing.TypeVar('_compose_4__SubResultContainer3_')  # <SubResultContainer3_>
    _compose_4__SubResult1_ = typing.TypeVar('_compose_4__SubResult1_')  # <SubResult1_>
    _compose_4__SubResult2_ = typing.TypeVar('_compose_4__SubResult2_')  # <SubResult2_>
    _compose_4__SubResult3_ = typing.TypeVar('_compose_4__SubResult3_')  # <SubResult3_>
    _compose_5__A = typing.TypeVar('_compose_5__A')  # <A>
    _compose_5__B = typing.TypeVar('_compose_5__B')  # <B>
    _compose_5__C = typing.TypeVar('_compose_5__C')  # <C>
    _compose_5__D = typing.TypeVar('_compose_5__D')  # <D>
    _compose_5__Result_ = typing.TypeVar('_compose_5__Result_')  # <Result_>
    _compose_5__SubResultContainer1_ = typing.TypeVar('_compose_5__SubResultContainer1_')  # <SubResultContainer1_>
    _compose_5__SubResultContainer2_ = typing.TypeVar('_compose_5__SubResultContainer2_')  # <SubResultContainer2_>
    _compose_5__SubResultContainer3_ = typing.TypeVar('_compose_5__SubResultContainer3_')  # <SubResultContainer3_>
    _compose_5__SubResultContainer4_ = typing.TypeVar('_compose_5__SubResultContainer4_')  # <SubResultContainer4_>
    _compose_5__SubResult1_ = typing.TypeVar('_compose_5__SubResult1_')  # <SubResult1_>
    _compose_5__SubResult2_ = typing.TypeVar('_compose_5__SubResult2_')  # <SubResult2_>
    _compose_5__SubResult3_ = typing.TypeVar('_compose_5__SubResult3_')  # <SubResult3_>
    _compose_5__SubResult4_ = typing.TypeVar('_compose_5__SubResult4_')  # <SubResult4_>
    _compose_6__A = typing.TypeVar('_compose_6__A')  # <A>
    _compose_6__B = typing.TypeVar('_compose_6__B')  # <B>
    _compose_6__C = typing.TypeVar('_compose_6__C')  # <C>
    _compose_6__Result_ = typing.TypeVar('_compose_6__Result_')  # <Result_>
    _compose_6__SubResultContainer1_ = typing.TypeVar('_compose_6__SubResultContainer1_')  # <SubResultContainer1_>
    _compose_6__SubResultContainer2_ = typing.TypeVar('_compose_6__SubResultContainer2_')  # <SubResultContainer2_>
    _compose_6__SubResult1_ = typing.TypeVar('_compose_6__SubResult1_')  # <SubResult1_>
    _compose_6__SubResult2_ = typing.TypeVar('_compose_6__SubResult2_')  # <SubResult2_>
    _compose_7__A = typing.TypeVar('_compose_7__A')  # <A>
    _compose_7__B = typing.TypeVar('_compose_7__B')  # <B>
    _compose_7__C = typing.TypeVar('_compose_7__C')  # <C>
    _compose_7__Result_ = typing.TypeVar('_compose_7__Result_')  # <Result_>
    _compose_7__SubResultContainer1_ = typing.TypeVar('_compose_7__SubResultContainer1_')  # <SubResultContainer1_>
    _compose_7__SubResultContainer2_ = typing.TypeVar('_compose_7__SubResultContainer2_')  # <SubResultContainer2_>
    _compose_7__SubResultContainer3_ = typing.TypeVar('_compose_7__SubResultContainer3_')  # <SubResultContainer3_>
    _compose_7__SubResult1_ = typing.TypeVar('_compose_7__SubResult1_')  # <SubResult1_>
    _compose_7__SubResult2_ = typing.TypeVar('_compose_7__SubResult2_')  # <SubResult2_>
    _compose_7__SubResult3_ = typing.TypeVar('_compose_7__SubResult3_')  # <SubResult3_>
    _compose_8__A = typing.TypeVar('_compose_8__A')  # <A>
    _compose_8__B = typing.TypeVar('_compose_8__B')  # <B>
    _compose_8__C = typing.TypeVar('_compose_8__C')  # <C>
    _compose_8__Result_ = typing.TypeVar('_compose_8__Result_')  # <Result_>
    _compose_8__SubResultContainer1_ = typing.TypeVar('_compose_8__SubResultContainer1_')  # <SubResultContainer1_>
    _compose_8__SubResultContainer2_ = typing.TypeVar('_compose_8__SubResultContainer2_')  # <SubResultContainer2_>
    _compose_8__SubResultContainer3_ = typing.TypeVar('_compose_8__SubResultContainer3_')  # <SubResultContainer3_>
    _compose_8__SubResultContainer4_ = typing.TypeVar('_compose_8__SubResultContainer4_')  # <SubResultContainer4_>
    _compose_8__SubResult1_ = typing.TypeVar('_compose_8__SubResult1_')  # <SubResult1_>
    _compose_8__SubResult2_ = typing.TypeVar('_compose_8__SubResult2_')  # <SubResult2_>
    _compose_8__SubResult3_ = typing.TypeVar('_compose_8__SubResult3_')  # <SubResult3_>
    _compose_8__SubResult4_ = typing.TypeVar('_compose_8__SubResult4_')  # <SubResult4_>
    _compose_9__A = typing.TypeVar('_compose_9__A')  # <A>
    _compose_9__Result_ = typing.TypeVar('_compose_9__Result_')  # <Result_>
    _compose_9__SubResultContainer1_ = typing.TypeVar('_compose_9__SubResultContainer1_')  # <SubResultContainer1_>
    _compose_9__SubResultContainer2_ = typing.TypeVar('_compose_9__SubResultContainer2_')  # <SubResultContainer2_>
    _compose_9__SubResult1_ = typing.TypeVar('_compose_9__SubResult1_')  # <SubResult1_>
    _compose_9__SubResult2_ = typing.TypeVar('_compose_9__SubResult2_')  # <SubResult2_>
    _compose_10__A = typing.TypeVar('_compose_10__A')  # <A>
    _compose_10__Result_ = typing.TypeVar('_compose_10__Result_')  # <Result_>
    _compose_10__SubResultContainer1_ = typing.TypeVar('_compose_10__SubResultContainer1_')  # <SubResultContainer1_>
    _compose_10__SubResultContainer2_ = typing.TypeVar('_compose_10__SubResultContainer2_')  # <SubResultContainer2_>
    _compose_10__SubResultContainer3_ = typing.TypeVar('_compose_10__SubResultContainer3_')  # <SubResultContainer3_>
    _compose_10__SubResult1_ = typing.TypeVar('_compose_10__SubResult1_')  # <SubResult1_>
    _compose_10__SubResult2_ = typing.TypeVar('_compose_10__SubResult2_')  # <SubResult2_>
    _compose_10__SubResult3_ = typing.TypeVar('_compose_10__SubResult3_')  # <SubResult3_>
    _compose_11__A = typing.TypeVar('_compose_11__A')  # <A>
    _compose_11__Result_ = typing.TypeVar('_compose_11__Result_')  # <Result_>
    _compose_11__SubResultContainer1_ = typing.TypeVar('_compose_11__SubResultContainer1_')  # <SubResultContainer1_>
    _compose_11__SubResultContainer2_ = typing.TypeVar('_compose_11__SubResultContainer2_')  # <SubResultContainer2_>
    _compose_11__SubResultContainer3_ = typing.TypeVar('_compose_11__SubResultContainer3_')  # <SubResultContainer3_>
    _compose_11__SubResultContainer4_ = typing.TypeVar('_compose_11__SubResultContainer4_')  # <SubResultContainer4_>
    _compose_11__SubResult1_ = typing.TypeVar('_compose_11__SubResult1_')  # <SubResult1_>
    _compose_11__SubResult2_ = typing.TypeVar('_compose_11__SubResult2_')  # <SubResult2_>
    _compose_11__SubResult3_ = typing.TypeVar('_compose_11__SubResult3_')  # <SubResult3_>
    _compose_11__SubResult4_ = typing.TypeVar('_compose_11__SubResult4_')  # <SubResult4_>
    @typing.overload
    @staticmethod
    def compose(biConstraintCollector: org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_compose_0__A, _compose_0__B, _compose_0__SubResultContainer1_, _compose_0__SubResult1_], biConstraintCollector2: org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_compose_0__A, _compose_0__B, _compose_0__SubResultContainer2_, _compose_0__SubResult2_], biFunction: typing.Union[java.util.function.BiFunction[_compose_0__SubResult1_, _compose_0__SubResult2_, _compose_0__Result_], typing.Callable[[_compose_0__SubResult1_, _compose_0__SubResult2_], _compose_0__Result_]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_compose_0__A, _compose_0__B, typing.Any, _compose_0__Result_]: ...
    @typing.overload
    @staticmethod
    def compose(biConstraintCollector: org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_compose_1__A, _compose_1__B, _compose_1__SubResultContainer1_, _compose_1__SubResult1_], biConstraintCollector2: org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_compose_1__A, _compose_1__B, _compose_1__SubResultContainer2_, _compose_1__SubResult2_], biConstraintCollector3: org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_compose_1__A, _compose_1__B, _compose_1__SubResultContainer3_, _compose_1__SubResult3_], triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_compose_1__SubResult1_, _compose_1__SubResult2_, _compose_1__SubResult3_, _compose_1__Result_], typing.Callable[[_compose_1__SubResult1_, _compose_1__SubResult2_, _compose_1__SubResult3_], _compose_1__Result_]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_compose_1__A, _compose_1__B, typing.Any, _compose_1__Result_]: ...
    @typing.overload
    @staticmethod
    def compose(biConstraintCollector: org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_compose_2__A, _compose_2__B, _compose_2__SubResultContainer1_, _compose_2__SubResult1_], biConstraintCollector2: org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_compose_2__A, _compose_2__B, _compose_2__SubResultContainer2_, _compose_2__SubResult2_], biConstraintCollector3: org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_compose_2__A, _compose_2__B, _compose_2__SubResultContainer3_, _compose_2__SubResult3_], biConstraintCollector4: org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_compose_2__A, _compose_2__B, _compose_2__SubResultContainer4_, _compose_2__SubResult4_], quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_compose_2__SubResult1_, _compose_2__SubResult2_, _compose_2__SubResult3_, _compose_2__SubResult4_, _compose_2__Result_], typing.Callable[[_compose_2__SubResult1_, _compose_2__SubResult2_, _compose_2__SubResult3_, _compose_2__SubResult4_], _compose_2__Result_]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_compose_2__A, _compose_2__B, typing.Any, _compose_2__Result_]: ...
    @typing.overload
    @staticmethod
    def compose(quadConstraintCollector: org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_compose_3__A, _compose_3__B, _compose_3__C, _compose_3__D, _compose_3__SubResultContainer1_, _compose_3__SubResult1_], quadConstraintCollector2: org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_compose_3__A, _compose_3__B, _compose_3__C, _compose_3__D, _compose_3__SubResultContainer2_, _compose_3__SubResult2_], biFunction: typing.Union[java.util.function.BiFunction[_compose_3__SubResult1_, _compose_3__SubResult2_, _compose_3__Result_], typing.Callable[[_compose_3__SubResult1_, _compose_3__SubResult2_], _compose_3__Result_]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_compose_3__A, _compose_3__B, _compose_3__C, _compose_3__D, typing.Any, _compose_3__Result_]: ...
    @typing.overload
    @staticmethod
    def compose(quadConstraintCollector: org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_compose_4__A, _compose_4__B, _compose_4__C, _compose_4__D, _compose_4__SubResultContainer1_, _compose_4__SubResult1_], quadConstraintCollector2: org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_compose_4__A, _compose_4__B, _compose_4__C, _compose_4__D, _compose_4__SubResultContainer2_, _compose_4__SubResult2_], quadConstraintCollector3: org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_compose_4__A, _compose_4__B, _compose_4__C, _compose_4__D, _compose_4__SubResultContainer3_, _compose_4__SubResult3_], triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_compose_4__SubResult1_, _compose_4__SubResult2_, _compose_4__SubResult3_, _compose_4__Result_], typing.Callable[[_compose_4__SubResult1_, _compose_4__SubResult2_, _compose_4__SubResult3_], _compose_4__Result_]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_compose_4__A, _compose_4__B, _compose_4__C, _compose_4__D, typing.Any, _compose_4__Result_]: ...
    @typing.overload
    @staticmethod
    def compose(quadConstraintCollector: org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_compose_5__A, _compose_5__B, _compose_5__C, _compose_5__D, _compose_5__SubResultContainer1_, _compose_5__SubResult1_], quadConstraintCollector2: org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_compose_5__A, _compose_5__B, _compose_5__C, _compose_5__D, _compose_5__SubResultContainer2_, _compose_5__SubResult2_], quadConstraintCollector3: org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_compose_5__A, _compose_5__B, _compose_5__C, _compose_5__D, _compose_5__SubResultContainer3_, _compose_5__SubResult3_], quadConstraintCollector4: org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_compose_5__A, _compose_5__B, _compose_5__C, _compose_5__D, _compose_5__SubResultContainer4_, _compose_5__SubResult4_], quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_compose_5__SubResult1_, _compose_5__SubResult2_, _compose_5__SubResult3_, _compose_5__SubResult4_, _compose_5__Result_], typing.Callable[[_compose_5__SubResult1_, _compose_5__SubResult2_, _compose_5__SubResult3_, _compose_5__SubResult4_], _compose_5__Result_]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_compose_5__A, _compose_5__B, _compose_5__C, _compose_5__D, typing.Any, _compose_5__Result_]: ...
    @typing.overload
    @staticmethod
    def compose(triConstraintCollector: org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_compose_6__A, _compose_6__B, _compose_6__C, _compose_6__SubResultContainer1_, _compose_6__SubResult1_], triConstraintCollector2: org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_compose_6__A, _compose_6__B, _compose_6__C, _compose_6__SubResultContainer2_, _compose_6__SubResult2_], biFunction: typing.Union[java.util.function.BiFunction[_compose_6__SubResult1_, _compose_6__SubResult2_, _compose_6__Result_], typing.Callable[[_compose_6__SubResult1_, _compose_6__SubResult2_], _compose_6__Result_]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_compose_6__A, _compose_6__B, _compose_6__C, typing.Any, _compose_6__Result_]: ...
    @typing.overload
    @staticmethod
    def compose(triConstraintCollector: org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_compose_7__A, _compose_7__B, _compose_7__C, _compose_7__SubResultContainer1_, _compose_7__SubResult1_], triConstraintCollector2: org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_compose_7__A, _compose_7__B, _compose_7__C, _compose_7__SubResultContainer2_, _compose_7__SubResult2_], triConstraintCollector3: org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_compose_7__A, _compose_7__B, _compose_7__C, _compose_7__SubResultContainer3_, _compose_7__SubResult3_], triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_compose_7__SubResult1_, _compose_7__SubResult2_, _compose_7__SubResult3_, _compose_7__Result_], typing.Callable[[_compose_7__SubResult1_, _compose_7__SubResult2_, _compose_7__SubResult3_], _compose_7__Result_]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_compose_7__A, _compose_7__B, _compose_7__C, typing.Any, _compose_7__Result_]: ...
    @typing.overload
    @staticmethod
    def compose(triConstraintCollector: org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_compose_8__A, _compose_8__B, _compose_8__C, _compose_8__SubResultContainer1_, _compose_8__SubResult1_], triConstraintCollector2: org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_compose_8__A, _compose_8__B, _compose_8__C, _compose_8__SubResultContainer2_, _compose_8__SubResult2_], triConstraintCollector3: org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_compose_8__A, _compose_8__B, _compose_8__C, _compose_8__SubResultContainer3_, _compose_8__SubResult3_], triConstraintCollector4: org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_compose_8__A, _compose_8__B, _compose_8__C, _compose_8__SubResultContainer4_, _compose_8__SubResult4_], quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_compose_8__SubResult1_, _compose_8__SubResult2_, _compose_8__SubResult3_, _compose_8__SubResult4_, _compose_8__Result_], typing.Callable[[_compose_8__SubResult1_, _compose_8__SubResult2_, _compose_8__SubResult3_, _compose_8__SubResult4_], _compose_8__Result_]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_compose_8__A, _compose_8__B, _compose_8__C, typing.Any, _compose_8__Result_]: ...
    @typing.overload
    @staticmethod
    def compose(uniConstraintCollector: org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_compose_9__A, _compose_9__SubResultContainer1_, _compose_9__SubResult1_], uniConstraintCollector2: org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_compose_9__A, _compose_9__SubResultContainer2_, _compose_9__SubResult2_], biFunction: typing.Union[java.util.function.BiFunction[_compose_9__SubResult1_, _compose_9__SubResult2_, _compose_9__Result_], typing.Callable[[_compose_9__SubResult1_, _compose_9__SubResult2_], _compose_9__Result_]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_compose_9__A, typing.Any, _compose_9__Result_]: ...
    @typing.overload
    @staticmethod
    def compose(uniConstraintCollector: org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_compose_10__A, _compose_10__SubResultContainer1_, _compose_10__SubResult1_], uniConstraintCollector2: org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_compose_10__A, _compose_10__SubResultContainer2_, _compose_10__SubResult2_], uniConstraintCollector3: org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_compose_10__A, _compose_10__SubResultContainer3_, _compose_10__SubResult3_], triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_compose_10__SubResult1_, _compose_10__SubResult2_, _compose_10__SubResult3_, _compose_10__Result_], typing.Callable[[_compose_10__SubResult1_, _compose_10__SubResult2_, _compose_10__SubResult3_], _compose_10__Result_]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_compose_10__A, typing.Any, _compose_10__Result_]: ...
    @typing.overload
    @staticmethod
    def compose(uniConstraintCollector: org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_compose_11__A, _compose_11__SubResultContainer1_, _compose_11__SubResult1_], uniConstraintCollector2: org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_compose_11__A, _compose_11__SubResultContainer2_, _compose_11__SubResult2_], uniConstraintCollector3: org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_compose_11__A, _compose_11__SubResultContainer3_, _compose_11__SubResult3_], uniConstraintCollector4: org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_compose_11__A, _compose_11__SubResultContainer4_, _compose_11__SubResult4_], quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_compose_11__SubResult1_, _compose_11__SubResult2_, _compose_11__SubResult3_, _compose_11__SubResult4_, _compose_11__Result_], typing.Callable[[_compose_11__SubResult1_, _compose_11__SubResult2_, _compose_11__SubResult3_, _compose_11__SubResult4_], _compose_11__Result_]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_compose_11__A, typing.Any, _compose_11__Result_]: ...
    _conditionally_0__A = typing.TypeVar('_conditionally_0__A')  # <A>
    _conditionally_0__B = typing.TypeVar('_conditionally_0__B')  # <B>
    _conditionally_0__ResultContainer_ = typing.TypeVar('_conditionally_0__ResultContainer_')  # <ResultContainer_>
    _conditionally_0__Result_ = typing.TypeVar('_conditionally_0__Result_')  # <Result_>
    _conditionally_1__A = typing.TypeVar('_conditionally_1__A')  # <A>
    _conditionally_1__B = typing.TypeVar('_conditionally_1__B')  # <B>
    _conditionally_1__C = typing.TypeVar('_conditionally_1__C')  # <C>
    _conditionally_1__D = typing.TypeVar('_conditionally_1__D')  # <D>
    _conditionally_1__ResultContainer_ = typing.TypeVar('_conditionally_1__ResultContainer_')  # <ResultContainer_>
    _conditionally_1__Result_ = typing.TypeVar('_conditionally_1__Result_')  # <Result_>
    _conditionally_2__A = typing.TypeVar('_conditionally_2__A')  # <A>
    _conditionally_2__B = typing.TypeVar('_conditionally_2__B')  # <B>
    _conditionally_2__C = typing.TypeVar('_conditionally_2__C')  # <C>
    _conditionally_2__ResultContainer_ = typing.TypeVar('_conditionally_2__ResultContainer_')  # <ResultContainer_>
    _conditionally_2__Result_ = typing.TypeVar('_conditionally_2__Result_')  # <Result_>
    _conditionally_3__A = typing.TypeVar('_conditionally_3__A')  # <A>
    _conditionally_3__ResultContainer_ = typing.TypeVar('_conditionally_3__ResultContainer_')  # <ResultContainer_>
    _conditionally_3__Result_ = typing.TypeVar('_conditionally_3__Result_')  # <Result_>
    @typing.overload
    @staticmethod
    def conditionally(biPredicate: typing.Union[java.util.function.BiPredicate[_conditionally_0__A, _conditionally_0__B], typing.Callable[[_conditionally_0__A, _conditionally_0__B], bool]], biConstraintCollector: org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_conditionally_0__A, _conditionally_0__B, _conditionally_0__ResultContainer_, _conditionally_0__Result_]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_conditionally_0__A, _conditionally_0__B, _conditionally_0__ResultContainer_, _conditionally_0__Result_]: ...
    @typing.overload
    @staticmethod
    def conditionally(quadPredicate: typing.Union[org.optaplanner.core.api.function.QuadPredicate[_conditionally_1__A, _conditionally_1__B, _conditionally_1__C, _conditionally_1__D], typing.Callable[[_conditionally_1__A, _conditionally_1__B, _conditionally_1__C, _conditionally_1__D], bool]], quadConstraintCollector: org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_conditionally_1__A, _conditionally_1__B, _conditionally_1__C, _conditionally_1__D, _conditionally_1__ResultContainer_, _conditionally_1__Result_]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_conditionally_1__A, _conditionally_1__B, _conditionally_1__C, _conditionally_1__D, _conditionally_1__ResultContainer_, _conditionally_1__Result_]: ...
    @typing.overload
    @staticmethod
    def conditionally(triPredicate: typing.Union[org.optaplanner.core.api.function.TriPredicate[_conditionally_2__A, _conditionally_2__B, _conditionally_2__C], typing.Callable[[_conditionally_2__A, _conditionally_2__B, _conditionally_2__C], bool]], triConstraintCollector: org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_conditionally_2__A, _conditionally_2__B, _conditionally_2__C, _conditionally_2__ResultContainer_, _conditionally_2__Result_]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_conditionally_2__A, _conditionally_2__B, _conditionally_2__C, _conditionally_2__ResultContainer_, _conditionally_2__Result_]: ...
    @typing.overload
    @staticmethod
    def conditionally(predicate: typing.Union[java.util.function.Predicate[_conditionally_3__A], typing.Callable[[_conditionally_3__A], bool]], uniConstraintCollector: org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_conditionally_3__A, _conditionally_3__ResultContainer_, _conditionally_3__Result_]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_conditionally_3__A, _conditionally_3__ResultContainer_, _conditionally_3__Result_]: ...
    _count__A = typing.TypeVar('_count__A')  # <A>
    @staticmethod
    def count() -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_count__A, typing.Any, int]: ...
    _countBi__A = typing.TypeVar('_countBi__A')  # <A>
    _countBi__B = typing.TypeVar('_countBi__B')  # <B>
    @staticmethod
    def countBi() -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_countBi__A, _countBi__B, typing.Any, int]: ...
    _countDistinct_0__A = typing.TypeVar('_countDistinct_0__A')  # <A>
    _countDistinct_0__B = typing.TypeVar('_countDistinct_0__B')  # <B>
    _countDistinct_1__A = typing.TypeVar('_countDistinct_1__A')  # <A>
    _countDistinct_1__B = typing.TypeVar('_countDistinct_1__B')  # <B>
    _countDistinct_1__C = typing.TypeVar('_countDistinct_1__C')  # <C>
    _countDistinct_1__D = typing.TypeVar('_countDistinct_1__D')  # <D>
    _countDistinct_2__A = typing.TypeVar('_countDistinct_2__A')  # <A>
    _countDistinct_2__B = typing.TypeVar('_countDistinct_2__B')  # <B>
    _countDistinct_2__C = typing.TypeVar('_countDistinct_2__C')  # <C>
    _countDistinct_3__A = typing.TypeVar('_countDistinct_3__A')  # <A>
    _countDistinct_4__A = typing.TypeVar('_countDistinct_4__A')  # <A>
    @typing.overload
    @staticmethod
    def countDistinct(biFunction: typing.Union[java.util.function.BiFunction[_countDistinct_0__A, _countDistinct_0__B, typing.Any], typing.Callable[[_countDistinct_0__A, _countDistinct_0__B], typing.Any]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_countDistinct_0__A, _countDistinct_0__B, typing.Any, int]: ...
    @typing.overload
    @staticmethod
    def countDistinct(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_countDistinct_1__A, _countDistinct_1__B, _countDistinct_1__C, _countDistinct_1__D, typing.Any], typing.Callable[[_countDistinct_1__A, _countDistinct_1__B, _countDistinct_1__C, _countDistinct_1__D], typing.Any]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_countDistinct_1__A, _countDistinct_1__B, _countDistinct_1__C, _countDistinct_1__D, typing.Any, int]: ...
    @typing.overload
    @staticmethod
    def countDistinct(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_countDistinct_2__A, _countDistinct_2__B, _countDistinct_2__C, typing.Any], typing.Callable[[_countDistinct_2__A, _countDistinct_2__B, _countDistinct_2__C], typing.Any]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_countDistinct_2__A, _countDistinct_2__B, _countDistinct_2__C, typing.Any, int]: ...
    @typing.overload
    @staticmethod
    def countDistinct() -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_countDistinct_3__A, typing.Any, int]: ...
    @typing.overload
    @staticmethod
    def countDistinct(function: typing.Union[java.util.function.Function[_countDistinct_4__A, typing.Any], typing.Callable[[_countDistinct_4__A], typing.Any]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_countDistinct_4__A, typing.Any, int]: ...
    _countDistinctLong_0__A = typing.TypeVar('_countDistinctLong_0__A')  # <A>
    _countDistinctLong_0__B = typing.TypeVar('_countDistinctLong_0__B')  # <B>
    _countDistinctLong_1__A = typing.TypeVar('_countDistinctLong_1__A')  # <A>
    _countDistinctLong_1__B = typing.TypeVar('_countDistinctLong_1__B')  # <B>
    _countDistinctLong_1__C = typing.TypeVar('_countDistinctLong_1__C')  # <C>
    _countDistinctLong_1__D = typing.TypeVar('_countDistinctLong_1__D')  # <D>
    _countDistinctLong_2__A = typing.TypeVar('_countDistinctLong_2__A')  # <A>
    _countDistinctLong_2__B = typing.TypeVar('_countDistinctLong_2__B')  # <B>
    _countDistinctLong_2__C = typing.TypeVar('_countDistinctLong_2__C')  # <C>
    _countDistinctLong_3__A = typing.TypeVar('_countDistinctLong_3__A')  # <A>
    @typing.overload
    @staticmethod
    def countDistinctLong(biFunction: typing.Union[java.util.function.BiFunction[_countDistinctLong_0__A, _countDistinctLong_0__B, typing.Any], typing.Callable[[_countDistinctLong_0__A, _countDistinctLong_0__B], typing.Any]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_countDistinctLong_0__A, _countDistinctLong_0__B, typing.Any, int]: ...
    @typing.overload
    @staticmethod
    def countDistinctLong(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_countDistinctLong_1__A, _countDistinctLong_1__B, _countDistinctLong_1__C, _countDistinctLong_1__D, typing.Any], typing.Callable[[_countDistinctLong_1__A, _countDistinctLong_1__B, _countDistinctLong_1__C, _countDistinctLong_1__D], typing.Any]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_countDistinctLong_1__A, _countDistinctLong_1__B, _countDistinctLong_1__C, _countDistinctLong_1__D, typing.Any, int]: ...
    @typing.overload
    @staticmethod
    def countDistinctLong(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_countDistinctLong_2__A, _countDistinctLong_2__B, _countDistinctLong_2__C, typing.Any], typing.Callable[[_countDistinctLong_2__A, _countDistinctLong_2__B, _countDistinctLong_2__C], typing.Any]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_countDistinctLong_2__A, _countDistinctLong_2__B, _countDistinctLong_2__C, typing.Any, int]: ...
    @typing.overload
    @staticmethod
    def countDistinctLong(function: typing.Union[java.util.function.Function[_countDistinctLong_3__A, typing.Any], typing.Callable[[_countDistinctLong_3__A], typing.Any]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_countDistinctLong_3__A, typing.Any, int]: ...
    _countLong__A = typing.TypeVar('_countLong__A')  # <A>
    @staticmethod
    def countLong() -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_countLong__A, typing.Any, int]: ...
    _countLongBi__A = typing.TypeVar('_countLongBi__A')  # <A>
    _countLongBi__B = typing.TypeVar('_countLongBi__B')  # <B>
    @staticmethod
    def countLongBi() -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_countLongBi__A, _countLongBi__B, typing.Any, int]: ...
    _countLongQuad__A = typing.TypeVar('_countLongQuad__A')  # <A>
    _countLongQuad__B = typing.TypeVar('_countLongQuad__B')  # <B>
    _countLongQuad__C = typing.TypeVar('_countLongQuad__C')  # <C>
    _countLongQuad__D = typing.TypeVar('_countLongQuad__D')  # <D>
    @staticmethod
    def countLongQuad() -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_countLongQuad__A, _countLongQuad__B, _countLongQuad__C, _countLongQuad__D, typing.Any, int]: ...
    _countLongTri__A = typing.TypeVar('_countLongTri__A')  # <A>
    _countLongTri__B = typing.TypeVar('_countLongTri__B')  # <B>
    _countLongTri__C = typing.TypeVar('_countLongTri__C')  # <C>
    @staticmethod
    def countLongTri() -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_countLongTri__A, _countLongTri__B, _countLongTri__C, typing.Any, int]: ...
    _countQuad__A = typing.TypeVar('_countQuad__A')  # <A>
    _countQuad__B = typing.TypeVar('_countQuad__B')  # <B>
    _countQuad__C = typing.TypeVar('_countQuad__C')  # <C>
    _countQuad__D = typing.TypeVar('_countQuad__D')  # <D>
    @staticmethod
    def countQuad() -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_countQuad__A, _countQuad__B, _countQuad__C, _countQuad__D, typing.Any, int]: ...
    _countTri__A = typing.TypeVar('_countTri__A')  # <A>
    _countTri__B = typing.TypeVar('_countTri__B')  # <B>
    _countTri__C = typing.TypeVar('_countTri__C')  # <C>
    @staticmethod
    def countTri() -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_countTri__A, _countTri__B, _countTri__C, typing.Any, int]: ...
    _max_0__A = typing.TypeVar('_max_0__A')  # <A>
    _max_0__B = typing.TypeVar('_max_0__B')  # <B>
    _max_0__Mapped = typing.TypeVar('_max_0__Mapped', bound=java.lang.Comparable)  # <Mapped>
    _max_1__A = typing.TypeVar('_max_1__A')  # <A>
    _max_1__B = typing.TypeVar('_max_1__B')  # <B>
    _max_1__Mapped = typing.TypeVar('_max_1__Mapped')  # <Mapped>
    _max_2__A = typing.TypeVar('_max_2__A')  # <A>
    _max_2__B = typing.TypeVar('_max_2__B')  # <B>
    _max_2__C = typing.TypeVar('_max_2__C')  # <C>
    _max_2__D = typing.TypeVar('_max_2__D')  # <D>
    _max_2__Mapped = typing.TypeVar('_max_2__Mapped', bound=java.lang.Comparable)  # <Mapped>
    _max_3__A = typing.TypeVar('_max_3__A')  # <A>
    _max_3__B = typing.TypeVar('_max_3__B')  # <B>
    _max_3__C = typing.TypeVar('_max_3__C')  # <C>
    _max_3__D = typing.TypeVar('_max_3__D')  # <D>
    _max_3__Mapped = typing.TypeVar('_max_3__Mapped')  # <Mapped>
    _max_4__A = typing.TypeVar('_max_4__A')  # <A>
    _max_4__B = typing.TypeVar('_max_4__B')  # <B>
    _max_4__C = typing.TypeVar('_max_4__C')  # <C>
    _max_4__Mapped = typing.TypeVar('_max_4__Mapped', bound=java.lang.Comparable)  # <Mapped>
    _max_5__A = typing.TypeVar('_max_5__A')  # <A>
    _max_5__B = typing.TypeVar('_max_5__B')  # <B>
    _max_5__C = typing.TypeVar('_max_5__C')  # <C>
    _max_5__Mapped = typing.TypeVar('_max_5__Mapped')  # <Mapped>
    _max_6__A = typing.TypeVar('_max_6__A', bound=java.lang.Comparable)  # <A>
    _max_7__A = typing.TypeVar('_max_7__A')  # <A>
    _max_8__A = typing.TypeVar('_max_8__A')  # <A>
    _max_8__Mapped = typing.TypeVar('_max_8__Mapped', bound=java.lang.Comparable)  # <Mapped>
    _max_9__A = typing.TypeVar('_max_9__A')  # <A>
    _max_9__Mapped = typing.TypeVar('_max_9__Mapped')  # <Mapped>
    @typing.overload
    @staticmethod
    def max(biFunction: typing.Union[java.util.function.BiFunction[_max_0__A, _max_0__B, _max_0__Mapped], typing.Callable[[_max_0__A, _max_0__B], _max_0__Mapped]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_max_0__A, _max_0__B, typing.Any, _max_0__Mapped]: ...
    @typing.overload
    @staticmethod
    def max(biFunction: typing.Union[java.util.function.BiFunction[_max_1__A, _max_1__B, _max_1__Mapped], typing.Callable[[_max_1__A, _max_1__B], _max_1__Mapped]], comparator: typing.Union[java.util.Comparator[_max_1__Mapped], typing.Callable[[_max_1__Mapped, _max_1__Mapped], int]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_max_1__A, _max_1__B, typing.Any, _max_1__Mapped]: ...
    @typing.overload
    @staticmethod
    def max(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_max_2__A, _max_2__B, _max_2__C, _max_2__D, _max_2__Mapped], typing.Callable[[_max_2__A, _max_2__B, _max_2__C, _max_2__D], _max_2__Mapped]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_max_2__A, _max_2__B, _max_2__C, _max_2__D, typing.Any, _max_2__Mapped]: ...
    @typing.overload
    @staticmethod
    def max(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_max_3__A, _max_3__B, _max_3__C, _max_3__D, _max_3__Mapped], typing.Callable[[_max_3__A, _max_3__B, _max_3__C, _max_3__D], _max_3__Mapped]], comparator: typing.Union[java.util.Comparator[_max_3__Mapped], typing.Callable[[_max_3__Mapped, _max_3__Mapped], int]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_max_3__A, _max_3__B, _max_3__C, _max_3__D, typing.Any, _max_3__Mapped]: ...
    @typing.overload
    @staticmethod
    def max(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_max_4__A, _max_4__B, _max_4__C, _max_4__Mapped], typing.Callable[[_max_4__A, _max_4__B, _max_4__C], _max_4__Mapped]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_max_4__A, _max_4__B, _max_4__C, typing.Any, _max_4__Mapped]: ...
    @typing.overload
    @staticmethod
    def max(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_max_5__A, _max_5__B, _max_5__C, _max_5__Mapped], typing.Callable[[_max_5__A, _max_5__B, _max_5__C], _max_5__Mapped]], comparator: typing.Union[java.util.Comparator[_max_5__Mapped], typing.Callable[[_max_5__Mapped, _max_5__Mapped], int]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_max_5__A, _max_5__B, _max_5__C, typing.Any, _max_5__Mapped]: ...
    @typing.overload
    @staticmethod
    def max() -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_max_6__A, typing.Any, _max_6__A]: ...
    @typing.overload
    @staticmethod
    def max(comparator: typing.Union[java.util.Comparator[_max_7__A], typing.Callable[[_max_7__A, _max_7__A], int]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_max_7__A, typing.Any, _max_7__A]: ...
    @typing.overload
    @staticmethod
    def max(function: typing.Union[java.util.function.Function[_max_8__A, _max_8__Mapped], typing.Callable[[_max_8__A], _max_8__Mapped]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_max_8__A, typing.Any, _max_8__Mapped]: ...
    @typing.overload
    @staticmethod
    def max(function: typing.Union[java.util.function.Function[_max_9__A, _max_9__Mapped], typing.Callable[[_max_9__A], _max_9__Mapped]], comparator: typing.Union[java.util.Comparator[_max_9__Mapped], typing.Callable[[_max_9__Mapped, _max_9__Mapped], int]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_max_9__A, typing.Any, _max_9__Mapped]: ...
    _min_0__A = typing.TypeVar('_min_0__A')  # <A>
    _min_0__B = typing.TypeVar('_min_0__B')  # <B>
    _min_0__Mapped = typing.TypeVar('_min_0__Mapped', bound=java.lang.Comparable)  # <Mapped>
    _min_1__A = typing.TypeVar('_min_1__A')  # <A>
    _min_1__B = typing.TypeVar('_min_1__B')  # <B>
    _min_1__Mapped = typing.TypeVar('_min_1__Mapped')  # <Mapped>
    _min_2__A = typing.TypeVar('_min_2__A')  # <A>
    _min_2__B = typing.TypeVar('_min_2__B')  # <B>
    _min_2__C = typing.TypeVar('_min_2__C')  # <C>
    _min_2__D = typing.TypeVar('_min_2__D')  # <D>
    _min_2__Mapped = typing.TypeVar('_min_2__Mapped', bound=java.lang.Comparable)  # <Mapped>
    _min_3__A = typing.TypeVar('_min_3__A')  # <A>
    _min_3__B = typing.TypeVar('_min_3__B')  # <B>
    _min_3__C = typing.TypeVar('_min_3__C')  # <C>
    _min_3__D = typing.TypeVar('_min_3__D')  # <D>
    _min_3__Mapped = typing.TypeVar('_min_3__Mapped')  # <Mapped>
    _min_4__A = typing.TypeVar('_min_4__A')  # <A>
    _min_4__B = typing.TypeVar('_min_4__B')  # <B>
    _min_4__C = typing.TypeVar('_min_4__C')  # <C>
    _min_4__Mapped = typing.TypeVar('_min_4__Mapped', bound=java.lang.Comparable)  # <Mapped>
    _min_5__A = typing.TypeVar('_min_5__A')  # <A>
    _min_5__B = typing.TypeVar('_min_5__B')  # <B>
    _min_5__C = typing.TypeVar('_min_5__C')  # <C>
    _min_5__Mapped = typing.TypeVar('_min_5__Mapped')  # <Mapped>
    _min_6__A = typing.TypeVar('_min_6__A', bound=java.lang.Comparable)  # <A>
    _min_7__A = typing.TypeVar('_min_7__A')  # <A>
    _min_8__A = typing.TypeVar('_min_8__A')  # <A>
    _min_8__Mapped = typing.TypeVar('_min_8__Mapped', bound=java.lang.Comparable)  # <Mapped>
    _min_9__A = typing.TypeVar('_min_9__A')  # <A>
    _min_9__Mapped = typing.TypeVar('_min_9__Mapped')  # <Mapped>
    @typing.overload
    @staticmethod
    def min(biFunction: typing.Union[java.util.function.BiFunction[_min_0__A, _min_0__B, _min_0__Mapped], typing.Callable[[_min_0__A, _min_0__B], _min_0__Mapped]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_min_0__A, _min_0__B, typing.Any, _min_0__Mapped]: ...
    @typing.overload
    @staticmethod
    def min(biFunction: typing.Union[java.util.function.BiFunction[_min_1__A, _min_1__B, _min_1__Mapped], typing.Callable[[_min_1__A, _min_1__B], _min_1__Mapped]], comparator: typing.Union[java.util.Comparator[_min_1__Mapped], typing.Callable[[_min_1__Mapped, _min_1__Mapped], int]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_min_1__A, _min_1__B, typing.Any, _min_1__Mapped]: ...
    @typing.overload
    @staticmethod
    def min(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_min_2__A, _min_2__B, _min_2__C, _min_2__D, _min_2__Mapped], typing.Callable[[_min_2__A, _min_2__B, _min_2__C, _min_2__D], _min_2__Mapped]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_min_2__A, _min_2__B, _min_2__C, _min_2__D, typing.Any, _min_2__Mapped]: ...
    @typing.overload
    @staticmethod
    def min(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_min_3__A, _min_3__B, _min_3__C, _min_3__D, _min_3__Mapped], typing.Callable[[_min_3__A, _min_3__B, _min_3__C, _min_3__D], _min_3__Mapped]], comparator: typing.Union[java.util.Comparator[_min_3__Mapped], typing.Callable[[_min_3__Mapped, _min_3__Mapped], int]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_min_3__A, _min_3__B, _min_3__C, _min_3__D, typing.Any, _min_3__Mapped]: ...
    @typing.overload
    @staticmethod
    def min(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_min_4__A, _min_4__B, _min_4__C, _min_4__Mapped], typing.Callable[[_min_4__A, _min_4__B, _min_4__C], _min_4__Mapped]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_min_4__A, _min_4__B, _min_4__C, typing.Any, _min_4__Mapped]: ...
    @typing.overload
    @staticmethod
    def min(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_min_5__A, _min_5__B, _min_5__C, _min_5__Mapped], typing.Callable[[_min_5__A, _min_5__B, _min_5__C], _min_5__Mapped]], comparator: typing.Union[java.util.Comparator[_min_5__Mapped], typing.Callable[[_min_5__Mapped, _min_5__Mapped], int]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_min_5__A, _min_5__B, _min_5__C, typing.Any, _min_5__Mapped]: ...
    @typing.overload
    @staticmethod
    def min() -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_min_6__A, typing.Any, _min_6__A]: ...
    @typing.overload
    @staticmethod
    def min(comparator: typing.Union[java.util.Comparator[_min_7__A], typing.Callable[[_min_7__A, _min_7__A], int]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_min_7__A, typing.Any, _min_7__A]: ...
    @typing.overload
    @staticmethod
    def min(function: typing.Union[java.util.function.Function[_min_8__A, _min_8__Mapped], typing.Callable[[_min_8__A], _min_8__Mapped]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_min_8__A, typing.Any, _min_8__Mapped]: ...
    @typing.overload
    @staticmethod
    def min(function: typing.Union[java.util.function.Function[_min_9__A, _min_9__Mapped], typing.Callable[[_min_9__A], _min_9__Mapped]], comparator: typing.Union[java.util.Comparator[_min_9__Mapped], typing.Callable[[_min_9__Mapped, _min_9__Mapped], int]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_min_9__A, typing.Any, _min_9__Mapped]: ...
    _sum_0__A = typing.TypeVar('_sum_0__A')  # <A>
    _sum_0__B = typing.TypeVar('_sum_0__B')  # <B>
    _sum_0__Result = typing.TypeVar('_sum_0__Result')  # <Result>
    _sum_1__A = typing.TypeVar('_sum_1__A')  # <A>
    _sum_1__B = typing.TypeVar('_sum_1__B')  # <B>
    _sum_2__A = typing.TypeVar('_sum_2__A')  # <A>
    _sum_2__B = typing.TypeVar('_sum_2__B')  # <B>
    _sum_2__C = typing.TypeVar('_sum_2__C')  # <C>
    _sum_2__D = typing.TypeVar('_sum_2__D')  # <D>
    _sum_2__Result = typing.TypeVar('_sum_2__Result')  # <Result>
    _sum_3__A = typing.TypeVar('_sum_3__A')  # <A>
    _sum_3__B = typing.TypeVar('_sum_3__B')  # <B>
    _sum_3__C = typing.TypeVar('_sum_3__C')  # <C>
    _sum_3__D = typing.TypeVar('_sum_3__D')  # <D>
    _sum_4__A = typing.TypeVar('_sum_4__A')  # <A>
    _sum_4__B = typing.TypeVar('_sum_4__B')  # <B>
    _sum_4__C = typing.TypeVar('_sum_4__C')  # <C>
    _sum_5__A = typing.TypeVar('_sum_5__A')  # <A>
    _sum_5__B = typing.TypeVar('_sum_5__B')  # <B>
    _sum_5__C = typing.TypeVar('_sum_5__C')  # <C>
    _sum_5__Result = typing.TypeVar('_sum_5__Result')  # <Result>
    _sum_6__A = typing.TypeVar('_sum_6__A')  # <A>
    _sum_6__Result = typing.TypeVar('_sum_6__Result')  # <Result>
    _sum_7__A = typing.TypeVar('_sum_7__A')  # <A>
    @typing.overload
    @staticmethod
    def sum(biFunction: typing.Union[java.util.function.BiFunction[_sum_0__A, _sum_0__B, _sum_0__Result], typing.Callable[[_sum_0__A, _sum_0__B], _sum_0__Result]], result: _sum_0__Result, binaryOperator: typing.Union[java.util.function.BinaryOperator[_sum_0__Result], typing.Callable], binaryOperator2: typing.Union[java.util.function.BinaryOperator[_sum_0__Result], typing.Callable]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_sum_0__A, _sum_0__B, typing.Any, _sum_0__Result]: ...
    @typing.overload
    @staticmethod
    def sum(toIntBiFunction: typing.Union[java.util.function.ToIntBiFunction[_sum_1__A, _sum_1__B], typing.Callable[[_sum_1__A, _sum_1__B], int]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_sum_1__A, _sum_1__B, typing.Any, int]: ...
    @typing.overload
    @staticmethod
    def sum(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_sum_2__A, _sum_2__B, _sum_2__C, _sum_2__D, _sum_2__Result], typing.Callable[[_sum_2__A, _sum_2__B, _sum_2__C, _sum_2__D], _sum_2__Result]], result: _sum_2__Result, binaryOperator: typing.Union[java.util.function.BinaryOperator[_sum_2__Result], typing.Callable], binaryOperator2: typing.Union[java.util.function.BinaryOperator[_sum_2__Result], typing.Callable]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_sum_2__A, _sum_2__B, _sum_2__C, _sum_2__D, typing.Any, _sum_2__Result]: ...
    @typing.overload
    @staticmethod
    def sum(toIntQuadFunction: typing.Union[org.optaplanner.core.api.function.ToIntQuadFunction[_sum_3__A, _sum_3__B, _sum_3__C, _sum_3__D], typing.Callable[[_sum_3__A, _sum_3__B, _sum_3__C, _sum_3__D], int]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_sum_3__A, _sum_3__B, _sum_3__C, _sum_3__D, typing.Any, int]: ...
    @typing.overload
    @staticmethod
    def sum(toIntTriFunction: typing.Union[org.optaplanner.core.api.function.ToIntTriFunction[_sum_4__A, _sum_4__B, _sum_4__C], typing.Callable[[_sum_4__A, _sum_4__B, _sum_4__C], int]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_sum_4__A, _sum_4__B, _sum_4__C, typing.Any, int]: ...
    @typing.overload
    @staticmethod
    def sum(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_sum_5__A, _sum_5__B, _sum_5__C, _sum_5__Result], typing.Callable[[_sum_5__A, _sum_5__B, _sum_5__C], _sum_5__Result]], result: _sum_5__Result, binaryOperator: typing.Union[java.util.function.BinaryOperator[_sum_5__Result], typing.Callable], binaryOperator2: typing.Union[java.util.function.BinaryOperator[_sum_5__Result], typing.Callable]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_sum_5__A, _sum_5__B, _sum_5__C, typing.Any, _sum_5__Result]: ...
    @typing.overload
    @staticmethod
    def sum(function: typing.Union[java.util.function.Function[_sum_6__A, _sum_6__Result], typing.Callable[[_sum_6__A], _sum_6__Result]], result: _sum_6__Result, binaryOperator: typing.Union[java.util.function.BinaryOperator[_sum_6__Result], typing.Callable], binaryOperator2: typing.Union[java.util.function.BinaryOperator[_sum_6__Result], typing.Callable]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_sum_6__A, typing.Any, _sum_6__Result]: ...
    @typing.overload
    @staticmethod
    def sum(toIntFunction: typing.Union[java.util.function.ToIntFunction[_sum_7__A], typing.Callable[[_sum_7__A], int]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_sum_7__A, typing.Any, int]: ...
    _sumBigDecimal_0__A = typing.TypeVar('_sumBigDecimal_0__A')  # <A>
    _sumBigDecimal_0__B = typing.TypeVar('_sumBigDecimal_0__B')  # <B>
    _sumBigDecimal_1__A = typing.TypeVar('_sumBigDecimal_1__A')  # <A>
    _sumBigDecimal_1__B = typing.TypeVar('_sumBigDecimal_1__B')  # <B>
    _sumBigDecimal_1__C = typing.TypeVar('_sumBigDecimal_1__C')  # <C>
    _sumBigDecimal_1__D = typing.TypeVar('_sumBigDecimal_1__D')  # <D>
    _sumBigDecimal_2__A = typing.TypeVar('_sumBigDecimal_2__A')  # <A>
    _sumBigDecimal_2__B = typing.TypeVar('_sumBigDecimal_2__B')  # <B>
    _sumBigDecimal_2__C = typing.TypeVar('_sumBigDecimal_2__C')  # <C>
    _sumBigDecimal_3__A = typing.TypeVar('_sumBigDecimal_3__A')  # <A>
    @typing.overload
    @staticmethod
    def sumBigDecimal(biFunction: typing.Union[java.util.function.BiFunction[_sumBigDecimal_0__A, _sumBigDecimal_0__B, typing.Union[java.math.BigDecimal, decimal.Decimal]], typing.Callable[[_sumBigDecimal_0__A, _sumBigDecimal_0__B], typing.Union[java.math.BigDecimal, decimal.Decimal]]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_sumBigDecimal_0__A, _sumBigDecimal_0__B, typing.Any, java.math.BigDecimal]: ...
    @typing.overload
    @staticmethod
    def sumBigDecimal(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_sumBigDecimal_1__A, _sumBigDecimal_1__B, _sumBigDecimal_1__C, _sumBigDecimal_1__D, typing.Union[java.math.BigDecimal, decimal.Decimal]], typing.Callable[[_sumBigDecimal_1__A, _sumBigDecimal_1__B, _sumBigDecimal_1__C, _sumBigDecimal_1__D], typing.Union[java.math.BigDecimal, decimal.Decimal]]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_sumBigDecimal_1__A, _sumBigDecimal_1__B, _sumBigDecimal_1__C, _sumBigDecimal_1__D, typing.Any, java.math.BigDecimal]: ...
    @typing.overload
    @staticmethod
    def sumBigDecimal(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_sumBigDecimal_2__A, _sumBigDecimal_2__B, _sumBigDecimal_2__C, typing.Union[java.math.BigDecimal, decimal.Decimal]], typing.Callable[[_sumBigDecimal_2__A, _sumBigDecimal_2__B, _sumBigDecimal_2__C], typing.Union[java.math.BigDecimal, decimal.Decimal]]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_sumBigDecimal_2__A, _sumBigDecimal_2__B, _sumBigDecimal_2__C, typing.Any, java.math.BigDecimal]: ...
    @typing.overload
    @staticmethod
    def sumBigDecimal(function: typing.Union[java.util.function.Function[_sumBigDecimal_3__A, typing.Union[java.math.BigDecimal, decimal.Decimal]], typing.Callable[[_sumBigDecimal_3__A], typing.Union[java.math.BigDecimal, decimal.Decimal]]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_sumBigDecimal_3__A, typing.Any, java.math.BigDecimal]: ...
    _sumBigInteger_0__A = typing.TypeVar('_sumBigInteger_0__A')  # <A>
    _sumBigInteger_0__B = typing.TypeVar('_sumBigInteger_0__B')  # <B>
    _sumBigInteger_1__A = typing.TypeVar('_sumBigInteger_1__A')  # <A>
    _sumBigInteger_1__B = typing.TypeVar('_sumBigInteger_1__B')  # <B>
    _sumBigInteger_1__C = typing.TypeVar('_sumBigInteger_1__C')  # <C>
    _sumBigInteger_1__D = typing.TypeVar('_sumBigInteger_1__D')  # <D>
    _sumBigInteger_2__A = typing.TypeVar('_sumBigInteger_2__A')  # <A>
    _sumBigInteger_2__B = typing.TypeVar('_sumBigInteger_2__B')  # <B>
    _sumBigInteger_2__C = typing.TypeVar('_sumBigInteger_2__C')  # <C>
    _sumBigInteger_3__A = typing.TypeVar('_sumBigInteger_3__A')  # <A>
    @typing.overload
    @staticmethod
    def sumBigInteger(biFunction: typing.Union[java.util.function.BiFunction[_sumBigInteger_0__A, _sumBigInteger_0__B, java.math.BigInteger], typing.Callable[[_sumBigInteger_0__A, _sumBigInteger_0__B], java.math.BigInteger]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_sumBigInteger_0__A, _sumBigInteger_0__B, typing.Any, java.math.BigInteger]: ...
    @typing.overload
    @staticmethod
    def sumBigInteger(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_sumBigInteger_1__A, _sumBigInteger_1__B, _sumBigInteger_1__C, _sumBigInteger_1__D, java.math.BigInteger], typing.Callable[[_sumBigInteger_1__A, _sumBigInteger_1__B, _sumBigInteger_1__C, _sumBigInteger_1__D], java.math.BigInteger]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_sumBigInteger_1__A, _sumBigInteger_1__B, _sumBigInteger_1__C, _sumBigInteger_1__D, typing.Any, java.math.BigInteger]: ...
    @typing.overload
    @staticmethod
    def sumBigInteger(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_sumBigInteger_2__A, _sumBigInteger_2__B, _sumBigInteger_2__C, java.math.BigInteger], typing.Callable[[_sumBigInteger_2__A, _sumBigInteger_2__B, _sumBigInteger_2__C], java.math.BigInteger]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_sumBigInteger_2__A, _sumBigInteger_2__B, _sumBigInteger_2__C, typing.Any, java.math.BigInteger]: ...
    @typing.overload
    @staticmethod
    def sumBigInteger(function: typing.Union[java.util.function.Function[_sumBigInteger_3__A, java.math.BigInteger], typing.Callable[[_sumBigInteger_3__A], java.math.BigInteger]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_sumBigInteger_3__A, typing.Any, java.math.BigInteger]: ...
    _sumDuration_0__A = typing.TypeVar('_sumDuration_0__A')  # <A>
    _sumDuration_0__B = typing.TypeVar('_sumDuration_0__B')  # <B>
    _sumDuration_1__A = typing.TypeVar('_sumDuration_1__A')  # <A>
    _sumDuration_1__B = typing.TypeVar('_sumDuration_1__B')  # <B>
    _sumDuration_1__C = typing.TypeVar('_sumDuration_1__C')  # <C>
    _sumDuration_1__D = typing.TypeVar('_sumDuration_1__D')  # <D>
    _sumDuration_2__A = typing.TypeVar('_sumDuration_2__A')  # <A>
    _sumDuration_2__B = typing.TypeVar('_sumDuration_2__B')  # <B>
    _sumDuration_2__C = typing.TypeVar('_sumDuration_2__C')  # <C>
    _sumDuration_3__A = typing.TypeVar('_sumDuration_3__A')  # <A>
    @typing.overload
    @staticmethod
    def sumDuration(biFunction: typing.Union[java.util.function.BiFunction[_sumDuration_0__A, _sumDuration_0__B, java.time.Duration], typing.Callable[[_sumDuration_0__A, _sumDuration_0__B], java.time.Duration]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_sumDuration_0__A, _sumDuration_0__B, typing.Any, java.time.Duration]: ...
    @typing.overload
    @staticmethod
    def sumDuration(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_sumDuration_1__A, _sumDuration_1__B, _sumDuration_1__C, _sumDuration_1__D, java.time.Duration], typing.Callable[[_sumDuration_1__A, _sumDuration_1__B, _sumDuration_1__C, _sumDuration_1__D], java.time.Duration]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_sumDuration_1__A, _sumDuration_1__B, _sumDuration_1__C, _sumDuration_1__D, typing.Any, java.time.Duration]: ...
    @typing.overload
    @staticmethod
    def sumDuration(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_sumDuration_2__A, _sumDuration_2__B, _sumDuration_2__C, java.time.Duration], typing.Callable[[_sumDuration_2__A, _sumDuration_2__B, _sumDuration_2__C], java.time.Duration]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_sumDuration_2__A, _sumDuration_2__B, _sumDuration_2__C, typing.Any, java.time.Duration]: ...
    @typing.overload
    @staticmethod
    def sumDuration(function: typing.Union[java.util.function.Function[_sumDuration_3__A, java.time.Duration], typing.Callable[[_sumDuration_3__A], java.time.Duration]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_sumDuration_3__A, typing.Any, java.time.Duration]: ...
    _sumLong_0__A = typing.TypeVar('_sumLong_0__A')  # <A>
    _sumLong_0__B = typing.TypeVar('_sumLong_0__B')  # <B>
    _sumLong_1__A = typing.TypeVar('_sumLong_1__A')  # <A>
    _sumLong_1__B = typing.TypeVar('_sumLong_1__B')  # <B>
    _sumLong_1__C = typing.TypeVar('_sumLong_1__C')  # <C>
    _sumLong_1__D = typing.TypeVar('_sumLong_1__D')  # <D>
    _sumLong_2__A = typing.TypeVar('_sumLong_2__A')  # <A>
    _sumLong_2__B = typing.TypeVar('_sumLong_2__B')  # <B>
    _sumLong_2__C = typing.TypeVar('_sumLong_2__C')  # <C>
    _sumLong_3__A = typing.TypeVar('_sumLong_3__A')  # <A>
    @typing.overload
    @staticmethod
    def sumLong(toLongBiFunction: typing.Union[java.util.function.ToLongBiFunction[_sumLong_0__A, _sumLong_0__B], typing.Callable[[_sumLong_0__A, _sumLong_0__B], int]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_sumLong_0__A, _sumLong_0__B, typing.Any, int]: ...
    @typing.overload
    @staticmethod
    def sumLong(toLongQuadFunction: typing.Union[org.optaplanner.core.api.function.ToLongQuadFunction[_sumLong_1__A, _sumLong_1__B, _sumLong_1__C, _sumLong_1__D], typing.Callable[[_sumLong_1__A, _sumLong_1__B, _sumLong_1__C, _sumLong_1__D], int]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_sumLong_1__A, _sumLong_1__B, _sumLong_1__C, _sumLong_1__D, typing.Any, int]: ...
    @typing.overload
    @staticmethod
    def sumLong(toLongTriFunction: typing.Union[org.optaplanner.core.api.function.ToLongTriFunction[_sumLong_2__A, _sumLong_2__B, _sumLong_2__C], typing.Callable[[_sumLong_2__A, _sumLong_2__B, _sumLong_2__C], int]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_sumLong_2__A, _sumLong_2__B, _sumLong_2__C, typing.Any, int]: ...
    @typing.overload
    @staticmethod
    def sumLong(toLongFunction: typing.Union[java.util.function.ToLongFunction[_sumLong_3__A], typing.Callable[[_sumLong_3__A], int]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_sumLong_3__A, typing.Any, int]: ...
    _sumPeriod_0__A = typing.TypeVar('_sumPeriod_0__A')  # <A>
    _sumPeriod_0__B = typing.TypeVar('_sumPeriod_0__B')  # <B>
    _sumPeriod_1__A = typing.TypeVar('_sumPeriod_1__A')  # <A>
    _sumPeriod_1__B = typing.TypeVar('_sumPeriod_1__B')  # <B>
    _sumPeriod_1__C = typing.TypeVar('_sumPeriod_1__C')  # <C>
    _sumPeriod_1__D = typing.TypeVar('_sumPeriod_1__D')  # <D>
    _sumPeriod_2__A = typing.TypeVar('_sumPeriod_2__A')  # <A>
    _sumPeriod_2__B = typing.TypeVar('_sumPeriod_2__B')  # <B>
    _sumPeriod_2__C = typing.TypeVar('_sumPeriod_2__C')  # <C>
    _sumPeriod_3__A = typing.TypeVar('_sumPeriod_3__A')  # <A>
    @typing.overload
    @staticmethod
    def sumPeriod(biFunction: typing.Union[java.util.function.BiFunction[_sumPeriod_0__A, _sumPeriod_0__B, java.time.Period], typing.Callable[[_sumPeriod_0__A, _sumPeriod_0__B], java.time.Period]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_sumPeriod_0__A, _sumPeriod_0__B, typing.Any, java.time.Period]: ...
    @typing.overload
    @staticmethod
    def sumPeriod(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_sumPeriod_1__A, _sumPeriod_1__B, _sumPeriod_1__C, _sumPeriod_1__D, java.time.Period], typing.Callable[[_sumPeriod_1__A, _sumPeriod_1__B, _sumPeriod_1__C, _sumPeriod_1__D], java.time.Period]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_sumPeriod_1__A, _sumPeriod_1__B, _sumPeriod_1__C, _sumPeriod_1__D, typing.Any, java.time.Period]: ...
    @typing.overload
    @staticmethod
    def sumPeriod(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_sumPeriod_2__A, _sumPeriod_2__B, _sumPeriod_2__C, java.time.Period], typing.Callable[[_sumPeriod_2__A, _sumPeriod_2__B, _sumPeriod_2__C], java.time.Period]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_sumPeriod_2__A, _sumPeriod_2__B, _sumPeriod_2__C, typing.Any, java.time.Period]: ...
    @typing.overload
    @staticmethod
    def sumPeriod(function: typing.Union[java.util.function.Function[_sumPeriod_3__A, java.time.Period], typing.Callable[[_sumPeriod_3__A], java.time.Period]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_sumPeriod_3__A, typing.Any, java.time.Period]: ...
    _toCollection_0__A = typing.TypeVar('_toCollection_0__A')  # <A>
    _toCollection_0__B = typing.TypeVar('_toCollection_0__B')  # <B>
    _toCollection_0__Mapped = typing.TypeVar('_toCollection_0__Mapped')  # <Mapped>
    _toCollection_0__Result = typing.TypeVar('_toCollection_0__Result', bound=java.util.Collection)  # <Result>
    _toCollection_1__A = typing.TypeVar('_toCollection_1__A')  # <A>
    _toCollection_1__B = typing.TypeVar('_toCollection_1__B')  # <B>
    _toCollection_1__C = typing.TypeVar('_toCollection_1__C')  # <C>
    _toCollection_1__D = typing.TypeVar('_toCollection_1__D')  # <D>
    _toCollection_1__Mapped = typing.TypeVar('_toCollection_1__Mapped')  # <Mapped>
    _toCollection_1__Result = typing.TypeVar('_toCollection_1__Result', bound=java.util.Collection)  # <Result>
    _toCollection_2__A = typing.TypeVar('_toCollection_2__A')  # <A>
    _toCollection_2__B = typing.TypeVar('_toCollection_2__B')  # <B>
    _toCollection_2__C = typing.TypeVar('_toCollection_2__C')  # <C>
    _toCollection_2__Mapped = typing.TypeVar('_toCollection_2__Mapped')  # <Mapped>
    _toCollection_2__Result = typing.TypeVar('_toCollection_2__Result', bound=java.util.Collection)  # <Result>
    _toCollection_3__A = typing.TypeVar('_toCollection_3__A')  # <A>
    _toCollection_3__Mapped = typing.TypeVar('_toCollection_3__Mapped')  # <Mapped>
    _toCollection_3__Result = typing.TypeVar('_toCollection_3__Result', bound=java.util.Collection)  # <Result>
    _toCollection_4__A = typing.TypeVar('_toCollection_4__A')  # <A>
    _toCollection_4__Result = typing.TypeVar('_toCollection_4__Result', bound=java.util.Collection)  # <Result>
    @typing.overload
    @staticmethod
    def toCollection(biFunction: typing.Union[java.util.function.BiFunction[_toCollection_0__A, _toCollection_0__B, _toCollection_0__Mapped], typing.Callable[[_toCollection_0__A, _toCollection_0__B], _toCollection_0__Mapped]], intFunction: typing.Union[java.util.function.IntFunction[_toCollection_0__Result], typing.Callable[[int], _toCollection_0__Result]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_toCollection_0__A, _toCollection_0__B, typing.Any, _toCollection_0__Result]: ...
    @typing.overload
    @staticmethod
    def toCollection(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toCollection_1__A, _toCollection_1__B, _toCollection_1__C, _toCollection_1__D, _toCollection_1__Mapped], typing.Callable[[_toCollection_1__A, _toCollection_1__B, _toCollection_1__C, _toCollection_1__D], _toCollection_1__Mapped]], intFunction: typing.Union[java.util.function.IntFunction[_toCollection_1__Result], typing.Callable[[int], _toCollection_1__Result]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_toCollection_1__A, _toCollection_1__B, _toCollection_1__C, _toCollection_1__D, typing.Any, _toCollection_1__Result]: ...
    @typing.overload
    @staticmethod
    def toCollection(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_toCollection_2__A, _toCollection_2__B, _toCollection_2__C, _toCollection_2__Mapped], typing.Callable[[_toCollection_2__A, _toCollection_2__B, _toCollection_2__C], _toCollection_2__Mapped]], intFunction: typing.Union[java.util.function.IntFunction[_toCollection_2__Result], typing.Callable[[int], _toCollection_2__Result]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_toCollection_2__A, _toCollection_2__B, _toCollection_2__C, typing.Any, _toCollection_2__Result]: ...
    @typing.overload
    @staticmethod
    def toCollection(function: typing.Union[java.util.function.Function[_toCollection_3__A, _toCollection_3__Mapped], typing.Callable[[_toCollection_3__A], _toCollection_3__Mapped]], intFunction: typing.Union[java.util.function.IntFunction[_toCollection_3__Result], typing.Callable[[int], _toCollection_3__Result]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_toCollection_3__A, typing.Any, _toCollection_3__Result]: ...
    @typing.overload
    @staticmethod
    def toCollection(intFunction: typing.Union[java.util.function.IntFunction[_toCollection_4__Result], typing.Callable[[int], _toCollection_4__Result]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_toCollection_4__A, typing.Any, _toCollection_4__Result]: ...
    _toList_0__A = typing.TypeVar('_toList_0__A')  # <A>
    _toList_0__B = typing.TypeVar('_toList_0__B')  # <B>
    _toList_0__Mapped = typing.TypeVar('_toList_0__Mapped')  # <Mapped>
    _toList_1__A = typing.TypeVar('_toList_1__A')  # <A>
    _toList_1__B = typing.TypeVar('_toList_1__B')  # <B>
    _toList_1__C = typing.TypeVar('_toList_1__C')  # <C>
    _toList_1__D = typing.TypeVar('_toList_1__D')  # <D>
    _toList_1__Mapped = typing.TypeVar('_toList_1__Mapped')  # <Mapped>
    _toList_2__A = typing.TypeVar('_toList_2__A')  # <A>
    _toList_2__B = typing.TypeVar('_toList_2__B')  # <B>
    _toList_2__C = typing.TypeVar('_toList_2__C')  # <C>
    _toList_2__Mapped = typing.TypeVar('_toList_2__Mapped')  # <Mapped>
    _toList_3__A = typing.TypeVar('_toList_3__A')  # <A>
    _toList_4__A = typing.TypeVar('_toList_4__A')  # <A>
    _toList_4__Mapped = typing.TypeVar('_toList_4__Mapped')  # <Mapped>
    @typing.overload
    @staticmethod
    def toList(biFunction: typing.Union[java.util.function.BiFunction[_toList_0__A, _toList_0__B, _toList_0__Mapped], typing.Callable[[_toList_0__A, _toList_0__B], _toList_0__Mapped]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_toList_0__A, _toList_0__B, typing.Any, java.util.List[_toList_0__Mapped]]: ...
    @typing.overload
    @staticmethod
    def toList(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toList_1__A, _toList_1__B, _toList_1__C, _toList_1__D, _toList_1__Mapped], typing.Callable[[_toList_1__A, _toList_1__B, _toList_1__C, _toList_1__D], _toList_1__Mapped]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_toList_1__A, _toList_1__B, _toList_1__C, _toList_1__D, typing.Any, java.util.List[_toList_1__Mapped]]: ...
    @typing.overload
    @staticmethod
    def toList(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_toList_2__A, _toList_2__B, _toList_2__C, _toList_2__Mapped], typing.Callable[[_toList_2__A, _toList_2__B, _toList_2__C], _toList_2__Mapped]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_toList_2__A, _toList_2__B, _toList_2__C, typing.Any, java.util.List[_toList_2__Mapped]]: ...
    @typing.overload
    @staticmethod
    def toList() -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_toList_3__A, typing.Any, java.util.List[_toList_3__A]]: ...
    @typing.overload
    @staticmethod
    def toList(function: typing.Union[java.util.function.Function[_toList_4__A, _toList_4__Mapped], typing.Callable[[_toList_4__A], _toList_4__Mapped]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_toList_4__A, typing.Any, java.util.List[_toList_4__Mapped]]: ...
    _toMap_0__A = typing.TypeVar('_toMap_0__A')  # <A>
    _toMap_0__B = typing.TypeVar('_toMap_0__B')  # <B>
    _toMap_0__Key = typing.TypeVar('_toMap_0__Key')  # <Key>
    _toMap_0__Value = typing.TypeVar('_toMap_0__Value')  # <Value>
    _toMap_1__A = typing.TypeVar('_toMap_1__A')  # <A>
    _toMap_1__B = typing.TypeVar('_toMap_1__B')  # <B>
    _toMap_1__Key = typing.TypeVar('_toMap_1__Key')  # <Key>
    _toMap_1__Value = typing.TypeVar('_toMap_1__Value')  # <Value>
    _toMap_2__A = typing.TypeVar('_toMap_2__A')  # <A>
    _toMap_2__B = typing.TypeVar('_toMap_2__B')  # <B>
    _toMap_2__Key = typing.TypeVar('_toMap_2__Key')  # <Key>
    _toMap_2__Value = typing.TypeVar('_toMap_2__Value')  # <Value>
    _toMap_2__ValueSet = typing.TypeVar('_toMap_2__ValueSet', bound=java.util.Set)  # <ValueSet>
    _toMap_3__A = typing.TypeVar('_toMap_3__A')  # <A>
    _toMap_3__B = typing.TypeVar('_toMap_3__B')  # <B>
    _toMap_3__C = typing.TypeVar('_toMap_3__C')  # <C>
    _toMap_3__D = typing.TypeVar('_toMap_3__D')  # <D>
    _toMap_3__Key = typing.TypeVar('_toMap_3__Key')  # <Key>
    _toMap_3__Value = typing.TypeVar('_toMap_3__Value')  # <Value>
    _toMap_4__A = typing.TypeVar('_toMap_4__A')  # <A>
    _toMap_4__B = typing.TypeVar('_toMap_4__B')  # <B>
    _toMap_4__C = typing.TypeVar('_toMap_4__C')  # <C>
    _toMap_4__D = typing.TypeVar('_toMap_4__D')  # <D>
    _toMap_4__Key = typing.TypeVar('_toMap_4__Key')  # <Key>
    _toMap_4__Value = typing.TypeVar('_toMap_4__Value')  # <Value>
    _toMap_5__A = typing.TypeVar('_toMap_5__A')  # <A>
    _toMap_5__B = typing.TypeVar('_toMap_5__B')  # <B>
    _toMap_5__C = typing.TypeVar('_toMap_5__C')  # <C>
    _toMap_5__D = typing.TypeVar('_toMap_5__D')  # <D>
    _toMap_5__Key = typing.TypeVar('_toMap_5__Key')  # <Key>
    _toMap_5__Value = typing.TypeVar('_toMap_5__Value')  # <Value>
    _toMap_5__ValueSet = typing.TypeVar('_toMap_5__ValueSet', bound=java.util.Set)  # <ValueSet>
    _toMap_6__A = typing.TypeVar('_toMap_6__A')  # <A>
    _toMap_6__B = typing.TypeVar('_toMap_6__B')  # <B>
    _toMap_6__C = typing.TypeVar('_toMap_6__C')  # <C>
    _toMap_6__Key = typing.TypeVar('_toMap_6__Key')  # <Key>
    _toMap_6__Value = typing.TypeVar('_toMap_6__Value')  # <Value>
    _toMap_7__A = typing.TypeVar('_toMap_7__A')  # <A>
    _toMap_7__B = typing.TypeVar('_toMap_7__B')  # <B>
    _toMap_7__C = typing.TypeVar('_toMap_7__C')  # <C>
    _toMap_7__Key = typing.TypeVar('_toMap_7__Key')  # <Key>
    _toMap_7__Value = typing.TypeVar('_toMap_7__Value')  # <Value>
    _toMap_8__A = typing.TypeVar('_toMap_8__A')  # <A>
    _toMap_8__B = typing.TypeVar('_toMap_8__B')  # <B>
    _toMap_8__C = typing.TypeVar('_toMap_8__C')  # <C>
    _toMap_8__Key = typing.TypeVar('_toMap_8__Key')  # <Key>
    _toMap_8__Value = typing.TypeVar('_toMap_8__Value')  # <Value>
    _toMap_8__ValueSet = typing.TypeVar('_toMap_8__ValueSet', bound=java.util.Set)  # <ValueSet>
    _toMap_9__A = typing.TypeVar('_toMap_9__A')  # <A>
    _toMap_9__Key = typing.TypeVar('_toMap_9__Key')  # <Key>
    _toMap_9__Value = typing.TypeVar('_toMap_9__Value')  # <Value>
    _toMap_10__A = typing.TypeVar('_toMap_10__A')  # <A>
    _toMap_10__Key = typing.TypeVar('_toMap_10__Key')  # <Key>
    _toMap_10__Value = typing.TypeVar('_toMap_10__Value')  # <Value>
    _toMap_11__A = typing.TypeVar('_toMap_11__A')  # <A>
    _toMap_11__Key = typing.TypeVar('_toMap_11__Key')  # <Key>
    _toMap_11__Value = typing.TypeVar('_toMap_11__Value')  # <Value>
    _toMap_11__ValueSet = typing.TypeVar('_toMap_11__ValueSet', bound=java.util.Set)  # <ValueSet>
    @typing.overload
    @staticmethod
    def toMap(biFunction: typing.Union[java.util.function.BiFunction[_toMap_0__A, _toMap_0__B, _toMap_0__Key], typing.Callable[[_toMap_0__A, _toMap_0__B], _toMap_0__Key]], biFunction2: typing.Union[java.util.function.BiFunction[_toMap_0__A, _toMap_0__B, _toMap_0__Value], typing.Callable[[_toMap_0__A, _toMap_0__B], _toMap_0__Value]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_toMap_0__A, _toMap_0__B, typing.Any, java.util.Map[_toMap_0__Key, java.util.Set[_toMap_0__Value]]]: ...
    @typing.overload
    @staticmethod
    def toMap(biFunction: typing.Union[java.util.function.BiFunction[_toMap_1__A, _toMap_1__B, _toMap_1__Key], typing.Callable[[_toMap_1__A, _toMap_1__B], _toMap_1__Key]], biFunction2: typing.Union[java.util.function.BiFunction[_toMap_1__A, _toMap_1__B, _toMap_1__Value], typing.Callable[[_toMap_1__A, _toMap_1__B], _toMap_1__Value]], binaryOperator: typing.Union[java.util.function.BinaryOperator[_toMap_1__Value], typing.Callable]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_toMap_1__A, _toMap_1__B, typing.Any, java.util.Map[_toMap_1__Key, _toMap_1__Value]]: ...
    @typing.overload
    @staticmethod
    def toMap(biFunction: typing.Union[java.util.function.BiFunction[_toMap_2__A, _toMap_2__B, _toMap_2__Key], typing.Callable[[_toMap_2__A, _toMap_2__B], _toMap_2__Key]], biFunction2: typing.Union[java.util.function.BiFunction[_toMap_2__A, _toMap_2__B, _toMap_2__Value], typing.Callable[[_toMap_2__A, _toMap_2__B], _toMap_2__Value]], intFunction: typing.Union[java.util.function.IntFunction[_toMap_2__ValueSet], typing.Callable[[int], _toMap_2__ValueSet]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_toMap_2__A, _toMap_2__B, typing.Any, java.util.Map[_toMap_2__Key, _toMap_2__ValueSet]]: ...
    @typing.overload
    @staticmethod
    def toMap(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toMap_3__A, _toMap_3__B, _toMap_3__C, _toMap_3__D, _toMap_3__Key], typing.Callable[[_toMap_3__A, _toMap_3__B, _toMap_3__C, _toMap_3__D], _toMap_3__Key]], quadFunction2: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toMap_3__A, _toMap_3__B, _toMap_3__C, _toMap_3__D, _toMap_3__Value], typing.Callable[[_toMap_3__A, _toMap_3__B, _toMap_3__C, _toMap_3__D], _toMap_3__Value]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_toMap_3__A, _toMap_3__B, _toMap_3__C, _toMap_3__D, typing.Any, java.util.Map[_toMap_3__Key, java.util.Set[_toMap_3__Value]]]: ...
    @typing.overload
    @staticmethod
    def toMap(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toMap_4__A, _toMap_4__B, _toMap_4__C, _toMap_4__D, _toMap_4__Key], typing.Callable[[_toMap_4__A, _toMap_4__B, _toMap_4__C, _toMap_4__D], _toMap_4__Key]], quadFunction2: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toMap_4__A, _toMap_4__B, _toMap_4__C, _toMap_4__D, _toMap_4__Value], typing.Callable[[_toMap_4__A, _toMap_4__B, _toMap_4__C, _toMap_4__D], _toMap_4__Value]], binaryOperator: typing.Union[java.util.function.BinaryOperator[_toMap_4__Value], typing.Callable]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_toMap_4__A, _toMap_4__B, _toMap_4__C, _toMap_4__D, typing.Any, java.util.Map[_toMap_4__Key, _toMap_4__Value]]: ...
    @typing.overload
    @staticmethod
    def toMap(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toMap_5__A, _toMap_5__B, _toMap_5__C, _toMap_5__D, _toMap_5__Key], typing.Callable[[_toMap_5__A, _toMap_5__B, _toMap_5__C, _toMap_5__D], _toMap_5__Key]], quadFunction2: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toMap_5__A, _toMap_5__B, _toMap_5__C, _toMap_5__D, _toMap_5__Value], typing.Callable[[_toMap_5__A, _toMap_5__B, _toMap_5__C, _toMap_5__D], _toMap_5__Value]], intFunction: typing.Union[java.util.function.IntFunction[_toMap_5__ValueSet], typing.Callable[[int], _toMap_5__ValueSet]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_toMap_5__A, _toMap_5__B, _toMap_5__C, _toMap_5__D, typing.Any, java.util.Map[_toMap_5__Key, _toMap_5__ValueSet]]: ...
    @typing.overload
    @staticmethod
    def toMap(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_toMap_6__A, _toMap_6__B, _toMap_6__C, _toMap_6__Key], typing.Callable[[_toMap_6__A, _toMap_6__B, _toMap_6__C], _toMap_6__Key]], triFunction2: typing.Union[org.optaplanner.core.api.function.TriFunction[_toMap_6__A, _toMap_6__B, _toMap_6__C, _toMap_6__Value], typing.Callable[[_toMap_6__A, _toMap_6__B, _toMap_6__C], _toMap_6__Value]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_toMap_6__A, _toMap_6__B, _toMap_6__C, typing.Any, java.util.Map[_toMap_6__Key, java.util.Set[_toMap_6__Value]]]: ...
    @typing.overload
    @staticmethod
    def toMap(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_toMap_7__A, _toMap_7__B, _toMap_7__C, _toMap_7__Key], typing.Callable[[_toMap_7__A, _toMap_7__B, _toMap_7__C], _toMap_7__Key]], triFunction2: typing.Union[org.optaplanner.core.api.function.TriFunction[_toMap_7__A, _toMap_7__B, _toMap_7__C, _toMap_7__Value], typing.Callable[[_toMap_7__A, _toMap_7__B, _toMap_7__C], _toMap_7__Value]], binaryOperator: typing.Union[java.util.function.BinaryOperator[_toMap_7__Value], typing.Callable]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_toMap_7__A, _toMap_7__B, _toMap_7__C, typing.Any, java.util.Map[_toMap_7__Key, _toMap_7__Value]]: ...
    @typing.overload
    @staticmethod
    def toMap(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_toMap_8__A, _toMap_8__B, _toMap_8__C, _toMap_8__Key], typing.Callable[[_toMap_8__A, _toMap_8__B, _toMap_8__C], _toMap_8__Key]], triFunction2: typing.Union[org.optaplanner.core.api.function.TriFunction[_toMap_8__A, _toMap_8__B, _toMap_8__C, _toMap_8__Value], typing.Callable[[_toMap_8__A, _toMap_8__B, _toMap_8__C], _toMap_8__Value]], intFunction: typing.Union[java.util.function.IntFunction[_toMap_8__ValueSet], typing.Callable[[int], _toMap_8__ValueSet]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_toMap_8__A, _toMap_8__B, _toMap_8__C, typing.Any, java.util.Map[_toMap_8__Key, _toMap_8__ValueSet]]: ...
    @typing.overload
    @staticmethod
    def toMap(function: typing.Union[java.util.function.Function[_toMap_9__A, _toMap_9__Key], typing.Callable[[_toMap_9__A], _toMap_9__Key]], function2: typing.Union[java.util.function.Function[_toMap_9__A, _toMap_9__Value], typing.Callable[[_toMap_9__A], _toMap_9__Value]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_toMap_9__A, typing.Any, java.util.Map[_toMap_9__Key, java.util.Set[_toMap_9__Value]]]: ...
    @typing.overload
    @staticmethod
    def toMap(function: typing.Union[java.util.function.Function[_toMap_10__A, _toMap_10__Key], typing.Callable[[_toMap_10__A], _toMap_10__Key]], function2: typing.Union[java.util.function.Function[_toMap_10__A, _toMap_10__Value], typing.Callable[[_toMap_10__A], _toMap_10__Value]], binaryOperator: typing.Union[java.util.function.BinaryOperator[_toMap_10__Value], typing.Callable]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_toMap_10__A, typing.Any, java.util.Map[_toMap_10__Key, _toMap_10__Value]]: ...
    @typing.overload
    @staticmethod
    def toMap(function: typing.Union[java.util.function.Function[_toMap_11__A, _toMap_11__Key], typing.Callable[[_toMap_11__A], _toMap_11__Key]], function2: typing.Union[java.util.function.Function[_toMap_11__A, _toMap_11__Value], typing.Callable[[_toMap_11__A], _toMap_11__Value]], intFunction: typing.Union[java.util.function.IntFunction[_toMap_11__ValueSet], typing.Callable[[int], _toMap_11__ValueSet]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_toMap_11__A, typing.Any, java.util.Map[_toMap_11__Key, _toMap_11__ValueSet]]: ...
    _toSet_0__A = typing.TypeVar('_toSet_0__A')  # <A>
    _toSet_0__B = typing.TypeVar('_toSet_0__B')  # <B>
    _toSet_0__Mapped = typing.TypeVar('_toSet_0__Mapped')  # <Mapped>
    _toSet_1__A = typing.TypeVar('_toSet_1__A')  # <A>
    _toSet_1__B = typing.TypeVar('_toSet_1__B')  # <B>
    _toSet_1__C = typing.TypeVar('_toSet_1__C')  # <C>
    _toSet_1__D = typing.TypeVar('_toSet_1__D')  # <D>
    _toSet_1__Mapped = typing.TypeVar('_toSet_1__Mapped')  # <Mapped>
    _toSet_2__A = typing.TypeVar('_toSet_2__A')  # <A>
    _toSet_2__B = typing.TypeVar('_toSet_2__B')  # <B>
    _toSet_2__C = typing.TypeVar('_toSet_2__C')  # <C>
    _toSet_2__Mapped = typing.TypeVar('_toSet_2__Mapped')  # <Mapped>
    _toSet_3__A = typing.TypeVar('_toSet_3__A')  # <A>
    _toSet_4__A = typing.TypeVar('_toSet_4__A')  # <A>
    _toSet_4__Mapped = typing.TypeVar('_toSet_4__Mapped')  # <Mapped>
    @typing.overload
    @staticmethod
    def toSet(biFunction: typing.Union[java.util.function.BiFunction[_toSet_0__A, _toSet_0__B, _toSet_0__Mapped], typing.Callable[[_toSet_0__A, _toSet_0__B], _toSet_0__Mapped]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_toSet_0__A, _toSet_0__B, typing.Any, java.util.Set[_toSet_0__Mapped]]: ...
    @typing.overload
    @staticmethod
    def toSet(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toSet_1__A, _toSet_1__B, _toSet_1__C, _toSet_1__D, _toSet_1__Mapped], typing.Callable[[_toSet_1__A, _toSet_1__B, _toSet_1__C, _toSet_1__D], _toSet_1__Mapped]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_toSet_1__A, _toSet_1__B, _toSet_1__C, _toSet_1__D, typing.Any, java.util.Set[_toSet_1__Mapped]]: ...
    @typing.overload
    @staticmethod
    def toSet(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_toSet_2__A, _toSet_2__B, _toSet_2__C, _toSet_2__Mapped], typing.Callable[[_toSet_2__A, _toSet_2__B, _toSet_2__C], _toSet_2__Mapped]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_toSet_2__A, _toSet_2__B, _toSet_2__C, typing.Any, java.util.Set[_toSet_2__Mapped]]: ...
    @typing.overload
    @staticmethod
    def toSet() -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_toSet_3__A, typing.Any, java.util.Set[_toSet_3__A]]: ...
    @typing.overload
    @staticmethod
    def toSet(function: typing.Union[java.util.function.Function[_toSet_4__A, _toSet_4__Mapped], typing.Callable[[_toSet_4__A], _toSet_4__Mapped]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_toSet_4__A, typing.Any, java.util.Set[_toSet_4__Mapped]]: ...
    _toSortedMap_0__A = typing.TypeVar('_toSortedMap_0__A')  # <A>
    _toSortedMap_0__B = typing.TypeVar('_toSortedMap_0__B')  # <B>
    _toSortedMap_0__Key = typing.TypeVar('_toSortedMap_0__Key', bound=java.lang.Comparable)  # <Key>
    _toSortedMap_0__Value = typing.TypeVar('_toSortedMap_0__Value')  # <Value>
    _toSortedMap_1__A = typing.TypeVar('_toSortedMap_1__A')  # <A>
    _toSortedMap_1__B = typing.TypeVar('_toSortedMap_1__B')  # <B>
    _toSortedMap_1__Key = typing.TypeVar('_toSortedMap_1__Key', bound=java.lang.Comparable)  # <Key>
    _toSortedMap_1__Value = typing.TypeVar('_toSortedMap_1__Value')  # <Value>
    _toSortedMap_2__A = typing.TypeVar('_toSortedMap_2__A')  # <A>
    _toSortedMap_2__B = typing.TypeVar('_toSortedMap_2__B')  # <B>
    _toSortedMap_2__Key = typing.TypeVar('_toSortedMap_2__Key', bound=java.lang.Comparable)  # <Key>
    _toSortedMap_2__Value = typing.TypeVar('_toSortedMap_2__Value')  # <Value>
    _toSortedMap_2__ValueSet = typing.TypeVar('_toSortedMap_2__ValueSet', bound=java.util.Set)  # <ValueSet>
    _toSortedMap_3__A = typing.TypeVar('_toSortedMap_3__A')  # <A>
    _toSortedMap_3__B = typing.TypeVar('_toSortedMap_3__B')  # <B>
    _toSortedMap_3__C = typing.TypeVar('_toSortedMap_3__C')  # <C>
    _toSortedMap_3__D = typing.TypeVar('_toSortedMap_3__D')  # <D>
    _toSortedMap_3__Key = typing.TypeVar('_toSortedMap_3__Key', bound=java.lang.Comparable)  # <Key>
    _toSortedMap_3__Value = typing.TypeVar('_toSortedMap_3__Value')  # <Value>
    _toSortedMap_4__A = typing.TypeVar('_toSortedMap_4__A')  # <A>
    _toSortedMap_4__B = typing.TypeVar('_toSortedMap_4__B')  # <B>
    _toSortedMap_4__C = typing.TypeVar('_toSortedMap_4__C')  # <C>
    _toSortedMap_4__D = typing.TypeVar('_toSortedMap_4__D')  # <D>
    _toSortedMap_4__Key = typing.TypeVar('_toSortedMap_4__Key', bound=java.lang.Comparable)  # <Key>
    _toSortedMap_4__Value = typing.TypeVar('_toSortedMap_4__Value')  # <Value>
    _toSortedMap_5__A = typing.TypeVar('_toSortedMap_5__A')  # <A>
    _toSortedMap_5__B = typing.TypeVar('_toSortedMap_5__B')  # <B>
    _toSortedMap_5__C = typing.TypeVar('_toSortedMap_5__C')  # <C>
    _toSortedMap_5__D = typing.TypeVar('_toSortedMap_5__D')  # <D>
    _toSortedMap_5__Key = typing.TypeVar('_toSortedMap_5__Key', bound=java.lang.Comparable)  # <Key>
    _toSortedMap_5__Value = typing.TypeVar('_toSortedMap_5__Value')  # <Value>
    _toSortedMap_5__ValueSet = typing.TypeVar('_toSortedMap_5__ValueSet', bound=java.util.Set)  # <ValueSet>
    _toSortedMap_6__A = typing.TypeVar('_toSortedMap_6__A')  # <A>
    _toSortedMap_6__B = typing.TypeVar('_toSortedMap_6__B')  # <B>
    _toSortedMap_6__C = typing.TypeVar('_toSortedMap_6__C')  # <C>
    _toSortedMap_6__Key = typing.TypeVar('_toSortedMap_6__Key', bound=java.lang.Comparable)  # <Key>
    _toSortedMap_6__Value = typing.TypeVar('_toSortedMap_6__Value')  # <Value>
    _toSortedMap_7__A = typing.TypeVar('_toSortedMap_7__A')  # <A>
    _toSortedMap_7__B = typing.TypeVar('_toSortedMap_7__B')  # <B>
    _toSortedMap_7__C = typing.TypeVar('_toSortedMap_7__C')  # <C>
    _toSortedMap_7__Key = typing.TypeVar('_toSortedMap_7__Key', bound=java.lang.Comparable)  # <Key>
    _toSortedMap_7__Value = typing.TypeVar('_toSortedMap_7__Value')  # <Value>
    _toSortedMap_8__A = typing.TypeVar('_toSortedMap_8__A')  # <A>
    _toSortedMap_8__B = typing.TypeVar('_toSortedMap_8__B')  # <B>
    _toSortedMap_8__C = typing.TypeVar('_toSortedMap_8__C')  # <C>
    _toSortedMap_8__Key = typing.TypeVar('_toSortedMap_8__Key', bound=java.lang.Comparable)  # <Key>
    _toSortedMap_8__Value = typing.TypeVar('_toSortedMap_8__Value')  # <Value>
    _toSortedMap_8__ValueSet = typing.TypeVar('_toSortedMap_8__ValueSet', bound=java.util.Set)  # <ValueSet>
    _toSortedMap_9__A = typing.TypeVar('_toSortedMap_9__A')  # <A>
    _toSortedMap_9__Key = typing.TypeVar('_toSortedMap_9__Key', bound=java.lang.Comparable)  # <Key>
    _toSortedMap_9__Value = typing.TypeVar('_toSortedMap_9__Value')  # <Value>
    _toSortedMap_10__A = typing.TypeVar('_toSortedMap_10__A')  # <A>
    _toSortedMap_10__Key = typing.TypeVar('_toSortedMap_10__Key', bound=java.lang.Comparable)  # <Key>
    _toSortedMap_10__Value = typing.TypeVar('_toSortedMap_10__Value')  # <Value>
    _toSortedMap_11__A = typing.TypeVar('_toSortedMap_11__A')  # <A>
    _toSortedMap_11__Key = typing.TypeVar('_toSortedMap_11__Key', bound=java.lang.Comparable)  # <Key>
    _toSortedMap_11__Value = typing.TypeVar('_toSortedMap_11__Value')  # <Value>
    _toSortedMap_11__ValueSet = typing.TypeVar('_toSortedMap_11__ValueSet', bound=java.util.Set)  # <ValueSet>
    @typing.overload
    @staticmethod
    def toSortedMap(biFunction: typing.Union[java.util.function.BiFunction[_toSortedMap_0__A, _toSortedMap_0__B, _toSortedMap_0__Key], typing.Callable[[_toSortedMap_0__A, _toSortedMap_0__B], _toSortedMap_0__Key]], biFunction2: typing.Union[java.util.function.BiFunction[_toSortedMap_0__A, _toSortedMap_0__B, _toSortedMap_0__Value], typing.Callable[[_toSortedMap_0__A, _toSortedMap_0__B], _toSortedMap_0__Value]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_toSortedMap_0__A, _toSortedMap_0__B, typing.Any, java.util.SortedMap[_toSortedMap_0__Key, java.util.Set[_toSortedMap_0__Value]]]: ...
    @typing.overload
    @staticmethod
    def toSortedMap(biFunction: typing.Union[java.util.function.BiFunction[_toSortedMap_1__A, _toSortedMap_1__B, _toSortedMap_1__Key], typing.Callable[[_toSortedMap_1__A, _toSortedMap_1__B], _toSortedMap_1__Key]], biFunction2: typing.Union[java.util.function.BiFunction[_toSortedMap_1__A, _toSortedMap_1__B, _toSortedMap_1__Value], typing.Callable[[_toSortedMap_1__A, _toSortedMap_1__B], _toSortedMap_1__Value]], binaryOperator: typing.Union[java.util.function.BinaryOperator[_toSortedMap_1__Value], typing.Callable]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_toSortedMap_1__A, _toSortedMap_1__B, typing.Any, java.util.SortedMap[_toSortedMap_1__Key, _toSortedMap_1__Value]]: ...
    @typing.overload
    @staticmethod
    def toSortedMap(biFunction: typing.Union[java.util.function.BiFunction[_toSortedMap_2__A, _toSortedMap_2__B, _toSortedMap_2__Key], typing.Callable[[_toSortedMap_2__A, _toSortedMap_2__B], _toSortedMap_2__Key]], biFunction2: typing.Union[java.util.function.BiFunction[_toSortedMap_2__A, _toSortedMap_2__B, _toSortedMap_2__Value], typing.Callable[[_toSortedMap_2__A, _toSortedMap_2__B], _toSortedMap_2__Value]], intFunction: typing.Union[java.util.function.IntFunction[_toSortedMap_2__ValueSet], typing.Callable[[int], _toSortedMap_2__ValueSet]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_toSortedMap_2__A, _toSortedMap_2__B, typing.Any, java.util.SortedMap[_toSortedMap_2__Key, _toSortedMap_2__ValueSet]]: ...
    @typing.overload
    @staticmethod
    def toSortedMap(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toSortedMap_3__A, _toSortedMap_3__B, _toSortedMap_3__C, _toSortedMap_3__D, _toSortedMap_3__Key], typing.Callable[[_toSortedMap_3__A, _toSortedMap_3__B, _toSortedMap_3__C, _toSortedMap_3__D], _toSortedMap_3__Key]], quadFunction2: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toSortedMap_3__A, _toSortedMap_3__B, _toSortedMap_3__C, _toSortedMap_3__D, _toSortedMap_3__Value], typing.Callable[[_toSortedMap_3__A, _toSortedMap_3__B, _toSortedMap_3__C, _toSortedMap_3__D], _toSortedMap_3__Value]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_toSortedMap_3__A, _toSortedMap_3__B, _toSortedMap_3__C, _toSortedMap_3__D, typing.Any, java.util.SortedMap[_toSortedMap_3__Key, java.util.Set[_toSortedMap_3__Value]]]: ...
    @typing.overload
    @staticmethod
    def toSortedMap(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toSortedMap_4__A, _toSortedMap_4__B, _toSortedMap_4__C, _toSortedMap_4__D, _toSortedMap_4__Key], typing.Callable[[_toSortedMap_4__A, _toSortedMap_4__B, _toSortedMap_4__C, _toSortedMap_4__D], _toSortedMap_4__Key]], quadFunction2: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toSortedMap_4__A, _toSortedMap_4__B, _toSortedMap_4__C, _toSortedMap_4__D, _toSortedMap_4__Value], typing.Callable[[_toSortedMap_4__A, _toSortedMap_4__B, _toSortedMap_4__C, _toSortedMap_4__D], _toSortedMap_4__Value]], binaryOperator: typing.Union[java.util.function.BinaryOperator[_toSortedMap_4__Value], typing.Callable]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_toSortedMap_4__A, _toSortedMap_4__B, _toSortedMap_4__C, _toSortedMap_4__D, typing.Any, java.util.SortedMap[_toSortedMap_4__Key, _toSortedMap_4__Value]]: ...
    @typing.overload
    @staticmethod
    def toSortedMap(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toSortedMap_5__A, _toSortedMap_5__B, _toSortedMap_5__C, _toSortedMap_5__D, _toSortedMap_5__Key], typing.Callable[[_toSortedMap_5__A, _toSortedMap_5__B, _toSortedMap_5__C, _toSortedMap_5__D], _toSortedMap_5__Key]], quadFunction2: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toSortedMap_5__A, _toSortedMap_5__B, _toSortedMap_5__C, _toSortedMap_5__D, _toSortedMap_5__Value], typing.Callable[[_toSortedMap_5__A, _toSortedMap_5__B, _toSortedMap_5__C, _toSortedMap_5__D], _toSortedMap_5__Value]], intFunction: typing.Union[java.util.function.IntFunction[_toSortedMap_5__ValueSet], typing.Callable[[int], _toSortedMap_5__ValueSet]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_toSortedMap_5__A, _toSortedMap_5__B, _toSortedMap_5__C, _toSortedMap_5__D, typing.Any, java.util.SortedMap[_toSortedMap_5__Key, _toSortedMap_5__ValueSet]]: ...
    @typing.overload
    @staticmethod
    def toSortedMap(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_toSortedMap_6__A, _toSortedMap_6__B, _toSortedMap_6__C, _toSortedMap_6__Key], typing.Callable[[_toSortedMap_6__A, _toSortedMap_6__B, _toSortedMap_6__C], _toSortedMap_6__Key]], triFunction2: typing.Union[org.optaplanner.core.api.function.TriFunction[_toSortedMap_6__A, _toSortedMap_6__B, _toSortedMap_6__C, _toSortedMap_6__Value], typing.Callable[[_toSortedMap_6__A, _toSortedMap_6__B, _toSortedMap_6__C], _toSortedMap_6__Value]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_toSortedMap_6__A, _toSortedMap_6__B, _toSortedMap_6__C, typing.Any, java.util.SortedMap[_toSortedMap_6__Key, java.util.Set[_toSortedMap_6__Value]]]: ...
    @typing.overload
    @staticmethod
    def toSortedMap(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_toSortedMap_7__A, _toSortedMap_7__B, _toSortedMap_7__C, _toSortedMap_7__Key], typing.Callable[[_toSortedMap_7__A, _toSortedMap_7__B, _toSortedMap_7__C], _toSortedMap_7__Key]], triFunction2: typing.Union[org.optaplanner.core.api.function.TriFunction[_toSortedMap_7__A, _toSortedMap_7__B, _toSortedMap_7__C, _toSortedMap_7__Value], typing.Callable[[_toSortedMap_7__A, _toSortedMap_7__B, _toSortedMap_7__C], _toSortedMap_7__Value]], binaryOperator: typing.Union[java.util.function.BinaryOperator[_toSortedMap_7__Value], typing.Callable]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_toSortedMap_7__A, _toSortedMap_7__B, _toSortedMap_7__C, typing.Any, java.util.SortedMap[_toSortedMap_7__Key, _toSortedMap_7__Value]]: ...
    @typing.overload
    @staticmethod
    def toSortedMap(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_toSortedMap_8__A, _toSortedMap_8__B, _toSortedMap_8__C, _toSortedMap_8__Key], typing.Callable[[_toSortedMap_8__A, _toSortedMap_8__B, _toSortedMap_8__C], _toSortedMap_8__Key]], triFunction2: typing.Union[org.optaplanner.core.api.function.TriFunction[_toSortedMap_8__A, _toSortedMap_8__B, _toSortedMap_8__C, _toSortedMap_8__Value], typing.Callable[[_toSortedMap_8__A, _toSortedMap_8__B, _toSortedMap_8__C], _toSortedMap_8__Value]], intFunction: typing.Union[java.util.function.IntFunction[_toSortedMap_8__ValueSet], typing.Callable[[int], _toSortedMap_8__ValueSet]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_toSortedMap_8__A, _toSortedMap_8__B, _toSortedMap_8__C, typing.Any, java.util.SortedMap[_toSortedMap_8__Key, _toSortedMap_8__ValueSet]]: ...
    @typing.overload
    @staticmethod
    def toSortedMap(function: typing.Union[java.util.function.Function[_toSortedMap_9__A, _toSortedMap_9__Key], typing.Callable[[_toSortedMap_9__A], _toSortedMap_9__Key]], function2: typing.Union[java.util.function.Function[_toSortedMap_9__A, _toSortedMap_9__Value], typing.Callable[[_toSortedMap_9__A], _toSortedMap_9__Value]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_toSortedMap_9__A, typing.Any, java.util.SortedMap[_toSortedMap_9__Key, java.util.Set[_toSortedMap_9__Value]]]: ...
    @typing.overload
    @staticmethod
    def toSortedMap(function: typing.Union[java.util.function.Function[_toSortedMap_10__A, _toSortedMap_10__Key], typing.Callable[[_toSortedMap_10__A], _toSortedMap_10__Key]], function2: typing.Union[java.util.function.Function[_toSortedMap_10__A, _toSortedMap_10__Value], typing.Callable[[_toSortedMap_10__A], _toSortedMap_10__Value]], binaryOperator: typing.Union[java.util.function.BinaryOperator[_toSortedMap_10__Value], typing.Callable]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_toSortedMap_10__A, typing.Any, java.util.SortedMap[_toSortedMap_10__Key, _toSortedMap_10__Value]]: ...
    @typing.overload
    @staticmethod
    def toSortedMap(function: typing.Union[java.util.function.Function[_toSortedMap_11__A, _toSortedMap_11__Key], typing.Callable[[_toSortedMap_11__A], _toSortedMap_11__Key]], function2: typing.Union[java.util.function.Function[_toSortedMap_11__A, _toSortedMap_11__Value], typing.Callable[[_toSortedMap_11__A], _toSortedMap_11__Value]], intFunction: typing.Union[java.util.function.IntFunction[_toSortedMap_11__ValueSet], typing.Callable[[int], _toSortedMap_11__ValueSet]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_toSortedMap_11__A, typing.Any, java.util.SortedMap[_toSortedMap_11__Key, _toSortedMap_11__ValueSet]]: ...
    _toSortedSet_0__A = typing.TypeVar('_toSortedSet_0__A')  # <A>
    _toSortedSet_0__B = typing.TypeVar('_toSortedSet_0__B')  # <B>
    _toSortedSet_0__Mapped = typing.TypeVar('_toSortedSet_0__Mapped', bound=java.lang.Comparable)  # <Mapped>
    _toSortedSet_1__A = typing.TypeVar('_toSortedSet_1__A')  # <A>
    _toSortedSet_1__B = typing.TypeVar('_toSortedSet_1__B')  # <B>
    _toSortedSet_1__Mapped = typing.TypeVar('_toSortedSet_1__Mapped')  # <Mapped>
    _toSortedSet_2__A = typing.TypeVar('_toSortedSet_2__A')  # <A>
    _toSortedSet_2__B = typing.TypeVar('_toSortedSet_2__B')  # <B>
    _toSortedSet_2__C = typing.TypeVar('_toSortedSet_2__C')  # <C>
    _toSortedSet_2__D = typing.TypeVar('_toSortedSet_2__D')  # <D>
    _toSortedSet_2__Mapped = typing.TypeVar('_toSortedSet_2__Mapped', bound=java.lang.Comparable)  # <Mapped>
    _toSortedSet_3__A = typing.TypeVar('_toSortedSet_3__A')  # <A>
    _toSortedSet_3__B = typing.TypeVar('_toSortedSet_3__B')  # <B>
    _toSortedSet_3__C = typing.TypeVar('_toSortedSet_3__C')  # <C>
    _toSortedSet_3__D = typing.TypeVar('_toSortedSet_3__D')  # <D>
    _toSortedSet_3__Mapped = typing.TypeVar('_toSortedSet_3__Mapped')  # <Mapped>
    _toSortedSet_4__A = typing.TypeVar('_toSortedSet_4__A')  # <A>
    _toSortedSet_4__B = typing.TypeVar('_toSortedSet_4__B')  # <B>
    _toSortedSet_4__C = typing.TypeVar('_toSortedSet_4__C')  # <C>
    _toSortedSet_4__Mapped = typing.TypeVar('_toSortedSet_4__Mapped', bound=java.lang.Comparable)  # <Mapped>
    _toSortedSet_5__A = typing.TypeVar('_toSortedSet_5__A')  # <A>
    _toSortedSet_5__B = typing.TypeVar('_toSortedSet_5__B')  # <B>
    _toSortedSet_5__C = typing.TypeVar('_toSortedSet_5__C')  # <C>
    _toSortedSet_5__Mapped = typing.TypeVar('_toSortedSet_5__Mapped')  # <Mapped>
    _toSortedSet_6__A = typing.TypeVar('_toSortedSet_6__A', bound=java.lang.Comparable)  # <A>
    _toSortedSet_7__A = typing.TypeVar('_toSortedSet_7__A')  # <A>
    _toSortedSet_8__A = typing.TypeVar('_toSortedSet_8__A')  # <A>
    _toSortedSet_8__Mapped = typing.TypeVar('_toSortedSet_8__Mapped', bound=java.lang.Comparable)  # <Mapped>
    _toSortedSet_9__A = typing.TypeVar('_toSortedSet_9__A')  # <A>
    _toSortedSet_9__Mapped = typing.TypeVar('_toSortedSet_9__Mapped')  # <Mapped>
    @typing.overload
    @staticmethod
    def toSortedSet(biFunction: typing.Union[java.util.function.BiFunction[_toSortedSet_0__A, _toSortedSet_0__B, _toSortedSet_0__Mapped], typing.Callable[[_toSortedSet_0__A, _toSortedSet_0__B], _toSortedSet_0__Mapped]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_toSortedSet_0__A, _toSortedSet_0__B, typing.Any, java.util.SortedSet[_toSortedSet_0__Mapped]]: ...
    @typing.overload
    @staticmethod
    def toSortedSet(biFunction: typing.Union[java.util.function.BiFunction[_toSortedSet_1__A, _toSortedSet_1__B, _toSortedSet_1__Mapped], typing.Callable[[_toSortedSet_1__A, _toSortedSet_1__B], _toSortedSet_1__Mapped]], comparator: typing.Union[java.util.Comparator[_toSortedSet_1__Mapped], typing.Callable[[_toSortedSet_1__Mapped, _toSortedSet_1__Mapped], int]]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintCollector[_toSortedSet_1__A, _toSortedSet_1__B, typing.Any, java.util.SortedSet[_toSortedSet_1__Mapped]]: ...
    @typing.overload
    @staticmethod
    def toSortedSet(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toSortedSet_2__A, _toSortedSet_2__B, _toSortedSet_2__C, _toSortedSet_2__D, _toSortedSet_2__Mapped], typing.Callable[[_toSortedSet_2__A, _toSortedSet_2__B, _toSortedSet_2__C, _toSortedSet_2__D], _toSortedSet_2__Mapped]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_toSortedSet_2__A, _toSortedSet_2__B, _toSortedSet_2__C, _toSortedSet_2__D, typing.Any, java.util.SortedSet[_toSortedSet_2__Mapped]]: ...
    @typing.overload
    @staticmethod
    def toSortedSet(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_toSortedSet_3__A, _toSortedSet_3__B, _toSortedSet_3__C, _toSortedSet_3__D, _toSortedSet_3__Mapped], typing.Callable[[_toSortedSet_3__A, _toSortedSet_3__B, _toSortedSet_3__C, _toSortedSet_3__D], _toSortedSet_3__Mapped]], comparator: typing.Union[java.util.Comparator[_toSortedSet_3__Mapped], typing.Callable[[_toSortedSet_3__Mapped, _toSortedSet_3__Mapped], int]]) -> org.optaplanner.core.api.score.stream.quad.QuadConstraintCollector[_toSortedSet_3__A, _toSortedSet_3__B, _toSortedSet_3__C, _toSortedSet_3__D, typing.Any, java.util.SortedSet[_toSortedSet_3__Mapped]]: ...
    @typing.overload
    @staticmethod
    def toSortedSet(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_toSortedSet_4__A, _toSortedSet_4__B, _toSortedSet_4__C, _toSortedSet_4__Mapped], typing.Callable[[_toSortedSet_4__A, _toSortedSet_4__B, _toSortedSet_4__C], _toSortedSet_4__Mapped]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_toSortedSet_4__A, _toSortedSet_4__B, _toSortedSet_4__C, typing.Any, java.util.SortedSet[_toSortedSet_4__Mapped]]: ...
    @typing.overload
    @staticmethod
    def toSortedSet(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_toSortedSet_5__A, _toSortedSet_5__B, _toSortedSet_5__C, _toSortedSet_5__Mapped], typing.Callable[[_toSortedSet_5__A, _toSortedSet_5__B, _toSortedSet_5__C], _toSortedSet_5__Mapped]], comparator: typing.Union[java.util.Comparator[_toSortedSet_5__Mapped], typing.Callable[[_toSortedSet_5__Mapped, _toSortedSet_5__Mapped], int]]) -> org.optaplanner.core.api.score.stream.tri.TriConstraintCollector[_toSortedSet_5__A, _toSortedSet_5__B, _toSortedSet_5__C, typing.Any, java.util.SortedSet[_toSortedSet_5__Mapped]]: ...
    @typing.overload
    @staticmethod
    def toSortedSet() -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_toSortedSet_6__A, typing.Any, java.util.SortedSet[_toSortedSet_6__A]]: ...
    @typing.overload
    @staticmethod
    def toSortedSet(comparator: typing.Union[java.util.Comparator[_toSortedSet_7__A], typing.Callable[[_toSortedSet_7__A, _toSortedSet_7__A], int]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_toSortedSet_7__A, typing.Any, java.util.SortedSet[_toSortedSet_7__A]]: ...
    @typing.overload
    @staticmethod
    def toSortedSet(function: typing.Union[java.util.function.Function[_toSortedSet_8__A, _toSortedSet_8__Mapped], typing.Callable[[_toSortedSet_8__A], _toSortedSet_8__Mapped]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_toSortedSet_8__A, typing.Any, java.util.SortedSet[_toSortedSet_8__Mapped]]: ...
    @typing.overload
    @staticmethod
    def toSortedSet(function: typing.Union[java.util.function.Function[_toSortedSet_9__A, _toSortedSet_9__Mapped], typing.Callable[[_toSortedSet_9__A], _toSortedSet_9__Mapped]], comparator: typing.Union[java.util.Comparator[_toSortedSet_9__Mapped], typing.Callable[[_toSortedSet_9__Mapped, _toSortedSet_9__Mapped], int]]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintCollector[_toSortedSet_9__A, typing.Any, java.util.SortedSet[_toSortedSet_9__Mapped]]: ...

class ConstraintFactory:
    _forEach__A = typing.TypeVar('_forEach__A')  # <A>
    def forEach(self, class_: typing.Type[_forEach__A]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintStream[_forEach__A]: ...
    _forEachIncludingNullVars__A = typing.TypeVar('_forEachIncludingNullVars__A')  # <A>
    def forEachIncludingNullVars(self, class_: typing.Type[_forEachIncludingNullVars__A]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintStream[_forEachIncludingNullVars__A]: ...
    _forEachUniquePair_0__A = typing.TypeVar('_forEachUniquePair_0__A')  # <A>
    _forEachUniquePair_1__A = typing.TypeVar('_forEachUniquePair_1__A')  # <A>
    _forEachUniquePair_2__A = typing.TypeVar('_forEachUniquePair_2__A')  # <A>
    _forEachUniquePair_3__A = typing.TypeVar('_forEachUniquePair_3__A')  # <A>
    _forEachUniquePair_4__A = typing.TypeVar('_forEachUniquePair_4__A')  # <A>
    _forEachUniquePair_5__A = typing.TypeVar('_forEachUniquePair_5__A')  # <A>
    @typing.overload
    def forEachUniquePair(self, class_: typing.Type[_forEachUniquePair_0__A], *biJoiner: org.optaplanner.core.api.score.stream.bi.BiJoiner[_forEachUniquePair_0__A, _forEachUniquePair_0__A]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintStream[_forEachUniquePair_0__A, _forEachUniquePair_0__A]: ...
    @typing.overload
    def forEachUniquePair(self, class_: typing.Type[_forEachUniquePair_1__A]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintStream[_forEachUniquePair_1__A, _forEachUniquePair_1__A]: ...
    @typing.overload
    def forEachUniquePair(self, class_: typing.Type[_forEachUniquePair_2__A], biJoiner: org.optaplanner.core.api.score.stream.bi.BiJoiner[_forEachUniquePair_2__A, _forEachUniquePair_2__A]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintStream[_forEachUniquePair_2__A, _forEachUniquePair_2__A]: ...
    @typing.overload
    def forEachUniquePair(self, class_: typing.Type[_forEachUniquePair_3__A], biJoiner: org.optaplanner.core.api.score.stream.bi.BiJoiner[_forEachUniquePair_3__A, _forEachUniquePair_3__A], biJoiner2: org.optaplanner.core.api.score.stream.bi.BiJoiner[_forEachUniquePair_3__A, _forEachUniquePair_3__A]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintStream[_forEachUniquePair_3__A, _forEachUniquePair_3__A]: ...
    @typing.overload
    def forEachUniquePair(self, class_: typing.Type[_forEachUniquePair_4__A], biJoiner: org.optaplanner.core.api.score.stream.bi.BiJoiner[_forEachUniquePair_4__A, _forEachUniquePair_4__A], biJoiner2: org.optaplanner.core.api.score.stream.bi.BiJoiner[_forEachUniquePair_4__A, _forEachUniquePair_4__A], biJoiner3: org.optaplanner.core.api.score.stream.bi.BiJoiner[_forEachUniquePair_4__A, _forEachUniquePair_4__A]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintStream[_forEachUniquePair_4__A, _forEachUniquePair_4__A]: ...
    @typing.overload
    def forEachUniquePair(self, class_: typing.Type[_forEachUniquePair_5__A], biJoiner: org.optaplanner.core.api.score.stream.bi.BiJoiner[_forEachUniquePair_5__A, _forEachUniquePair_5__A], biJoiner2: org.optaplanner.core.api.score.stream.bi.BiJoiner[_forEachUniquePair_5__A, _forEachUniquePair_5__A], biJoiner3: org.optaplanner.core.api.score.stream.bi.BiJoiner[_forEachUniquePair_5__A, _forEachUniquePair_5__A], biJoiner4: org.optaplanner.core.api.score.stream.bi.BiJoiner[_forEachUniquePair_5__A, _forEachUniquePair_5__A]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintStream[_forEachUniquePair_5__A, _forEachUniquePair_5__A]: ...
    _fromUnfiltered__A = typing.TypeVar('_fromUnfiltered__A')  # <A>
    def fromUnfiltered(self, class_: typing.Type[_fromUnfiltered__A]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintStream[_fromUnfiltered__A]: ...
    _fromUniquePair_0__A = typing.TypeVar('_fromUniquePair_0__A')  # <A>
    _fromUniquePair_1__A = typing.TypeVar('_fromUniquePair_1__A')  # <A>
    _fromUniquePair_2__A = typing.TypeVar('_fromUniquePair_2__A')  # <A>
    _fromUniquePair_3__A = typing.TypeVar('_fromUniquePair_3__A')  # <A>
    _fromUniquePair_4__A = typing.TypeVar('_fromUniquePair_4__A')  # <A>
    _fromUniquePair_5__A = typing.TypeVar('_fromUniquePair_5__A')  # <A>
    @typing.overload
    def fromUniquePair(self, class_: typing.Type[_fromUniquePair_0__A], *biJoiner: org.optaplanner.core.api.score.stream.bi.BiJoiner[_fromUniquePair_0__A, _fromUniquePair_0__A]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintStream[_fromUniquePair_0__A, _fromUniquePair_0__A]: ...
    @typing.overload
    def fromUniquePair(self, class_: typing.Type[_fromUniquePair_1__A]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintStream[_fromUniquePair_1__A, _fromUniquePair_1__A]: ...
    @typing.overload
    def fromUniquePair(self, class_: typing.Type[_fromUniquePair_2__A], biJoiner: org.optaplanner.core.api.score.stream.bi.BiJoiner[_fromUniquePair_2__A, _fromUniquePair_2__A]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintStream[_fromUniquePair_2__A, _fromUniquePair_2__A]: ...
    @typing.overload
    def fromUniquePair(self, class_: typing.Type[_fromUniquePair_3__A], biJoiner: org.optaplanner.core.api.score.stream.bi.BiJoiner[_fromUniquePair_3__A, _fromUniquePair_3__A], biJoiner2: org.optaplanner.core.api.score.stream.bi.BiJoiner[_fromUniquePair_3__A, _fromUniquePair_3__A]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintStream[_fromUniquePair_3__A, _fromUniquePair_3__A]: ...
    @typing.overload
    def fromUniquePair(self, class_: typing.Type[_fromUniquePair_4__A], biJoiner: org.optaplanner.core.api.score.stream.bi.BiJoiner[_fromUniquePair_4__A, _fromUniquePair_4__A], biJoiner2: org.optaplanner.core.api.score.stream.bi.BiJoiner[_fromUniquePair_4__A, _fromUniquePair_4__A], biJoiner3: org.optaplanner.core.api.score.stream.bi.BiJoiner[_fromUniquePair_4__A, _fromUniquePair_4__A]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintStream[_fromUniquePair_4__A, _fromUniquePair_4__A]: ...
    @typing.overload
    def fromUniquePair(self, class_: typing.Type[_fromUniquePair_5__A], biJoiner: org.optaplanner.core.api.score.stream.bi.BiJoiner[_fromUniquePair_5__A, _fromUniquePair_5__A], biJoiner2: org.optaplanner.core.api.score.stream.bi.BiJoiner[_fromUniquePair_5__A, _fromUniquePair_5__A], biJoiner3: org.optaplanner.core.api.score.stream.bi.BiJoiner[_fromUniquePair_5__A, _fromUniquePair_5__A], biJoiner4: org.optaplanner.core.api.score.stream.bi.BiJoiner[_fromUniquePair_5__A, _fromUniquePair_5__A]) -> org.optaplanner.core.api.score.stream.bi.BiConstraintStream[_fromUniquePair_5__A, _fromUniquePair_5__A]: ...
    _from___A = typing.TypeVar('_from___A')  # <A>
    def from_(self, class_: typing.Type[_from___A]) -> org.optaplanner.core.api.score.stream.uni.UniConstraintStream[_from___A]: ...
    def getDefaultConstraintPackage(self) -> str: ...

class ConstraintJustification: ...

class ConstraintProvider:
    def defineConstraints(self, constraintFactory: ConstraintFactory) -> typing.MutableSequence[Constraint]: ...

class ConstraintStream:
    def getConstraintFactory(self) -> ConstraintFactory: ...
    @typing.overload
    def impact(self, string: str, string2: str, score: org.optaplanner.core.api.score.Score[typing.Any]) -> Constraint: ...
    @typing.overload
    def impact(self, string: str, score: org.optaplanner.core.api.score.Score[typing.Any]) -> Constraint: ...
    @typing.overload
    def penalize(self, string: str, string2: str, score: org.optaplanner.core.api.score.Score[typing.Any]) -> Constraint: ...
    @typing.overload
    def penalize(self, string: str, score: org.optaplanner.core.api.score.Score[typing.Any]) -> Constraint: ...
    @typing.overload
    def penalizeConfigurable(self, string: str) -> Constraint: ...
    @typing.overload
    def penalizeConfigurable(self, string: str, string2: str) -> Constraint: ...
    @typing.overload
    def reward(self, string: str, string2: str, score: org.optaplanner.core.api.score.Score[typing.Any]) -> Constraint: ...
    @typing.overload
    def reward(self, string: str, score: org.optaplanner.core.api.score.Score[typing.Any]) -> Constraint: ...
    @typing.overload
    def rewardConfigurable(self, string: str) -> Constraint: ...
    @typing.overload
    def rewardConfigurable(self, string: str, string2: str) -> Constraint: ...

class ConstraintStreamImplType(java.lang.Enum['ConstraintStreamImplType']):
    BAVET: typing.ClassVar['ConstraintStreamImplType'] = ...
    DROOLS: typing.ClassVar['ConstraintStreamImplType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'ConstraintStreamImplType': ...
    @staticmethod
    def values() -> typing.MutableSequence['ConstraintStreamImplType']: ...

class Joiners:
    _equal_0__A = typing.TypeVar('_equal_0__A')  # <A>
    _equal_1__A = typing.TypeVar('_equal_1__A')  # <A>
    _equal_1__Property_ = typing.TypeVar('_equal_1__Property_')  # <Property_>
    _equal_2__A = typing.TypeVar('_equal_2__A')  # <A>
    _equal_2__B = typing.TypeVar('_equal_2__B')  # <B>
    _equal_2__Property_ = typing.TypeVar('_equal_2__Property_')  # <Property_>
    _equal_3__A = typing.TypeVar('_equal_3__A')  # <A>
    _equal_3__B = typing.TypeVar('_equal_3__B')  # <B>
    _equal_3__C = typing.TypeVar('_equal_3__C')  # <C>
    _equal_3__D = typing.TypeVar('_equal_3__D')  # <D>
    _equal_3__E = typing.TypeVar('_equal_3__E')  # <E>
    _equal_3__Property_ = typing.TypeVar('_equal_3__Property_')  # <Property_>
    _equal_4__A = typing.TypeVar('_equal_4__A')  # <A>
    _equal_4__B = typing.TypeVar('_equal_4__B')  # <B>
    _equal_4__C = typing.TypeVar('_equal_4__C')  # <C>
    _equal_4__D = typing.TypeVar('_equal_4__D')  # <D>
    _equal_4__Property_ = typing.TypeVar('_equal_4__Property_')  # <Property_>
    _equal_5__A = typing.TypeVar('_equal_5__A')  # <A>
    _equal_5__B = typing.TypeVar('_equal_5__B')  # <B>
    _equal_5__C = typing.TypeVar('_equal_5__C')  # <C>
    _equal_5__Property_ = typing.TypeVar('_equal_5__Property_')  # <Property_>
    @typing.overload
    @staticmethod
    def equal() -> org.optaplanner.core.api.score.stream.bi.BiJoiner[_equal_0__A, _equal_0__A]: ...
    @typing.overload
    @staticmethod
    def equal(function: typing.Union[java.util.function.Function[_equal_1__A, _equal_1__Property_], typing.Callable[[_equal_1__A], _equal_1__Property_]]) -> org.optaplanner.core.api.score.stream.bi.BiJoiner[_equal_1__A, _equal_1__A]: ...
    @typing.overload
    @staticmethod
    def equal(function: typing.Union[java.util.function.Function[_equal_2__A, _equal_2__Property_], typing.Callable[[_equal_2__A], _equal_2__Property_]], function2: typing.Union[java.util.function.Function[_equal_2__B, _equal_2__Property_], typing.Callable[[_equal_2__B], _equal_2__Property_]]) -> org.optaplanner.core.api.score.stream.bi.BiJoiner[_equal_2__A, _equal_2__B]: ...
    @typing.overload
    @staticmethod
    def equal(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_equal_3__A, _equal_3__B, _equal_3__C, _equal_3__D, _equal_3__Property_], typing.Callable[[_equal_3__A, _equal_3__B, _equal_3__C, _equal_3__D], _equal_3__Property_]], function: typing.Union[java.util.function.Function[_equal_3__E, _equal_3__Property_], typing.Callable[[_equal_3__E], _equal_3__Property_]]) -> org.optaplanner.core.api.score.stream.penta.PentaJoiner[_equal_3__A, _equal_3__B, _equal_3__C, _equal_3__D, _equal_3__E]: ...
    @typing.overload
    @staticmethod
    def equal(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_equal_4__A, _equal_4__B, _equal_4__C, _equal_4__Property_], typing.Callable[[_equal_4__A, _equal_4__B, _equal_4__C], _equal_4__Property_]], function: typing.Union[java.util.function.Function[_equal_4__D, _equal_4__Property_], typing.Callable[[_equal_4__D], _equal_4__Property_]]) -> org.optaplanner.core.api.score.stream.quad.QuadJoiner[_equal_4__A, _equal_4__B, _equal_4__C, _equal_4__D]: ...
    @typing.overload
    @staticmethod
    def equal(biFunction: typing.Union[java.util.function.BiFunction[_equal_5__A, _equal_5__B, _equal_5__Property_], typing.Callable[[_equal_5__A, _equal_5__B], _equal_5__Property_]], function: typing.Union[java.util.function.Function[_equal_5__C, _equal_5__Property_], typing.Callable[[_equal_5__C], _equal_5__Property_]]) -> org.optaplanner.core.api.score.stream.tri.TriJoiner[_equal_5__A, _equal_5__B, _equal_5__C]: ...
    _filtering_0__A = typing.TypeVar('_filtering_0__A')  # <A>
    _filtering_0__B = typing.TypeVar('_filtering_0__B')  # <B>
    _filtering_1__A = typing.TypeVar('_filtering_1__A')  # <A>
    _filtering_1__B = typing.TypeVar('_filtering_1__B')  # <B>
    _filtering_1__C = typing.TypeVar('_filtering_1__C')  # <C>
    _filtering_1__D = typing.TypeVar('_filtering_1__D')  # <D>
    _filtering_1__E = typing.TypeVar('_filtering_1__E')  # <E>
    _filtering_2__A = typing.TypeVar('_filtering_2__A')  # <A>
    _filtering_2__B = typing.TypeVar('_filtering_2__B')  # <B>
    _filtering_2__C = typing.TypeVar('_filtering_2__C')  # <C>
    _filtering_2__D = typing.TypeVar('_filtering_2__D')  # <D>
    _filtering_3__A = typing.TypeVar('_filtering_3__A')  # <A>
    _filtering_3__B = typing.TypeVar('_filtering_3__B')  # <B>
    _filtering_3__C = typing.TypeVar('_filtering_3__C')  # <C>
    @typing.overload
    @staticmethod
    def filtering(biPredicate: typing.Union[java.util.function.BiPredicate[_filtering_0__A, _filtering_0__B], typing.Callable[[_filtering_0__A, _filtering_0__B], bool]]) -> org.optaplanner.core.api.score.stream.bi.BiJoiner[_filtering_0__A, _filtering_0__B]: ...
    @typing.overload
    @staticmethod
    def filtering(pentaPredicate: typing.Union[org.optaplanner.core.api.function.PentaPredicate[_filtering_1__A, _filtering_1__B, _filtering_1__C, _filtering_1__D, _filtering_1__E], typing.Callable[[_filtering_1__A, _filtering_1__B, _filtering_1__C, _filtering_1__D, _filtering_1__E], bool]]) -> org.optaplanner.core.api.score.stream.penta.PentaJoiner[_filtering_1__A, _filtering_1__B, _filtering_1__C, _filtering_1__D, _filtering_1__E]: ...
    @typing.overload
    @staticmethod
    def filtering(quadPredicate: typing.Union[org.optaplanner.core.api.function.QuadPredicate[_filtering_2__A, _filtering_2__B, _filtering_2__C, _filtering_2__D], typing.Callable[[_filtering_2__A, _filtering_2__B, _filtering_2__C, _filtering_2__D], bool]]) -> org.optaplanner.core.api.score.stream.quad.QuadJoiner[_filtering_2__A, _filtering_2__B, _filtering_2__C, _filtering_2__D]: ...
    @typing.overload
    @staticmethod
    def filtering(triPredicate: typing.Union[org.optaplanner.core.api.function.TriPredicate[_filtering_3__A, _filtering_3__B, _filtering_3__C], typing.Callable[[_filtering_3__A, _filtering_3__B, _filtering_3__C], bool]]) -> org.optaplanner.core.api.score.stream.tri.TriJoiner[_filtering_3__A, _filtering_3__B, _filtering_3__C]: ...
    _greaterThan_0__A = typing.TypeVar('_greaterThan_0__A')  # <A>
    _greaterThan_0__Property_ = typing.TypeVar('_greaterThan_0__Property_', bound=java.lang.Comparable)  # <Property_>
    _greaterThan_1__A = typing.TypeVar('_greaterThan_1__A')  # <A>
    _greaterThan_1__B = typing.TypeVar('_greaterThan_1__B')  # <B>
    _greaterThan_1__Property_ = typing.TypeVar('_greaterThan_1__Property_', bound=java.lang.Comparable)  # <Property_>
    _greaterThan_2__A = typing.TypeVar('_greaterThan_2__A')  # <A>
    _greaterThan_2__B = typing.TypeVar('_greaterThan_2__B')  # <B>
    _greaterThan_2__C = typing.TypeVar('_greaterThan_2__C')  # <C>
    _greaterThan_2__D = typing.TypeVar('_greaterThan_2__D')  # <D>
    _greaterThan_2__E = typing.TypeVar('_greaterThan_2__E')  # <E>
    _greaterThan_2__Property_ = typing.TypeVar('_greaterThan_2__Property_', bound=java.lang.Comparable)  # <Property_>
    _greaterThan_3__A = typing.TypeVar('_greaterThan_3__A')  # <A>
    _greaterThan_3__B = typing.TypeVar('_greaterThan_3__B')  # <B>
    _greaterThan_3__C = typing.TypeVar('_greaterThan_3__C')  # <C>
    _greaterThan_3__D = typing.TypeVar('_greaterThan_3__D')  # <D>
    _greaterThan_3__Property_ = typing.TypeVar('_greaterThan_3__Property_', bound=java.lang.Comparable)  # <Property_>
    _greaterThan_4__A = typing.TypeVar('_greaterThan_4__A')  # <A>
    _greaterThan_4__B = typing.TypeVar('_greaterThan_4__B')  # <B>
    _greaterThan_4__C = typing.TypeVar('_greaterThan_4__C')  # <C>
    _greaterThan_4__Property_ = typing.TypeVar('_greaterThan_4__Property_', bound=java.lang.Comparable)  # <Property_>
    @typing.overload
    @staticmethod
    def greaterThan(function: typing.Union[java.util.function.Function[_greaterThan_0__A, _greaterThan_0__Property_], typing.Callable[[_greaterThan_0__A], _greaterThan_0__Property_]]) -> org.optaplanner.core.api.score.stream.bi.BiJoiner[_greaterThan_0__A, _greaterThan_0__A]: ...
    @typing.overload
    @staticmethod
    def greaterThan(function: typing.Union[java.util.function.Function[_greaterThan_1__A, _greaterThan_1__Property_], typing.Callable[[_greaterThan_1__A], _greaterThan_1__Property_]], function2: typing.Union[java.util.function.Function[_greaterThan_1__B, _greaterThan_1__Property_], typing.Callable[[_greaterThan_1__B], _greaterThan_1__Property_]]) -> org.optaplanner.core.api.score.stream.bi.BiJoiner[_greaterThan_1__A, _greaterThan_1__B]: ...
    @typing.overload
    @staticmethod
    def greaterThan(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_greaterThan_2__A, _greaterThan_2__B, _greaterThan_2__C, _greaterThan_2__D, _greaterThan_2__Property_], typing.Callable[[_greaterThan_2__A, _greaterThan_2__B, _greaterThan_2__C, _greaterThan_2__D], _greaterThan_2__Property_]], function: typing.Union[java.util.function.Function[_greaterThan_2__E, _greaterThan_2__Property_], typing.Callable[[_greaterThan_2__E], _greaterThan_2__Property_]]) -> org.optaplanner.core.api.score.stream.penta.PentaJoiner[_greaterThan_2__A, _greaterThan_2__B, _greaterThan_2__C, _greaterThan_2__D, _greaterThan_2__E]: ...
    @typing.overload
    @staticmethod
    def greaterThan(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_greaterThan_3__A, _greaterThan_3__B, _greaterThan_3__C, _greaterThan_3__Property_], typing.Callable[[_greaterThan_3__A, _greaterThan_3__B, _greaterThan_3__C], _greaterThan_3__Property_]], function: typing.Union[java.util.function.Function[_greaterThan_3__D, _greaterThan_3__Property_], typing.Callable[[_greaterThan_3__D], _greaterThan_3__Property_]]) -> org.optaplanner.core.api.score.stream.quad.QuadJoiner[_greaterThan_3__A, _greaterThan_3__B, _greaterThan_3__C, _greaterThan_3__D]: ...
    @typing.overload
    @staticmethod
    def greaterThan(biFunction: typing.Union[java.util.function.BiFunction[_greaterThan_4__A, _greaterThan_4__B, _greaterThan_4__Property_], typing.Callable[[_greaterThan_4__A, _greaterThan_4__B], _greaterThan_4__Property_]], function: typing.Union[java.util.function.Function[_greaterThan_4__C, _greaterThan_4__Property_], typing.Callable[[_greaterThan_4__C], _greaterThan_4__Property_]]) -> org.optaplanner.core.api.score.stream.tri.TriJoiner[_greaterThan_4__A, _greaterThan_4__B, _greaterThan_4__C]: ...
    _greaterThanOrEqual_0__A = typing.TypeVar('_greaterThanOrEqual_0__A')  # <A>
    _greaterThanOrEqual_0__Property_ = typing.TypeVar('_greaterThanOrEqual_0__Property_', bound=java.lang.Comparable)  # <Property_>
    _greaterThanOrEqual_1__A = typing.TypeVar('_greaterThanOrEqual_1__A')  # <A>
    _greaterThanOrEqual_1__B = typing.TypeVar('_greaterThanOrEqual_1__B')  # <B>
    _greaterThanOrEqual_1__Property_ = typing.TypeVar('_greaterThanOrEqual_1__Property_', bound=java.lang.Comparable)  # <Property_>
    _greaterThanOrEqual_2__A = typing.TypeVar('_greaterThanOrEqual_2__A')  # <A>
    _greaterThanOrEqual_2__B = typing.TypeVar('_greaterThanOrEqual_2__B')  # <B>
    _greaterThanOrEqual_2__C = typing.TypeVar('_greaterThanOrEqual_2__C')  # <C>
    _greaterThanOrEqual_2__D = typing.TypeVar('_greaterThanOrEqual_2__D')  # <D>
    _greaterThanOrEqual_2__E = typing.TypeVar('_greaterThanOrEqual_2__E')  # <E>
    _greaterThanOrEqual_2__Property_ = typing.TypeVar('_greaterThanOrEqual_2__Property_', bound=java.lang.Comparable)  # <Property_>
    _greaterThanOrEqual_3__A = typing.TypeVar('_greaterThanOrEqual_3__A')  # <A>
    _greaterThanOrEqual_3__B = typing.TypeVar('_greaterThanOrEqual_3__B')  # <B>
    _greaterThanOrEqual_3__C = typing.TypeVar('_greaterThanOrEqual_3__C')  # <C>
    _greaterThanOrEqual_3__D = typing.TypeVar('_greaterThanOrEqual_3__D')  # <D>
    _greaterThanOrEqual_3__Property_ = typing.TypeVar('_greaterThanOrEqual_3__Property_', bound=java.lang.Comparable)  # <Property_>
    _greaterThanOrEqual_4__A = typing.TypeVar('_greaterThanOrEqual_4__A')  # <A>
    _greaterThanOrEqual_4__B = typing.TypeVar('_greaterThanOrEqual_4__B')  # <B>
    _greaterThanOrEqual_4__C = typing.TypeVar('_greaterThanOrEqual_4__C')  # <C>
    _greaterThanOrEqual_4__Property_ = typing.TypeVar('_greaterThanOrEqual_4__Property_', bound=java.lang.Comparable)  # <Property_>
    @typing.overload
    @staticmethod
    def greaterThanOrEqual(function: typing.Union[java.util.function.Function[_greaterThanOrEqual_0__A, _greaterThanOrEqual_0__Property_], typing.Callable[[_greaterThanOrEqual_0__A], _greaterThanOrEqual_0__Property_]]) -> org.optaplanner.core.api.score.stream.bi.BiJoiner[_greaterThanOrEqual_0__A, _greaterThanOrEqual_0__A]: ...
    @typing.overload
    @staticmethod
    def greaterThanOrEqual(function: typing.Union[java.util.function.Function[_greaterThanOrEqual_1__A, _greaterThanOrEqual_1__Property_], typing.Callable[[_greaterThanOrEqual_1__A], _greaterThanOrEqual_1__Property_]], function2: typing.Union[java.util.function.Function[_greaterThanOrEqual_1__B, _greaterThanOrEqual_1__Property_], typing.Callable[[_greaterThanOrEqual_1__B], _greaterThanOrEqual_1__Property_]]) -> org.optaplanner.core.api.score.stream.bi.BiJoiner[_greaterThanOrEqual_1__A, _greaterThanOrEqual_1__B]: ...
    @typing.overload
    @staticmethod
    def greaterThanOrEqual(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_greaterThanOrEqual_2__A, _greaterThanOrEqual_2__B, _greaterThanOrEqual_2__C, _greaterThanOrEqual_2__D, _greaterThanOrEqual_2__Property_], typing.Callable[[_greaterThanOrEqual_2__A, _greaterThanOrEqual_2__B, _greaterThanOrEqual_2__C, _greaterThanOrEqual_2__D], _greaterThanOrEqual_2__Property_]], function: typing.Union[java.util.function.Function[_greaterThanOrEqual_2__E, _greaterThanOrEqual_2__Property_], typing.Callable[[_greaterThanOrEqual_2__E], _greaterThanOrEqual_2__Property_]]) -> org.optaplanner.core.api.score.stream.penta.PentaJoiner[_greaterThanOrEqual_2__A, _greaterThanOrEqual_2__B, _greaterThanOrEqual_2__C, _greaterThanOrEqual_2__D, _greaterThanOrEqual_2__E]: ...
    @typing.overload
    @staticmethod
    def greaterThanOrEqual(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_greaterThanOrEqual_3__A, _greaterThanOrEqual_3__B, _greaterThanOrEqual_3__C, _greaterThanOrEqual_3__Property_], typing.Callable[[_greaterThanOrEqual_3__A, _greaterThanOrEqual_3__B, _greaterThanOrEqual_3__C], _greaterThanOrEqual_3__Property_]], function: typing.Union[java.util.function.Function[_greaterThanOrEqual_3__D, _greaterThanOrEqual_3__Property_], typing.Callable[[_greaterThanOrEqual_3__D], _greaterThanOrEqual_3__Property_]]) -> org.optaplanner.core.api.score.stream.quad.QuadJoiner[_greaterThanOrEqual_3__A, _greaterThanOrEqual_3__B, _greaterThanOrEqual_3__C, _greaterThanOrEqual_3__D]: ...
    @typing.overload
    @staticmethod
    def greaterThanOrEqual(biFunction: typing.Union[java.util.function.BiFunction[_greaterThanOrEqual_4__A, _greaterThanOrEqual_4__B, _greaterThanOrEqual_4__Property_], typing.Callable[[_greaterThanOrEqual_4__A, _greaterThanOrEqual_4__B], _greaterThanOrEqual_4__Property_]], function: typing.Union[java.util.function.Function[_greaterThanOrEqual_4__C, _greaterThanOrEqual_4__Property_], typing.Callable[[_greaterThanOrEqual_4__C], _greaterThanOrEqual_4__Property_]]) -> org.optaplanner.core.api.score.stream.tri.TriJoiner[_greaterThanOrEqual_4__A, _greaterThanOrEqual_4__B, _greaterThanOrEqual_4__C]: ...
    _lessThan_0__A = typing.TypeVar('_lessThan_0__A')  # <A>
    _lessThan_0__Property_ = typing.TypeVar('_lessThan_0__Property_', bound=java.lang.Comparable)  # <Property_>
    _lessThan_1__A = typing.TypeVar('_lessThan_1__A')  # <A>
    _lessThan_1__B = typing.TypeVar('_lessThan_1__B')  # <B>
    _lessThan_1__Property_ = typing.TypeVar('_lessThan_1__Property_', bound=java.lang.Comparable)  # <Property_>
    _lessThan_2__A = typing.TypeVar('_lessThan_2__A')  # <A>
    _lessThan_2__B = typing.TypeVar('_lessThan_2__B')  # <B>
    _lessThan_2__C = typing.TypeVar('_lessThan_2__C')  # <C>
    _lessThan_2__D = typing.TypeVar('_lessThan_2__D')  # <D>
    _lessThan_2__E = typing.TypeVar('_lessThan_2__E')  # <E>
    _lessThan_2__Property_ = typing.TypeVar('_lessThan_2__Property_', bound=java.lang.Comparable)  # <Property_>
    _lessThan_3__A = typing.TypeVar('_lessThan_3__A')  # <A>
    _lessThan_3__B = typing.TypeVar('_lessThan_3__B')  # <B>
    _lessThan_3__C = typing.TypeVar('_lessThan_3__C')  # <C>
    _lessThan_3__D = typing.TypeVar('_lessThan_3__D')  # <D>
    _lessThan_3__Property_ = typing.TypeVar('_lessThan_3__Property_', bound=java.lang.Comparable)  # <Property_>
    _lessThan_4__A = typing.TypeVar('_lessThan_4__A')  # <A>
    _lessThan_4__B = typing.TypeVar('_lessThan_4__B')  # <B>
    _lessThan_4__C = typing.TypeVar('_lessThan_4__C')  # <C>
    _lessThan_4__Property_ = typing.TypeVar('_lessThan_4__Property_', bound=java.lang.Comparable)  # <Property_>
    @typing.overload
    @staticmethod
    def lessThan(function: typing.Union[java.util.function.Function[_lessThan_0__A, _lessThan_0__Property_], typing.Callable[[_lessThan_0__A], _lessThan_0__Property_]]) -> org.optaplanner.core.api.score.stream.bi.BiJoiner[_lessThan_0__A, _lessThan_0__A]: ...
    @typing.overload
    @staticmethod
    def lessThan(function: typing.Union[java.util.function.Function[_lessThan_1__A, _lessThan_1__Property_], typing.Callable[[_lessThan_1__A], _lessThan_1__Property_]], function2: typing.Union[java.util.function.Function[_lessThan_1__B, _lessThan_1__Property_], typing.Callable[[_lessThan_1__B], _lessThan_1__Property_]]) -> org.optaplanner.core.api.score.stream.bi.BiJoiner[_lessThan_1__A, _lessThan_1__B]: ...
    @typing.overload
    @staticmethod
    def lessThan(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_lessThan_2__A, _lessThan_2__B, _lessThan_2__C, _lessThan_2__D, _lessThan_2__Property_], typing.Callable[[_lessThan_2__A, _lessThan_2__B, _lessThan_2__C, _lessThan_2__D], _lessThan_2__Property_]], function: typing.Union[java.util.function.Function[_lessThan_2__E, _lessThan_2__Property_], typing.Callable[[_lessThan_2__E], _lessThan_2__Property_]]) -> org.optaplanner.core.api.score.stream.penta.PentaJoiner[_lessThan_2__A, _lessThan_2__B, _lessThan_2__C, _lessThan_2__D, _lessThan_2__E]: ...
    @typing.overload
    @staticmethod
    def lessThan(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_lessThan_3__A, _lessThan_3__B, _lessThan_3__C, _lessThan_3__Property_], typing.Callable[[_lessThan_3__A, _lessThan_3__B, _lessThan_3__C], _lessThan_3__Property_]], function: typing.Union[java.util.function.Function[_lessThan_3__D, _lessThan_3__Property_], typing.Callable[[_lessThan_3__D], _lessThan_3__Property_]]) -> org.optaplanner.core.api.score.stream.quad.QuadJoiner[_lessThan_3__A, _lessThan_3__B, _lessThan_3__C, _lessThan_3__D]: ...
    @typing.overload
    @staticmethod
    def lessThan(biFunction: typing.Union[java.util.function.BiFunction[_lessThan_4__A, _lessThan_4__B, _lessThan_4__Property_], typing.Callable[[_lessThan_4__A, _lessThan_4__B], _lessThan_4__Property_]], function: typing.Union[java.util.function.Function[_lessThan_4__C, _lessThan_4__Property_], typing.Callable[[_lessThan_4__C], _lessThan_4__Property_]]) -> org.optaplanner.core.api.score.stream.tri.TriJoiner[_lessThan_4__A, _lessThan_4__B, _lessThan_4__C]: ...
    _lessThanOrEqual_0__A = typing.TypeVar('_lessThanOrEqual_0__A')  # <A>
    _lessThanOrEqual_0__Property_ = typing.TypeVar('_lessThanOrEqual_0__Property_', bound=java.lang.Comparable)  # <Property_>
    _lessThanOrEqual_1__A = typing.TypeVar('_lessThanOrEqual_1__A')  # <A>
    _lessThanOrEqual_1__B = typing.TypeVar('_lessThanOrEqual_1__B')  # <B>
    _lessThanOrEqual_1__Property_ = typing.TypeVar('_lessThanOrEqual_1__Property_', bound=java.lang.Comparable)  # <Property_>
    _lessThanOrEqual_2__A = typing.TypeVar('_lessThanOrEqual_2__A')  # <A>
    _lessThanOrEqual_2__B = typing.TypeVar('_lessThanOrEqual_2__B')  # <B>
    _lessThanOrEqual_2__C = typing.TypeVar('_lessThanOrEqual_2__C')  # <C>
    _lessThanOrEqual_2__D = typing.TypeVar('_lessThanOrEqual_2__D')  # <D>
    _lessThanOrEqual_2__E = typing.TypeVar('_lessThanOrEqual_2__E')  # <E>
    _lessThanOrEqual_2__Property_ = typing.TypeVar('_lessThanOrEqual_2__Property_', bound=java.lang.Comparable)  # <Property_>
    _lessThanOrEqual_3__A = typing.TypeVar('_lessThanOrEqual_3__A')  # <A>
    _lessThanOrEqual_3__B = typing.TypeVar('_lessThanOrEqual_3__B')  # <B>
    _lessThanOrEqual_3__C = typing.TypeVar('_lessThanOrEqual_3__C')  # <C>
    _lessThanOrEqual_3__D = typing.TypeVar('_lessThanOrEqual_3__D')  # <D>
    _lessThanOrEqual_3__Property_ = typing.TypeVar('_lessThanOrEqual_3__Property_', bound=java.lang.Comparable)  # <Property_>
    _lessThanOrEqual_4__A = typing.TypeVar('_lessThanOrEqual_4__A')  # <A>
    _lessThanOrEqual_4__B = typing.TypeVar('_lessThanOrEqual_4__B')  # <B>
    _lessThanOrEqual_4__C = typing.TypeVar('_lessThanOrEqual_4__C')  # <C>
    _lessThanOrEqual_4__Property_ = typing.TypeVar('_lessThanOrEqual_4__Property_', bound=java.lang.Comparable)  # <Property_>
    @typing.overload
    @staticmethod
    def lessThanOrEqual(function: typing.Union[java.util.function.Function[_lessThanOrEqual_0__A, _lessThanOrEqual_0__Property_], typing.Callable[[_lessThanOrEqual_0__A], _lessThanOrEqual_0__Property_]]) -> org.optaplanner.core.api.score.stream.bi.BiJoiner[_lessThanOrEqual_0__A, _lessThanOrEqual_0__A]: ...
    @typing.overload
    @staticmethod
    def lessThanOrEqual(function: typing.Union[java.util.function.Function[_lessThanOrEqual_1__A, _lessThanOrEqual_1__Property_], typing.Callable[[_lessThanOrEqual_1__A], _lessThanOrEqual_1__Property_]], function2: typing.Union[java.util.function.Function[_lessThanOrEqual_1__B, _lessThanOrEqual_1__Property_], typing.Callable[[_lessThanOrEqual_1__B], _lessThanOrEqual_1__Property_]]) -> org.optaplanner.core.api.score.stream.bi.BiJoiner[_lessThanOrEqual_1__A, _lessThanOrEqual_1__B]: ...
    @typing.overload
    @staticmethod
    def lessThanOrEqual(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_lessThanOrEqual_2__A, _lessThanOrEqual_2__B, _lessThanOrEqual_2__C, _lessThanOrEqual_2__D, _lessThanOrEqual_2__Property_], typing.Callable[[_lessThanOrEqual_2__A, _lessThanOrEqual_2__B, _lessThanOrEqual_2__C, _lessThanOrEqual_2__D], _lessThanOrEqual_2__Property_]], function: typing.Union[java.util.function.Function[_lessThanOrEqual_2__E, _lessThanOrEqual_2__Property_], typing.Callable[[_lessThanOrEqual_2__E], _lessThanOrEqual_2__Property_]]) -> org.optaplanner.core.api.score.stream.penta.PentaJoiner[_lessThanOrEqual_2__A, _lessThanOrEqual_2__B, _lessThanOrEqual_2__C, _lessThanOrEqual_2__D, _lessThanOrEqual_2__E]: ...
    @typing.overload
    @staticmethod
    def lessThanOrEqual(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_lessThanOrEqual_3__A, _lessThanOrEqual_3__B, _lessThanOrEqual_3__C, _lessThanOrEqual_3__Property_], typing.Callable[[_lessThanOrEqual_3__A, _lessThanOrEqual_3__B, _lessThanOrEqual_3__C], _lessThanOrEqual_3__Property_]], function: typing.Union[java.util.function.Function[_lessThanOrEqual_3__D, _lessThanOrEqual_3__Property_], typing.Callable[[_lessThanOrEqual_3__D], _lessThanOrEqual_3__Property_]]) -> org.optaplanner.core.api.score.stream.quad.QuadJoiner[_lessThanOrEqual_3__A, _lessThanOrEqual_3__B, _lessThanOrEqual_3__C, _lessThanOrEqual_3__D]: ...
    @typing.overload
    @staticmethod
    def lessThanOrEqual(biFunction: typing.Union[java.util.function.BiFunction[_lessThanOrEqual_4__A, _lessThanOrEqual_4__B, _lessThanOrEqual_4__Property_], typing.Callable[[_lessThanOrEqual_4__A, _lessThanOrEqual_4__B], _lessThanOrEqual_4__Property_]], function: typing.Union[java.util.function.Function[_lessThanOrEqual_4__C, _lessThanOrEqual_4__Property_], typing.Callable[[_lessThanOrEqual_4__C], _lessThanOrEqual_4__Property_]]) -> org.optaplanner.core.api.score.stream.tri.TriJoiner[_lessThanOrEqual_4__A, _lessThanOrEqual_4__B, _lessThanOrEqual_4__C]: ...
    _overlapping_0__A = typing.TypeVar('_overlapping_0__A')  # <A>
    _overlapping_0__Property_ = typing.TypeVar('_overlapping_0__Property_', bound=java.lang.Comparable)  # <Property_>
    _overlapping_1__A = typing.TypeVar('_overlapping_1__A')  # <A>
    _overlapping_1__B = typing.TypeVar('_overlapping_1__B')  # <B>
    _overlapping_1__Property_ = typing.TypeVar('_overlapping_1__Property_', bound=java.lang.Comparable)  # <Property_>
    _overlapping_2__A = typing.TypeVar('_overlapping_2__A')  # <A>
    _overlapping_2__B = typing.TypeVar('_overlapping_2__B')  # <B>
    _overlapping_2__C = typing.TypeVar('_overlapping_2__C')  # <C>
    _overlapping_2__D = typing.TypeVar('_overlapping_2__D')  # <D>
    _overlapping_2__E = typing.TypeVar('_overlapping_2__E')  # <E>
    _overlapping_2__Property_ = typing.TypeVar('_overlapping_2__Property_', bound=java.lang.Comparable)  # <Property_>
    _overlapping_3__A = typing.TypeVar('_overlapping_3__A')  # <A>
    _overlapping_3__B = typing.TypeVar('_overlapping_3__B')  # <B>
    _overlapping_3__C = typing.TypeVar('_overlapping_3__C')  # <C>
    _overlapping_3__D = typing.TypeVar('_overlapping_3__D')  # <D>
    _overlapping_3__Property_ = typing.TypeVar('_overlapping_3__Property_', bound=java.lang.Comparable)  # <Property_>
    _overlapping_4__A = typing.TypeVar('_overlapping_4__A')  # <A>
    _overlapping_4__B = typing.TypeVar('_overlapping_4__B')  # <B>
    _overlapping_4__C = typing.TypeVar('_overlapping_4__C')  # <C>
    _overlapping_4__Property_ = typing.TypeVar('_overlapping_4__Property_', bound=java.lang.Comparable)  # <Property_>
    @typing.overload
    @staticmethod
    def overlapping(function: typing.Union[java.util.function.Function[_overlapping_0__A, _overlapping_0__Property_], typing.Callable[[_overlapping_0__A], _overlapping_0__Property_]], function2: typing.Union[java.util.function.Function[_overlapping_0__A, _overlapping_0__Property_], typing.Callable[[_overlapping_0__A], _overlapping_0__Property_]]) -> org.optaplanner.core.api.score.stream.bi.BiJoiner[_overlapping_0__A, _overlapping_0__A]: ...
    @typing.overload
    @staticmethod
    def overlapping(function: typing.Union[java.util.function.Function[_overlapping_1__A, _overlapping_1__Property_], typing.Callable[[_overlapping_1__A], _overlapping_1__Property_]], function2: typing.Union[java.util.function.Function[_overlapping_1__A, _overlapping_1__Property_], typing.Callable[[_overlapping_1__A], _overlapping_1__Property_]], function3: typing.Union[java.util.function.Function[_overlapping_1__B, _overlapping_1__Property_], typing.Callable[[_overlapping_1__B], _overlapping_1__Property_]], function4: typing.Union[java.util.function.Function[_overlapping_1__B, _overlapping_1__Property_], typing.Callable[[_overlapping_1__B], _overlapping_1__Property_]]) -> org.optaplanner.core.api.score.stream.bi.BiJoiner[_overlapping_1__A, _overlapping_1__B]: ...
    @typing.overload
    @staticmethod
    def overlapping(quadFunction: typing.Union[org.optaplanner.core.api.function.QuadFunction[_overlapping_2__A, _overlapping_2__B, _overlapping_2__C, _overlapping_2__D, _overlapping_2__Property_], typing.Callable[[_overlapping_2__A, _overlapping_2__B, _overlapping_2__C, _overlapping_2__D], _overlapping_2__Property_]], quadFunction2: typing.Union[org.optaplanner.core.api.function.QuadFunction[_overlapping_2__A, _overlapping_2__B, _overlapping_2__C, _overlapping_2__D, _overlapping_2__Property_], typing.Callable[[_overlapping_2__A, _overlapping_2__B, _overlapping_2__C, _overlapping_2__D], _overlapping_2__Property_]], function: typing.Union[java.util.function.Function[_overlapping_2__E, _overlapping_2__Property_], typing.Callable[[_overlapping_2__E], _overlapping_2__Property_]], function2: typing.Union[java.util.function.Function[_overlapping_2__E, _overlapping_2__Property_], typing.Callable[[_overlapping_2__E], _overlapping_2__Property_]]) -> org.optaplanner.core.api.score.stream.penta.PentaJoiner[_overlapping_2__A, _overlapping_2__B, _overlapping_2__C, _overlapping_2__D, _overlapping_2__E]: ...
    @typing.overload
    @staticmethod
    def overlapping(triFunction: typing.Union[org.optaplanner.core.api.function.TriFunction[_overlapping_3__A, _overlapping_3__B, _overlapping_3__C, _overlapping_3__Property_], typing.Callable[[_overlapping_3__A, _overlapping_3__B, _overlapping_3__C], _overlapping_3__Property_]], triFunction2: typing.Union[org.optaplanner.core.api.function.TriFunction[_overlapping_3__A, _overlapping_3__B, _overlapping_3__C, _overlapping_3__Property_], typing.Callable[[_overlapping_3__A, _overlapping_3__B, _overlapping_3__C], _overlapping_3__Property_]], function: typing.Union[java.util.function.Function[_overlapping_3__D, _overlapping_3__Property_], typing.Callable[[_overlapping_3__D], _overlapping_3__Property_]], function2: typing.Union[java.util.function.Function[_overlapping_3__D, _overlapping_3__Property_], typing.Callable[[_overlapping_3__D], _overlapping_3__Property_]]) -> org.optaplanner.core.api.score.stream.quad.QuadJoiner[_overlapping_3__A, _overlapping_3__B, _overlapping_3__C, _overlapping_3__D]: ...
    @typing.overload
    @staticmethod
    def overlapping(biFunction: typing.Union[java.util.function.BiFunction[_overlapping_4__A, _overlapping_4__B, _overlapping_4__Property_], typing.Callable[[_overlapping_4__A, _overlapping_4__B], _overlapping_4__Property_]], biFunction2: typing.Union[java.util.function.BiFunction[_overlapping_4__A, _overlapping_4__B, _overlapping_4__Property_], typing.Callable[[_overlapping_4__A, _overlapping_4__B], _overlapping_4__Property_]], function: typing.Union[java.util.function.Function[_overlapping_4__C, _overlapping_4__Property_], typing.Callable[[_overlapping_4__C], _overlapping_4__Property_]], function2: typing.Union[java.util.function.Function[_overlapping_4__C, _overlapping_4__Property_], typing.Callable[[_overlapping_4__C], _overlapping_4__Property_]]) -> org.optaplanner.core.api.score.stream.tri.TriJoiner[_overlapping_4__A, _overlapping_4__B, _overlapping_4__C]: ...

class DefaultConstraintJustification(ConstraintJustification, java.lang.Comparable['DefaultConstraintJustification']):
    def compareTo(self, defaultConstraintJustification: 'DefaultConstraintJustification') -> int: ...
    def getFacts(self) -> java.util.List[typing.Any]: ...
    _getImpact__Score_ = typing.TypeVar('_getImpact__Score_', bound=org.optaplanner.core.api.score.Score)  # <Score_>
    def getImpact(self) -> _getImpact__Score_: ...
    @typing.overload
    @staticmethod
    def of(score: org.optaplanner.core.api.score.Score[typing.Any], object: typing.Any) -> 'DefaultConstraintJustification': ...
    @typing.overload
    @staticmethod
    def of(score: org.optaplanner.core.api.score.Score[typing.Any], object: typing.Any, object2: typing.Any) -> 'DefaultConstraintJustification': ...
    @typing.overload
    @staticmethod
    def of(score: org.optaplanner.core.api.score.Score[typing.Any], object: typing.Any, object2: typing.Any, object3: typing.Any) -> 'DefaultConstraintJustification': ...
    @typing.overload
    @staticmethod
    def of(score: org.optaplanner.core.api.score.Score[typing.Any], object: typing.Any, object2: typing.Any, object3: typing.Any, object4: typing.Any) -> 'DefaultConstraintJustification': ...
    @typing.overload
    @staticmethod
    def of(score: org.optaplanner.core.api.score.Score[typing.Any], *object: typing.Any) -> 'DefaultConstraintJustification': ...
    @typing.overload
    @staticmethod
    def of(score: org.optaplanner.core.api.score.Score[typing.Any], list: java.util.List[typing.Any]) -> 'DefaultConstraintJustification': ...
    def toString(self) -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.api.score.stream")``.

    Constraint: typing.Type[Constraint]
    ConstraintBuilder: typing.Type[ConstraintBuilder]
    ConstraintCollectors: typing.Type[ConstraintCollectors]
    ConstraintFactory: typing.Type[ConstraintFactory]
    ConstraintJustification: typing.Type[ConstraintJustification]
    ConstraintProvider: typing.Type[ConstraintProvider]
    ConstraintStream: typing.Type[ConstraintStream]
    ConstraintStreamImplType: typing.Type[ConstraintStreamImplType]
    DefaultConstraintJustification: typing.Type[DefaultConstraintJustification]
    Joiners: typing.Type[Joiners]
    bi: org.optaplanner.core.api.score.stream.bi.__module_protocol__
    penta: org.optaplanner.core.api.score.stream.penta.__module_protocol__
    quad: org.optaplanner.core.api.score.stream.quad.__module_protocol__
    tri: org.optaplanner.core.api.score.stream.tri.__module_protocol__
    uni: org.optaplanner.core.api.score.stream.uni.__module_protocol__
