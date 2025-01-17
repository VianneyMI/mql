# Standard Library imports
# ----------------------------
from typing import Any

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class AddToSet(BaseOperator):
    """Update operator to add elements to array only if they don't exist"""

    __symbol__ = "$addToSet"

    left: str
    right: Any

    @property
    def expression(self) -> Expression:
        return {self.symbol: {self.left: self.right}}