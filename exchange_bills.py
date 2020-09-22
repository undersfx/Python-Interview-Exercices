"""
Implement a function for a vending machine. Receive the price and the amount of money.

The function need to return the exchange limited with four kinds of bills: 1, 5, 10, 20.

Calculate the exchange with the usage of fewest bills possible.
"""


def naive_exchange(price, amount): # Do not scale well
    """
    Doctests:
    >>> naive_exchange(10, 30)
    {20: 1, 10: 0, 5: 0, 1: 0}

    >>> naive_exchange(10, 40)
    {20: 1, 10: 1, 5: 0, 1: 0}

    >>> naive_exchange(10, 45)
    {20: 1, 10: 1, 5: 1, 1: 0}

    >>> naive_exchange(10, 46)
    {20: 1, 10: 1, 5: 1, 1: 1}

    >>> naive_exchange(10, 56)
    {20: 2, 10: 0, 5: 1, 1: 1}
    """
    diff = amount - price

    bill_20 = diff // 20
    diff = diff - (bill_20 * 20)

    bill_10 = diff // 10
    diff = diff - (bill_10 * 10)

    bill_5 = diff // 5
    diff = diff - (bill_5 * 5)

    return {20:bill_20, 10:bill_10, 5:bill_5, 1:diff}


def exchange_with_zeros(price, amount):
    """
    Doctests:
    >>> exchange_with_zeros(10, 30)
    {20: 1, 10: 0, 5: 0, 1: 0}

    >>> exchange_with_zeros(10, 40)
    {20: 1, 10: 1, 5: 0, 1: 0}

    >>> exchange_with_zeros(10, 45)
    {20: 1, 10: 1, 5: 1, 1: 0}

    >>> exchange_with_zeros(10, 46)
    {20: 1, 10: 1, 5: 1, 1: 1}

    >>> exchange_with_zeros(10, 56)
    {20: 2, 10: 0, 5: 1, 1: 1}
    """
    BILLS = [20, 10, 5, 1]
    difference = amount - price
    exchange = {}

    for bill in BILLS:
        exchange[bill] = difference // bill
        difference %= bill

    return exchange


def exchange_no_zeros(price, amount):
    """
    Doctests:
    >>> exchange_no_zeros(10, 30)
    {20: 1}

    >>> exchange_no_zeros(10, 40)
    {20: 1, 10: 1}

    >>> exchange_no_zeros(10, 45)
    {20: 1, 10: 1, 5: 1}

    >>> exchange_no_zeros(10, 46)
    {20: 1, 10: 1, 5: 1, 1: 1}

    >>> exchange_no_zeros(10, 56)
    {20: 2, 5: 1, 1: 1}
    """
    BILLS = [20, 10, 5, 1]
    difference = amount - price
    exchange = {}

    for bill in BILLS:
        if difference // bill:
            exchange[bill] = difference // bill
            difference %= bill

    return exchange
