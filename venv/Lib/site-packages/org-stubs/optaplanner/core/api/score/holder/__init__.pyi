
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.kie.api.runtime.rule
import org.optaplanner.core.api.score
import typing



_ScoreHolder__Score_ = typing.TypeVar('_ScoreHolder__Score_', bound=org.optaplanner.core.api.score.Score)  # <Score_>
class ScoreHolder(typing.Generic[_ScoreHolder__Score_]):
    def penalize(self, ruleContext: org.kie.api.runtime.rule.RuleContext) -> None: ...
    def reward(self, ruleContext: org.kie.api.runtime.rule.RuleContext) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.optaplanner.core.api.score.holder")``.

    ScoreHolder: typing.Type[ScoreHolder]
