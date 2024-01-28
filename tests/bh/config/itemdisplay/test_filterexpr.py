"""
``tests.bh.config.itemdisplay.test_filterexpr``
===============================================

This module contains test code for :py:mod:`d2lfg.bh.config.itemdisplay.filterexpr`.
"""

from typing import Sequence

import pytest

from d2lfg.bh.config.itemdisplay.filterexpr import (
    bh_and,
    bh_not,
    bh_or,
    BHCompoundFilterExpression,
    BHFilterExpression,
    BHFilterExpressionLiteral as L,
    BHFilterOperator,
    BHFilterOperators,
)
from d2lfg.error import InvalidStringConversionError, TooManyOperandsError


@pytest.fixture
def axe() -> L:
    """
    Returns an "axe"
    :py:class:`~d2lfg.bh.config.itemdisplay.filterexpr.BHFilterExpressionLiteral`.
    """
    return L("axe")


@pytest.fixture
def lvlreq() -> L:
    """
    Returns a "LVLREQ"
    :py:class:`~d2lfg.bh.config.itemdisplay.filterexpr.BHFilterExpressionLiteral`.
    """
    return L("LVLREQ")


@pytest.fixture
def cres() -> L:
    """
    Returns a "CRES" (cold resistance)
    :py:class:`~d2lfg.bh.config.itemdisplay.filterexpr.BHFilterExpressionLiteral`.
    """
    return L("CRES")


@pytest.fixture
def fres() -> L:
    """
    Returns a "FRES" (fire resistance)
    :py:class:`~d2lfg.bh.config.itemdisplay.filterexpr.BHFilterExpressionLiteral`.
    """
    return L("FRES")


class TestBHLogicFunctions:
    """
    Tests py:func:`~d2lfg.bh.config.itemdisplay.filterexpr.bh_and`,
    :py:func:`~d2lfg.bh.config.itemdisplay.filterexpr.bh_not`, and
    :py:func:`~d2lfg.bh.config.itemdisplay.filterexpr.bh_or`.
    """

    def test_bh_and_correct_expression(
        self,
        axe: BHFilterExpression,
        cres: BHFilterExpression,
        fres: BHFilterExpression,
    ) -> None:
        """
        Tests that py:func:`~d2lfg.bh.config.itemdisplay.filterexpr.bh_and`
        produces the expected expression.
        """
        e = bh_and(axe, cres.gt(10), fres.gt(15))

        assert e.bhexpr() == "axe CRES>10 FRES>15"

    def test_bh_not_correct_expression(
        self,
        cres: BHFilterExpression,
    ) -> None:
        """
        Tests that py:func:`~d2lfg.bh.config.itemdisplay.filterexpr.bh_not`
        produces the expected expression.
        """
        e = bh_not(cres.gt(10))

        assert e.bhexpr() == "!(CRES>10)"

    def test_bh_or_correct_expression(
        self,
        axe: BHFilterExpression,
        cres: BHFilterExpression,
        fres: BHFilterExpression,
    ) -> None:
        """
        Tests that py:func:`~d2lfg.bh.config.itemdisplay.filterexpr.bh_or`
        produces the expected expression.
        """
        e = bh_or(axe, cres.gt(10), fres.gt(15))

        assert e.bhexpr() == "axe OR CRES>10 OR FRES>15"


