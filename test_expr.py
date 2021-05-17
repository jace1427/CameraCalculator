"""Test cases for expr.py
Michal Young, 2020.01.17
"""
import unittest
from expr import *


class TestIntConst(unittest.TestCase):

    def test_eval(self):
        five = IntConst(5)
        self.assertEqual(five.eval(), IntConst(5))

    def test_str(self):
        twelve = IntConst(12)
        self.assertEqual(str(twelve), "12")

    def test_repr(self):
        forty_two = IntConst(42)
        self.assertEqual(repr(forty_two), f"IntConst(42)")


class TestPlus(unittest.TestCase):

    def test_plus_str(self):
        exp = Plus(IntConst(5), IntConst(4))
        self.assertEqual(str(exp), "(5 + 4)")

    def test_nested_str(self):
        exp = Plus(Plus(IntConst(4), IntConst(5)), IntConst(3))
        self.assertEqual(str(exp), "((4 + 5) + 3)")

    def test_repr_simple(self):
        exp = Plus(IntConst(12), IntConst(13))
        self.assertEqual(repr(exp), "Plus(IntConst(12), IntConst(13))")

    def test_repr_nested(self):
        exp = Plus(IntConst(7), Plus(IntConst(4), IntConst(2)))
        self.assertEqual(repr(exp),
                         "Plus(IntConst(7), Plus(IntConst(4), IntConst(2)))")

    def test_simple(self):
        exp = Plus(IntConst(4), IntConst(8))
        self.assertEqual(exp.eval(), IntConst(12))

    def test_nested(self):
        exp = Plus(IntConst(7), Plus(IntConst(2), IntConst(3)))
        self.assertEqual(exp.eval(), IntConst(12))


class TestMinus(unittest.TestCase):

    def test_Minus_str(self):
        exp = Minus(IntConst(5), IntConst(4))
        self.assertEqual(str(exp), "(5 - 4)")

    def test_nested_str(self):
        exp = Minus(Minus(IntConst(4), IntConst(5)), IntConst(3))
        self.assertEqual(str(exp), "((4 - 5) - 3)")

    def test_repr_simple(self):
        exp = Minus(IntConst(12), IntConst(13))
        self.assertEqual(repr(exp), "Minus(IntConst(12), IntConst(13))")

    def test_repr_nested(self):
        exp = Minus(IntConst(7), Minus(IntConst(4), IntConst(2)))
        self.assertEqual(repr(exp),
                         "Minus(IntConst(7), Minus(IntConst(4), IntConst(2)))")

    def test_simple(self):
        exp = Minus(IntConst(4), IntConst(8))
        self.assertEqual(exp.eval(), IntConst(-4))

    def test_nested(self):
        exp = Minus(IntConst(7), Minus(IntConst(2), IntConst(3)))
        self.assertEqual(exp.eval(), IntConst(8))


class TestDiv(unittest.TestCase):

    def test_Div_str(self):
        exp = Div(IntConst(5), IntConst(4))
        self.assertEqual(str(exp), "(5 / 4)")

    def test_nested_str(self):
        exp = Div(Div(IntConst(4), IntConst(5)), IntConst(3))
        self.assertEqual(str(exp), "((4 / 5) / 3)")

    def test_repr_simple(self):
        exp = Div(IntConst(12), IntConst(13))
        self.assertEqual(repr(exp), "Div(IntConst(12), IntConst(13))")

    def test_repr_nested(self):
        exp = Div(IntConst(7), Div(IntConst(4), IntConst(2)))
        self.assertEqual(repr(exp),
                         "Div(IntConst(7), Div(IntConst(4), IntConst(2)))")

    def test_simple(self):
        exp = Div(IntConst(4), IntConst(8))
        self.assertEqual(exp.eval(), IntConst(0.5))

    def test_nested(self):
        exp = Div(IntConst(7), Div(IntConst(2), IntConst(3)))
        self.assertEqual(exp.eval(), IntConst(10.5))


class TestTimes(unittest.TestCase):

    def test_Times_str(self):
        exp = Times(IntConst(5), IntConst(4))
        self.assertEqual(str(exp), "(5 * 4)")

    def test_nested_str(self):
        exp = Times(Times(IntConst(4), IntConst(5)), IntConst(3))
        self.assertEqual(str(exp), "((4 * 5) * 3)")

    def test_repr_simple(self):
        exp = Times(IntConst(12), IntConst(13))
        self.assertEqual(repr(exp), "Times(IntConst(12), IntConst(13))")

    def test_repr_nested(self):
        exp = Times(IntConst(7), Times(IntConst(4), IntConst(2)))
        self.assertEqual(repr(exp),
                         "Times(IntConst(7), Times(IntConst(4), IntConst(2)))")

    def test_simple(self):
        exp = Times(IntConst(4), IntConst(8))
        self.assertEqual(exp.eval(), IntConst(32))

    def test_nested(self):
        exp = Times(IntConst(7), Times(IntConst(2), IntConst(3)))
        self.assertEqual(exp.eval(), IntConst(42))


# #
# # Tests of UnOp alone
# #


class TestUnOp(unittest.TestCase):

    def test_repr_simple(self):
        exp = Abs(IntConst(5))
        self.assertEqual(repr(exp), "Abs(IntConst(5))")
        exp = Neg(IntConst(6))
        self.assertEqual(repr(exp), "Neg(IntConst(6))")

    def test_str_simple(self):
        exp = Abs(IntConst(12))
        self.assertEqual(str(exp), "@ 12")
        exp = Neg(IntConst(13))
        self.assertEqual(str(exp), "~ 13")

    def test_abs_eval(self):
        exp = Minus(IntConst(3), IntConst(5))
        self.assertEqual(exp.eval(), IntConst(-2))
        exp = Abs(exp)
        self.assertEqual(exp.eval(), IntConst(2))

    def test_neg_eval(self):
        exp = Minus(IntConst(12), IntConst(8))
        self.assertEqual(exp.eval(), IntConst(4))
        exp = Neg(exp)
        self.assertEqual(exp.eval(), IntConst(-4))


class TestEquals(unittest.TestCase):

    def test_assign_left(self):
        v = Var("v")
        w = Var("w")
        exp = Equals(v, IntConst(5))
        self.assertEqual(exp.eval(), IntConst(5))
        self.assertEqual(v.eval(), IntConst(5))
        exp = Equals(w, v)
        self.assertEqual(exp.eval(), IntConst(5))
        self.assertEqual(w.eval(), IntConst(5))

    def test_assign_right(self):
        v = Var("v")
        w = Var("w")
        exp = Equals(IntConst(5), v)
        self.assertEqual(exp.eval(), IntConst(5))
        self.assertEqual(v.eval(), IntConst(5))
        exp = Equals(w, v)
        self.assertEqual(exp.eval(), IntConst(5))
        self.assertEqual(w.eval(), IntConst(5))

    def test_solve_easy_right(self):
        v = Var("v")
        exp = Equals(v, Plus(IntConst(5), IntConst(2)))
        self.assertEquals(exp.eval(), IntConst(7))

    def test_solve_easy_left(self):
        v = Var("v")
        exp = Equals(Plus(IntConst(5), IntConst(2)), v)
        self.assertEquals(exp.eval(), IntConst(7))

    def test_solve_hard(self):
        v = Var("v")
        exp = Equals(Plus(v, IntConst(3)), Minus(IntConst(9), IntConst(4)))
        self.assertEquals(exp.eval(), IntConst(2))


if __name__ == "__main__":
    unittest.main()