#!/usr/bin/env python3

"""
DESCRIÇÂO DO DESAFIO

Imagine uma lista de compras. Ela possui:
    - Itens
    - Quantidade de cada item
    - Preço por unidade/peso/pacote de cada item

Desenvolva uma função (ou método) que irá receber uma lista de compras (como a
detalhada acima) e uma lista de e-mails. Aqui, cada e-mail representa uma pessoa.

A função deve:
    - Calcular a soma dos valores, ou seja, multiplicar o preço de cada item por
    sua quantidade e somar todos os itens

    - Dividir o valor de forma igual entre a quantidade de e-mails

    - Retornar um mapa/dicionário onde a chave será o e-mail e o valor será quanto
    ele deve pagar nessa conta

Importante:
    - Quando fizer a divisão, é importante que não falte nenhum centavo! Cuidado
    quando tiver, por exemplo, um valor total de R$ 1,00 para ser dividido entre
    3 e-mails. Isso daria uma dízima infinita. No entanto, o correto aqui é que
    duas pessoas fiquem com o valor 0,33 e a terceira fique com 0,34.

    - Para facilitar e como boa prática, não trabalhe com valores com decimais.
    Ou seja, ponto flutuante ou float. Use inteiros para representar os valores!
    Como a menor unidade na nossa moeda é o centavo, use valores inteiros em
    centavos. Assim, um real será representado por 100 (cem centavos é igual a
    um real).

    - Deixe documentado como você "testa" a solução. Por exemplo: "eu coloco o
    arquivo numa pasta/desafio e executo javac Desafio.java e depois java
    Desafio". Testes automatizados são bem vindos, mas não são necessários.
"""

from typing import List, Tuple


def calculate_bill(items:List[Tuple], emails:List[str]) -> dict:
    """
    Calculate the equal division of the bill based on a provived list of items.

    Each email will be charged (total_price / total_emails) where "total_price"
    is based on each item (amount * price)

    :items: expects a list of tuples with "name" (str), "amount" (int) and
    "price" in cents (int)
    e.g. [('Banana', 1, 100), ('Macã', 1, 200)]

    :emails: expects a list of valid e-mails (str)
    e.g. ['foo@bar.com', 'fiz@buz.com']

    :return: return a dict with the emails as keys (str) and the equal divided
    price  as value (int)
    e.g. {'foo@bar.com': 150, 'fiz@buz.com': 150}

    Doctest Example:
    >>> items = [('Banana', 1, 100), ('Macã', 1, 200)]
    >>> emails = ['foo@bar.com', 'fiz@buz.com']
    >>> calculate_bill(items, emails)
    {'foo@bar.com': 150, 'fiz@buz.com': 150}


    In case of division results in a periodic tithe, the last email will be
    chaged a aditional cent to round the total_price correctly.

    Doctest Examples:
    >>> items = [('Banana', 1, 100)]
    >>> emails = ['foo@bar.com', 'fiz@buz.com', 'bar@foo.com']
    >>> calculate_bill(items, emails)
    {'foo@bar.com': 33, 'fiz@buz.com': 33, 'bar@foo.com': 34}

    >>> items = [('Banana', 10, 100)]
    >>> emails = ['foo@bar.com', 'fiz@buz.com', 'bar@foo.com', 'foo@bar.org', 'fiz@buz.org', 'bar@foo.org']
    >>> calculate_bill(items, emails)
    {'foo@bar.com': 166, 'fiz@buz.com': 166, 'bar@foo.com': 166, 'foo@bar.org': 166, 'fiz@buz.org': 166, 'bar@foo.org': 170}


    In case the list of emails provided is blank, the return will be a empty
    dict to maintain consistency of data type in return clause.

    Doctest Examples:
    >>> items = [('Banana', 1, 100)]
    >>> emails = []
    >>> calculate_bill(items, emails)
    {}

    >>> items = []
    >>> emails = ['foo@bar.com', 'fiz@buz.com', 'bar@foo.com']
    >>> calculate_bill(items, emails)
    {}
    """

    bill = {}

    if items and emails:
        total_price = sum([item[1] * item[2] for item in items])
        total_emails = len(emails)
        divided_price = total_price / total_emails

        for email in emails:
            bill[email] = int(divided_price)
        else:
            if total_price % total_emails != 0:
                bill[email] += total_price % total_emails

    return bill
