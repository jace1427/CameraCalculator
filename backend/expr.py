"""expr.py

Author: Justin Spidell
"""
import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# One global environment (scope) for
# the calculator
ENV = dict()


def env_clear():
    """Clear all variables in calculator memory."""
    global ENV
    ENV = dict()


class Expr(object):
    """Abstract base class of all expressions."""

    def eval(self) -> "Const":
        """Implementations of eval should return an integer constant."""
        raise NotImplementedError(
            'Each concrete Expr class must define "eval"')

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in
        algebraic notation
        """
        raise NotImplementedError(
            'Each concrete Expr class must define __str__')

    def __repr__(self) -> str:
        """Implementations of __repr__ should return a string that looks like
        the constructor, e.g., Plus(Const(5), Const(4))
        """
        raise NotImplementedError(
            'Each concrete Expr class must define __repr__')

    def _find_var(self, curr):
        log.debug(f"_find_var:{curr.__repr__()}")
        if isinstance(curr, Var):
            return True
        if isinstance(curr, Const):
            return False
        if not isinstance(curr.left, Const):
            if self._find_var(curr.left):
                return True
        if not isinstance(curr.right, Const):
            if self._find_var(curr.right):
                return True
        return False


class Const(Expr):
    """Class for integers, used for all Expr functions."""

    def __init__(self, value: int):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f'Const({self.value})'

    def eval(self) -> 'Const':
        """Eval of a constant integer is a constant integer."""
        log.debug(self.__repr__())
        return self

    def __eq__(self, other: Expr) -> bool:
        return isinstance(other, Const) and self.value == other.value


class BinOp(Expr):
    """Abstract base class of all binary operation classes."""

    def __init__(self):
        raise NotImplementedError('Do not instantiate BinOp')

    def _binop_init(self, left: Expr, right: Expr, op_sym: str, op_name: str):
        self.left = left
        self.right = right
        self.op_sym = op_sym
        self.op_name = op_name

    def __str__(self) -> str:
        return f'({self.left} {self.op_sym} {self.right})'

    def __repr__(self) -> str:
        return f'{self.op_name}({repr(self.left)}, {repr(self.right)})'

    def eval(self) -> 'Const':
        """Each concrete subclass must define _apply(int, int) -> int"""
        log.debug(self.__repr__())
        left_val = self.left.eval()
        right_val = self.right.eval()
        return Const(self._apply(left_val.value, right_val.value))

    def _reverse(self, other):
        log.debug(f"_reverse:{self.__repr__()}")

        if isinstance(self, Const):
            raise SyntaxError(
                "_reverse should never be called on an Const")

        if isinstance(self.left, Var) or self._find_var(self.left):
            new_other = self._opp(other, self.right)
            new_self = self.left

        elif isinstance(self.right, Var) or self._find_var(self.right):
            if (not isinstance(self, Minus)) and (not isinstance(self, Div)):
                new_other = self._opp(other, self.left)
                new_self = self.right
            else:
                if isinstance(self, Minus):
                    new_other = Neg(Minus(other, self.left))
                    new_self = self.right
                elif isinstance(self, Div):
                    new_other = Times(self.left, Div(Const(1), other))
                    new_self = self.right
        return new_self, new_other


class Plus(BinOp):
    """Expr + Expr"""

    def __init__(self, left: Expr, right: Expr):
        self._binop_init(left, right, '+', 'Plus')

    def _apply(self, left: int, right: int) -> int:
        return left + right

    def _opp(self, left, right):
        return Minus(left, right)


class Minus(BinOp):
    """Expr - Expr"""

    def __init__(self, left: Expr, right: Expr):
        self._binop_init(left, right, '-', 'Minus')

    def _apply(self, left: int, right: int) -> int:
        return left - right

    def _opp(self, left, right):
        return Plus(left, right)


class Times(BinOp):
    """Expr * Expr"""

    def __init__(self, left: Expr, right: Expr):
        self._binop_init(left, right, '*', 'Times')

    def _apply(self, left: int, right: int) -> int:
        return left * right

    def _opp(self, left, right):
        return Div(left, right)


class Div(BinOp):
    """Expr // Expr"""

    def __init__(self, left: Expr, right: Expr):
        self._binop_init(left, right, '/', 'Div')

    def _apply(self, left: int, right: int) -> int:
        return left / right

    def _opp(self, left, right):
        return Times(left, right)


class Unop(Expr):
    """Abstract base class of all Unary operations."""

    def __init__(self):
        raise NotImplementedError('Do not instantiate UnOp')

    def _Unop_init(self, left: Expr, op_sym: str, op_name: str):
        self.left = left
        self.op_sym = op_sym
        self.op_name = op_name

    def __str__(self) -> str:
        return f'{self.op_sym} {self.left}'

    def __repr__(self) -> str:
        return f'{self.op_name}({repr(self.left)})'

    def eval(self) -> 'Const':
        log.debug(self.__repr__())
        left_val = self.left.eval()
        return Const(self._apply(left_val.value))


class Abs(Unop):
    """Abs(Expr)"""

    def __init__(self, left: Expr):
        self._Unop_init(left, '@', 'Abs')

    def _apply(self, left: int) -> int:
        return abs(left)


class Neg(Unop):
    """-(Expr)"""

    def __init__(self, left: Expr):
        self._Unop_init(left, '~', 'Neg')

    def _apply(self, left: int) -> int:
        return -left


class UndefinedVariable(Exception):
    """Raised when expression tries to use a variable that
    is not in ENV
    """
    pass


class Var(Expr):
    """Variable class, for any token that isn't an integer,
    x = repersented as Var(x).
    """

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'Var({self.name})'

    def eval(self) -> str:
        global ENV
        if self.name in ENV:
            return ENV[self.name]
        else:
            raise UndefinedVariable(
                f'{self.name} has not been assigned a value')
        log.debug(self.__repr__())
        pass

    def assign(self, value: Const):
        global ENV
        ENV[self.name] = value


class Equals(Expr):
    """Equals: x = y represented as Equals(x, y)."""

    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right

    def eval(self) -> Const:
        log.debug(self.__repr__())

        if isinstance(self.left, Var):
            log.debug("Var on left")
            r_val = self.right.eval()
            self.left.assign(r_val)
            return r_val

        elif isinstance(self.right, Var):
            log.debug("Var on right")
            l_val = self.left.eval()
            self.right.assign(l_val)
            return l_val

        else:
            if isinstance(self.left, Const):
                left = False
            else:
                left = self._find_var(self.left)
            if isinstance(self.right, Const):
                right = False
            else:
                right = self._find_var(self.right)

            if left:
                log.debug("solving left side")
                self._isolate("left")
                return self.eval()
            elif right:
                log.debug("solving right side")
                self._isolate("right")
                return self.eval()
            else:
                raise NotImplementedError(
                    "Tried to solve but couldn't find the variable")

    def _isolate(self, left_right):
        if left_right == "left":
            self.left, self.right = self.left._reverse(self.right)
        if left_right == "right":
            self.right, self.left = self.right._reverse(self.left)

    def __str__(self) -> str:
        return f'{self.left} = {self.right}'

    def __repr__(self) -> str:
        return f'Equals({self.left.__repr__()}, {self.right.__repr__()})'