class TestBHFilterExpression:
    """
    Tests :py:class:`~d2lfg.bh.config.itemdisplay.filterexpr.BHFilterExpression`.
    """

    def test_eq_same_is_equal(self, cres: BHFilterExpression) -> None:
        """
        Verifies that a filter expression is equivalent to itself.
        """
        assert cres == cres

    def test_eq_similar_is_equal(self, cres: BHFilterExpression) -> None:
        """
        Verifies that a filter expression is equivalent to another expression
        which produces the same expression string.
        """
        similar_expr = L(cres.bhexpr())

        assert cres == similar_expr

    def test_eq_different_is_not_equal(
        self,
        cres: BHFilterExpression,
        fres: BHFilterExpression,
    ) -> None:
        """
        Verifies that a filter expression is not equivalent to an expression
        which is different.
        """
        assert cres != fres

    def test_eq_different_object_is_not_equal(self, cres: BHFilterExpression) -> None:
        """
        Verifies that a filter expression is not equivalent to a different
        type of object.
        """
        assert cres != cres.bhexpr()

    def test_add(self, cres: BHFilterExpression, fres: BHFilterExpression) -> None:
        """
        Verifies that filter expressions can be added.
        """
        e = cres + fres

        assert isinstance(e, BHCompoundFilterExpression)
        assert e.operator == BHFilterOperators.ADD
        assert tuple(e.operands) == tuple((cres, fres))

    def test_between(self, lvlreq: BHFilterExpression) -> None:
        """
        Verifies that filter expression "between" comparisons can be made.
        """
        e = lvlreq.between(60, 85)

        assert isinstance(e, BHCompoundFilterExpression)
        assert e.operator == BHFilterOperators.BTWN
        assert e.bhexpr() == "LVLREQ~60-85"

    def test_eq(self, lvlreq: BHFilterExpression) -> None:
        """
        Verifies that filter expression equality comparisons can be made.
        """
        e = lvlreq.eq(85)

        assert e.bhexpr() == "LVLREQ=85"

    def test_gt(self, lvlreq: BHFilterExpression) -> None:
        """
        Verifies that filter expression "greater than" comparisons can be made.
        """
        e = lvlreq.gt(85)

        assert isinstance(e, BHFilterExpression)
        assert e.bhexpr() == "LVLREQ>85"

    def test_lt(self, lvlreq: BHFilterExpression) -> None:
        """
        Verifies that filter expression "less than" comparisons can be made.
        """
        e = lvlreq.lt(85)

        assert isinstance(e, BHFilterExpression)
        assert e.bhexpr() == "LVLREQ<85"

    def test_str_raises_exception(self, axe: BHFilterExpression) -> None:
        """
        Verifies that converting
        :py:class:`~d2lfg.bh.config.itemdisplay.filterexpr.BHFilterExpression` objects
        to a string raises an exception.

        This prevents objects from being accidentally used in output strings where
        such use is invalid.
        """
        with pytest.raises(InvalidStringConversionError):
            str(axe)

    def test_string_interpolation_raises_exception(
        self, axe: BHFilterExpression
    ) -> None:
        """
        Verifies that interpolation of
        :py:class:`~d2lfg.bh.config.itemdisplay.filterexpr.BHFilterExpression` objects
        in a string raises an exception.

        This prevents objects from being accidentally used in output strings where
        such use is invalid.
        """
        with pytest.raises(InvalidStringConversionError):
            f"{axe}%NL%%CONTINUE%"


class TestBHFilterExpressionLiteral:
    """
    Tests :py:class:`~d2lfg.bh.config.itemdisplay.filterexpr.BHFilterExpressionLiteral`.
    """

    @pytest.mark.parametrize(
        "literal, expected",
        [
            (L("~1-4"), "~1-4"),
            (L("lvlreq"), "lvlreq"),
        ],
    )
    def test_bhexpr(self, literal: L, expected: str) -> None:
        """
        Verifies that
        :py:meth:`~d2lfg.bh.config.itemdisplay.filterexpr.BHFilterExpressionLiteral.bhexpr`
        produces the correct string.
        """

        assert literal.bhexpr() == expected


