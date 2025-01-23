import pytest

from currency import Bank, Money, Pair, Sum


@pytest.fixture
def bank() -> Bank:
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    return bank


def test_equality() -> None:
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.frank(3) != Money.frank(5)
    assert Money.frank(5) != Money.dollar(5)


def test_money_times() -> None:
    assert Money.frank(5).times(2) == Money.frank(10)
    assert Money.dollar(5).times(3) == Money.dollar(15)


def test_currency() -> None:
    """No privat or protected prop in Python"""
    assert Money.frank(1).currency == "CHF"
    assert Money.dollar(1).currency == "USD"


def test_simple_add(bank: Bank) -> None:
    reducer = bank.reduce(Money.dollar(5) + Money.dollar(5), "USD")
    assert Money.dollar(10) == reducer


def test_reduce_money(bank: Bank) -> None:
    reduced = bank.reduce(Money.dollar(1), "USD")
    assert reduced == Money.dollar(1)


def test_add_rate_to_bank(bank: Bank) -> None:
    assert bank.rates.get(Pair("CHF", "USD")) == 2


def test_reduce_differnt_currency(bank: Bank) -> None:
    reduced = bank.reduce(Money.frank(2), "USD")
    assert reduced == Money.dollar(1)


def test_mixed_currency_add(bank: Bank) -> None:
    reduced = bank.reduce(Money.dollar(5) + Money.frank(10), "USD")
    assert reduced == Money.dollar(10)


def test_add_expressions(bank: Bank) -> None:
    sum = Sum(Money.dollar(5), Money.frank(10))
    reduced = bank.reduce(sum + Money.dollar(5), "USD")
    assert reduced == Money.dollar(15)
    reduced = bank.reduce(sum + Sum(Money.dollar(5), Money.frank(10)), "USD")
    assert reduced == Money.dollar(20)


def test_add_return_money(bank: Bank) -> None:
    sum = Sum(Money.dollar(5), Money.frank(10))
    reduced = bank.reduce(sum + Money.dollar(5), "USD")
    assert isinstance(reduced, Money)


def test_sum_times(bank: Bank) -> None:
    sum = Sum(Money.dollar(5), Money.frank(10)).times(2)
    reduced = bank.reduce(sum, "USD")
    assert reduced == Money.dollar(20)
