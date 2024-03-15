
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang.annotation
import java.lang.reflect
import java.util
import java.util.function
import org.optaplanner.core.api.domain.common
import org.optaplanner.core.config
import org.optaplanner.core.impl.domain.common.accessor
import typing



class ConfigUtils:
    @typing.overload
    @staticmethod
    def abbreviate(list: java.util.List[str]) -> str: ...
    @typing.overload
    @staticmethod
    def abbreviate(list: java.util.List[str], int: int) -> str: ...
    @staticmethod
    def applyCustomProperties(object: typing.Any, string: str, map: typing.Union[java.util.Map[str, str], typing.Mapping[str, str]], string2: str) -> None: ...
    @staticmethod
    def ceilDivide(int: int, int2: int) -> int: ...
    @staticmethod
    def extractAnnotationClass(member: java.lang.reflect.Member, *class_: typing.Type[java.lang.annotation.Annotation]) -> typing.Type[java.lang.annotation.Annotation]: ...
    @staticmethod
    def extractCollectionGenericTypeParameterLeniently(string: str, class_: typing.Type[typing.Any], class2: typing.Type[typing.Any], type: java.lang.reflect.Type, class3: typing.Type[java.lang.annotation.Annotation], string2: str) -> java.util.Optional[typing.Type[typing.Any]]: ...
    @staticmethod
    def extractCollectionGenericTypeParameterStrictly(string: str, class_: typing.Type[typing.Any], class2: typing.Type[typing.Any], type: java.lang.reflect.Type, class3: typing.Type[java.lang.annotation.Annotation], string2: str) -> typing.Type[typing.Any]: ...
    _findPlanningIdMemberAccessor__C = typing.TypeVar('_findPlanningIdMemberAccessor__C')  # <C>
    @staticmethod
    def findPlanningIdMemberAccessor(class_: typing.Type[_findPlanningIdMemberAccessor__C], memberAccessorFactory: org.optaplanner.core.impl.domain.common.accessor.MemberAccessorFactory, domainAccessType: org.optaplanner.core.api.domain.common.DomainAccessType) -> org.optaplanner.core.impl.domain.common.accessor.MemberAccessor: ...
    @staticmethod
    def getAllAnnotatedLineageClasses(class_: typing.Type[typing.Any], class2: typing.Type[java.lang.annotation.Annotation]) -> java.util.List[typing.Type[typing.Any]]: ...
    @staticmethod
    def getAllMembers(class_: typing.Type[typing.Any], class2: typing.Type[java.lang.annotation.Annotation]) -> java.util.List[java.lang.reflect.Member]: ...
    @staticmethod
    def getDeclaredMembers(class_: typing.Type[typing.Any]) -> java.util.List[java.lang.reflect.Member]: ...
    _inheritConfig__Config_ = typing.TypeVar('_inheritConfig__Config_', bound=org.optaplanner.core.config.AbstractConfig)  # <Config_>
    @staticmethod
    def inheritConfig(config_: _inheritConfig__Config_, config_2: _inheritConfig__Config_) -> _inheritConfig__Config_: ...
    _inheritMergeableListConfig__Config_ = typing.TypeVar('_inheritMergeableListConfig__Config_', bound=org.optaplanner.core.config.AbstractConfig)  # <Config_>
    @staticmethod
    def inheritMergeableListConfig(list: java.util.List[_inheritMergeableListConfig__Config_], list2: java.util.List[_inheritMergeableListConfig__Config_]) -> java.util.List[_inheritMergeableListConfig__Config_]: ...
    _inheritMergeableListProperty__T = typing.TypeVar('_inheritMergeableListProperty__T')  # <T>
    @staticmethod
    def inheritMergeableListProperty(list: java.util.List[_inheritMergeableListProperty__T], list2: java.util.List[_inheritMergeableListProperty__T]) -> java.util.List[_inheritMergeableListProperty__T]: ...
    _inheritMergeableMapProperty__K = typing.TypeVar('_inheritMergeableMapProperty__K')  # <K>
    _inheritMergeableMapProperty__T = typing.TypeVar('_inheritMergeableMapProperty__T')  # <T>
    @staticmethod
    def inheritMergeableMapProperty(map: typing.Union[java.util.Map[_inheritMergeableMapProperty__K, _inheritMergeableMapProperty__T], typing.Mapping[_inheritMergeableMapProperty__K, _inheritMergeableMapProperty__T]], map2: typing.Union[java.util.Map[_inheritMergeableMapProperty__K, _inheritMergeableMapProperty__T], typing.Mapping[_inheritMergeableMapProperty__K, _inheritMergeableMapProperty__T]]) -> java.util.Map[_inheritMergeableMapProperty__K, _inheritMergeableMapProperty__T]: ...
    _inheritOverwritableProperty__T = typing.TypeVar('_inheritOverwritableProperty__T')  # <T>
    @staticmethod
    def inheritOverwritableProperty(t: _inheritOverwritableProperty__T, t2: _inheritOverwritableProperty__T) -> _inheritOverwritableProperty__T: ...
    @staticmethod
    def isEmptyCollection(collection: typing.Union[java.util.Collection[typing.Any], typing.Sequence[typing.Any], typing.Set[typing.Any]]) -> bool: ...
    @staticmethod
    def isNativeImage() -> bool: ...
    _meldProperty__T = typing.TypeVar('_meldProperty__T')  # <T>
    @staticmethod
    def meldProperty(t: _meldProperty__T, t2: _meldProperty__T) -> _meldProperty__T: ...
    _mergeProperty__T = typing.TypeVar('_mergeProperty__T')  # <T>
    @staticmethod
    def mergeProperty(t: _mergeProperty__T, t2: _mergeProperty__T) -> _mergeProperty__T: ...
    _newInstance_0__T = typing.TypeVar('_newInstance_0__T')  # <T>
    _newInstance_1__T = typing.TypeVar('_newInstance_1__T')  # <T>
    @typing.overload
    @staticmethod
    def newInstance(object: typing.Any, string: str, class_: typing.Type[_newInstance_0__T]) -> _newInstance_0__T: ...
    @typing.overload
    @staticmethod
    def newInstance(supplier: typing.Union[java.util.function.Supplier[str], typing.Callable[[], str]], string: str, class_: typing.Type[_newInstance_1__T]) -> _newInstance_1__T: ...
    @staticmethod
    def resolvePoolSize(string: str, string2: str, *string3: str) -> int: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.config.util")``.

    ConfigUtils: typing.Type[ConfigUtils]
