"""Test cases for expr.py
Michal Young, 2020.01.17
"""
import unittest
from expr import *


class TestConst(unittest.TestCase):

    def test_eval(self):
        five = Const(5)
        self.assertEqual(five.eval(), Const(5))

    def test_str(self):
        twelve = Const(12)
        self.assertEqual(str(twelve), "12")

    def test_repr(self):
        forty_two = Const(42)
        self.assertEqual(repr(forty_two), f"Const(42)")


class TestPlus(unittest.TestCase):

    def test_plus_str(self):
        exp = Plus(Const(5), Const(4))
        self.assertEqual(str(exp), "(5 + 4)")

    def test_nested_str(self):
        exp = Plus(Plus(Const(4), Const(5)), Const(3))
        self.assertEqual(str(exp), "((4 + 5) + 3)")

    def test_repr_simple(self):
        exp = Plus(Const(12), Const(13))
        self.assertEqual(repr(exp), "Plus(Const(12), Const(13))")

    def test_repr_nested(self):
        exp = Plus(Const(7), Plus(Const(4), Const(2)))
        self.assertEqual(repr(exp),
                         "Plus(Const(7), Plus(Const(4), Const(2)))")

    def test_simple(self):
        exp = Plus(Const(4), Const(8))
        self.assertEqual(exp.eval(), Const(12))

    def test_nested(self):
        exp = Plus(Const(7), Plus(Const(2), Const(3)))
        self.assertEqual(exp.eval(), Const(12))


class TestMinus(unittest.TestCase):

    def test_Minus_str(self):
        exp = Minus(Const(5), Const(4))
        self.assertEqual(str(exp), "(5 - 4)")

    def test_nested_str(self):
        exp = Minus(Minus(Const(4), Const(5)), Const(3))
        self.assertEqual(str(exp), "((4 - 5) - 3)")

    def test_repr_simple(self):
        exp = Minus(Const(12), Const(13))
        self.assertEqual(repr(exp), "Minus(Const(12), Const(13))")

    def test_repr_nested(self):
        exp = Minus(Const(7), Minus(Const(4), Const(2)))
        self.assertEqual(repr(exp),
                         "Minus(Const(7), Minus(Const(4), Const(2)))")

    def test_simple(self):
        exp = Minus(Const(4), Const(8))
        self.assertEqual(exp.eval(), Const(-4))

    def test_nested(self):
        exp = Minus(Const(7), Minus(Const(2), Const(3)))
        self.assertEqual(exp.eval(), Const(8))


class TestDiv(unittest.TestCase):

    def test_Div_str(self):
        exp = Div(Const(5), Const(4))
        self.assertEqual(str(exp), "(5 / 4)")

    def test_nested_str(self):
        exp = Div(Div(Const(4), Const(5)), Const(3))
        self.assertEqual(str(exp), "((4 / 5) / 3)")

    def test_repr_simple(self):
        exp = Div(Const(12), Const(13))
        self.assertEqual(repr(exp), "Div(Const(12), Const(13))")

    def test_repr_nested(self):
        exp = Div(Const(7), Div(Const(4), Const(2)))
        self.assertEqual(repr(exp),
                         "Div(Const(7), Div(Const(4), Const(2)))")

    def test_simple(self):
        exp = Div(Const(4), Const(8))
        self.assertEqual(exp.eval(), Const(0.5))

    def test_nested(self):
        exp = Div(Const(7), Div(Const(2), Const(3)))
        self.assertEqual(exp.eval(), Const(10.5))


class TestTimes(unittest.TestCase):

    def test_Times_str(self):
        exp = Times(Const(5), Const(4))
        self.assertEqual(str(exp), "(5 * 4)")

    def test_nested_str(self):
        exp = Times(Times(Const(4), Const(5)), Const(3))
        self.assertEqual(str(exp), "((4 * 5) * 3)")

    def test_repr_simple(self):
        exp = Times(Const(12), Const(13))
        self.assertEqual(repr(exp), "Times(Const(12), Const(13))")

    def test_repr_nested(self):
        exp = Times(Const(7), Times(Const(4), Const(2)))
        self.assertEqual(repr(exp),
                         "Times(Const(7), Times(Const(4), Const(2)))")

    def test_simple(self):
        exp = Times(Const(4), Const(8))
        self.assertEqual(exp.eval(), Const(32))

    def test_nested(self):
        exp = Times(Const(7), Times(Const(2), Const(3)))
        self.assertEqual(exp.eval(), Const(42))


class TestRaise(unittest.TestCase):

    def test_Raise_str(self):
        exp = Raise(Const(5), Const(4))
        self.assertEqual(str(exp), "(5 ^ 4)")

    def test_nested_str(self):
        exp = Raise(Raise(Const(4), Const(5)), Const(3))
        self.assertEqual(str(exp), "((4 ^ 5) ^ 3)")

    def test_repr_simple(self):
        exp = Raise(Const(12), Const(13))
        self.assertEqual(repr(exp), "Raise(Const(12), Const(13))")

    def test_repr_nested(self):
        exp = Raise(Const(7), Raise(Const(4), Const(2)))
        self.assertEqual(repr(exp),
                         "Raise(Const(7), Raise(Const(4), Const(2)))")

    def test_simple(self):
        exp = Raise(Const(4), Const(8))
        self.assertEqual(exp.eval(), Const(65536))

    def test_nested(self):
        exp = Raise(Const(7), Raise(Const(2), Const(3)))
        self.assertEqual(exp.eval(), Const(5764801))