class TestBHCompoundFilterExpression:
    """
    Tests :py:class:`~d2lfg.bh.config.itemdisplay.filterexpr.BHCompoundFilterExpression`.
    """

    def test_init_with_too_many_operands_raises_error(self) -> None:
        """
        Verifies that initializing a
        :py:class:`~d2lfg.bh.config.itemdisplay.filterexpr.BHCompoundFilterExpression`
        with too many operands raises a :py:class:`~d2lfg.error.TooManyOperandsError`.
        """
        with pytest.raises(TooManyOperandsError):
            BHCompoundFilterExpression(
                BHFilterOperators.NOT,
                L("lvlreq=85"),
                L("axe"),
            )

    @pytest.mark.parametrize(
        "expected_operator",
        [
            BHFilterOperators.NOT,
            BHFilterOperators.OR,
        ],
    )
    def test_operator_property_returns_operator(
        self, expected_operator: BHFilterOperator
    ) -> None:
        """
        Verifies that the operator property returns the appropriate
        :py:class:`~d2lfg.bh.config.itemdisplay.filterexpr.BHFilterOperator`.
        """
        e = BHCompoundFilterExpression(expected_operator, L("test"))

        assert e.operator == expected_operator

    @pytest.mark.parametrize(
        "expected_operands",
        [
            (L("test1"), L("test2")),
            (L("test3"), L("test4")),
        ],
    )
    def test_operand_property_returns_operands(
        self, expected_operands: Sequence[BHFilterExpression]
    ) -> None:
        """
        Verifies that the operator property returns the appropriate
        :py:class:`~d2lfg.bh.config.itemdisplay.filterexpr.BHFilterOperator`.
        """
        e = BHCompoundFilterExpression(BHFilterOperators.OR, *expected_operands)

        assert expected_operands == e.operands

    def test_bhexpr_always_returns_same_value(self) -> None:
        """
        Verifies that
        :py:meth:`~d2lfg.bh.config.itemdisplay.filterexpr.BHCompoundFilterExpression.bhexpr`
        always returns the same value.
        """
        e = BHCompoundFilterExpression(BHFilterOperators.AND, L("axe"))

        assert e.bhexpr() == e.bhexpr()

    def test_unary_operand(self) -> None:
        """
        Verifies that
        :py:meth:`~d2lfg.bh.config.itemdisplay.filterexpr.BHCompoundFilterExpression.bhexpr`
        produces a string of the form "{operator}{operand}".
        """
        e = BHCompoundFilterExpression(BHFilterOperators.NOT, L("axe"))

        assert e.bhexpr() == "!axe"

    def test_expr_requires_parens_non_compound_inner(
        self, axe: BHFilterExpression
    ) -> None:
        """
        Verifies that
        :py:meth:`~d2lfg.bh.config.itemdisplay.filterexpr.BHCompoundFilterExpression.expr_requires_parens`
        returns ``False`` if the inner expression is not a compound expression.
        """
        e_and = BHCompoundFilterExpression(BHFilterOperators.AND, axe)

        assert not BHCompoundFilterExpression.expr_requires_parens(e_and, axe)

    def test_expr_requires_parens_logical_inverse(
        self, cres: BHFilterExpression
    ) -> None:
        """
        Verifies that
        :py:meth:`~d2lfg.bh.config.itemdisplay.filterexpr.BHCompoundFilterExpression.expr_requires_parens`
        returns ``True`` if the outer expression will perform a logical not and
        the inner expression is compound.
        """
        e_gt = cres.gt(10)
        e_not = bh_not(e_gt)

        assert BHCompoundFilterExpression.expr_requires_parens(e_not, e_gt)

    def test_expr_requires_parens_gt_and(
        self,
        cres: BHFilterExpression,
    ) -> None:
        """
        Verifies that
        :py:meth:`~d2lfg.bh.config.itemdisplay.filterexpr.BHCompoundFilterExpression.expr_requires_parens`
        returns ``False`` if the outer expression is a logical and and
        the inner expression is a comparison.
        """
        e_gt = cres.gt(10)
        e_and = bh_and(e_gt, e_gt)

        assert not BHCompoundFilterExpression.expr_requires_parens(e_and, e_gt)

    def test_expr_requires_parens_and_joining_or(
        self,
        axe: BHFilterExpression,
        cres: BHFilterExpression,
        fres: BHFilterExpression,
    ) -> None:
        """
        Verifies that
        :py:meth:`~d2lfg.bh.config.itemdisplay.filterexpr.BHCompoundFilterExpression.expr_requires_parens`
        returns ``True`` if the outer expression is a logical and and
        the inner expression is a logical or.
        """
        e_or = bh_or(axe, cres.gt(10))
        e_and = bh_and(fres.gt(10), e_or)

        assert BHCompoundFilterExpression.expr_requires_parens(e_and, e_or)


class TestRealWorldFilterExpressions:
    """
    Contains test cases for various real-world, complex filters.
    """

    def test_realworld_01(self) -> None:
        """
        Testcase 01 for real-world filter expressions.

        https://github.com/KassahiPD2/Kassahi/blob/1e547c28c06fd17580720c44de6191e225f81265/Regular.filter#L2100
        """
        e = bh_and(
            L("FILTLVL").lt(2), L("NMAG"), L("SOCK").eq(4), L("SWORD"), bh_not(L("RW"))
        )

        assert e.bhexpr() == "FILTLVL<2 NMAG SOCK=4 SWORD !RW"

    def test_realworld_02(self) -> None:
        """
        Testcase 02 for real-world filter expressions.

        https://github.com/KassahiPD2/Kassahi/blob/1e547c28c06fd17580720c44de6191e225f81265/Regular.filter#L2158
        """
        e = bh_and(
            L("NMAG"),
            bh_not(L("INF")),
            bh_not(L("SUP")),
            bh_not(L("RW")),
            L("SOCK").eq(0),
            bh_not(L("THROWING")),
            bh_or(
                L("HELM"),
                L("CHEST"),
                L("SHIELD"),
                L("CIRC"),
                L("WEAPON"),
            ),
            bh_or(
                L("9la"),
                L("7la"),
            ),
        )
        expected = "NMAG !INF !SUP !RW SOCK=0 !THROWING (HELM OR CHEST OR SHIELD OR CIRC OR WEAPON) (9la OR 7la)"

        assert e.bhexpr() == expected
