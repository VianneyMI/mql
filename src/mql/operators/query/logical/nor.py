# Standard Library imports
# ----------------------------
from typing import List

# Local imports
# ----------------------------
from mql.base import Expression
from mql.operators.base import BaseOperator


class Nor(BaseOperator):
    """Logical NOR operator"""

    __symbol__ = "$nor"

    right: List[Expression]

    @property
    def expression(self) -> Expression:
        return {self.symbol: self.right}