class TestRoot(unittest.TestCase):

    def test_Root_str(self):
        exp = Root(Const(5), Const(4))
        self.assertEqual(str(exp), "(5 | 4)")

    def test_nested_str(self):
        exp = Root(Root(Const(4), Const(5)), Const(3))
        self.assertEqual(str(exp), "((4 | 5) | 3)")

    def test_repr_simple(self):
        exp = Root(Const(12), Const(13))
        self.assertEqual(repr(exp), "Root(Const(12), Const(13))")

    def test_repr_nested(self):
        exp = Root(Const(7), Root(Const(4), Const(2)))
        self.assertEqual(repr(exp),
                         "Root(Const(7), Root(Const(4), Const(2)))")

    def test_simple(self):
        exp = Root(Const(4), Const(8))
        self.assertEqual(exp.eval(), Const(1.189207115002721))

    def test_nested(self):
        exp = Root(Const(7), Root(Const(2), Const(3)))
        self.assertEqual(exp.eval(), Const(4.685487233160311))


# #
# # Tests of UnOp alone
# #


class TestUnOp(unittest.TestCase):

    def test_repr_simple(self):
        exp = Abs(Const(5))
        self.assertEqual(repr(exp), "Abs(Const(5))")
        exp = Neg(Const(6))
        self.assertEqual(repr(exp), "Neg(Const(6))")

    def test_str_simple(self):
        exp = Abs(Const(12))
        self.assertEqual(str(exp), "@ 12")
        exp = Neg(Const(13))
        self.assertEqual(str(exp), "~ 13")

    def test_abs_eval(self):
        exp = Minus(Const(3), Const(5))
        self.assertEqual(exp.eval(), Const(-2))
        exp = Abs(exp)
        self.assertEqual(exp.eval(), Const(2))

    def test_neg_eval(self):
        exp = Minus(Const(12), Const(8))
        self.assertEqual(exp.eval(), Const(4))
        exp = Neg(exp)
        self.assertEqual(exp.eval(), Const(-4))


class TestEquals(unittest.TestCase):

    def test_assign_left(self):
        v = Var("v")
        w = Var("w")
        exp = Equals(v, Const(5))
        self.assertEqual(exp.eval(), Const(5))
        self.assertEqual(v.eval(), Const(5))
        exp = Equals(w, v)
        self.assertEqual(exp.eval(), Const(5))
        self.assertEqual(w.eval(), Const(5))

    def test_assign_right(self):
        v = Var("v")
        w = Var("w")
        exp = Equals(Const(5), v)
        self.assertEqual(exp.eval(), Const(5))
        self.assertEqual(v.eval(), Const(5))
        exp = Equals(w, v)
        self.assertEqual(exp.eval(), Const(5))
        self.assertEqual(w.eval(), Const(5))


class TestReverse(unittest.TestCase):

    def test_plus_left(self):
        exp = Equals(Plus(Var("v"), Const(2)), Const(5))
        self.assertEquals(exp.eval(), Const(3))

    def test_plus_right(self):
        exp = Equals(Plus(Const(2), Var("v")), Const(5))
        self.assertEquals(exp.eval(), Const(3))

    def test_minus_left(self):
        exp = Equals(Minus(Var("v"), Const(2)), Const(5))
        self.assertEquals(exp.eval(), Const(7))

    def test_minus_right(self):
        exp = Equals(Minus(Const(2), Var("v")), Const(5))
        self.assertEquals(exp.eval(), Const(-3))

    def test_times_left(self):
        exp = Equals(Times(Var("v"), Const(2)), Const(5))
        self.assertEquals(exp.eval(), Const(2.5))

    def test_times_right(self):
        exp = Equals(Times(Const(2), Var("v")), Const(5))
        self.assertEquals(exp.eval(), Const(2.5))

    def test_div_left(self):
        exp = Equals(Div(Var("v"), Const(2)), Const(5))
        self.assertEquals(exp.eval(), Const(10))

    def test_div_right(self):
        exp = Equals(Div(Const(2), Var("v")), Const(5))
        self.assertEquals(exp.eval(), Const(0.4))

    def test_raise_left(self):
        exp = Equals(Raise(Var("v"), Const(2)), Const(5))
        self.assertEquals(exp.eval(), Const(2.23606797749979))

    # TODO : implement solving: (int ^ x) = int
    # def test_raise_right(self):
    #     exp = Equals(Raise(Const(2), Var("v")), Const(5))
    #     self.assertEquals(exp.eval(), Const(0.4))

    def test_root_left(self):
        exp = Equals(Root(Var("v"), Const(2)), Const(5))
        self.assertEquals(exp.eval(), Const(25))

    # TODO : implement solving: (int | x) = int
    # def test_root_right(self):
    #     exp = Equals(Root(Const(2), Var("v")), Const(5))
    #     self.assertEquals(exp.eval(), Const(0.4))


class TestSolve(unittest.TestCase):

    def test_solve_easy_right(self):
        v = Var("v")
        exp = Equals(v, Plus(Const(5), Const(2)))
        self.assertEquals(exp.eval(), Const(7))

    def test_solve_easy_left(self):
        v = Var("v")
        exp = Equals(Plus(Const(5), Const(2)), v)
        self.assertEquals(exp.eval(), Const(7))

    def test_solve_hard_left(self):
        v = Var("v")
        exp = Equals(Plus(v, Const(3)), Minus(Const(9), Const(4)))
        self.assertEquals(exp.eval(), Const(2))

    def test_solve_hard_right(self):
        v = Var("v")
        exp = Equals(Plus(Const(9), Const(3)), Minus(v, Const(4)))
        self.assertEquals(exp.eval(), Const(16))


if __name__ == "__main__":
    unittest.main()
