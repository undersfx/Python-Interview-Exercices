"""
Given a valid (IPv4) IP address, return a Defanged version of that IP address.

A Defanged IP address replaces every period "." with "[.]".

Constraints:
The given address is a valid IPv4 address.

Tests:
>>> address = '1.1.1.1'
>>> defang_IP_addr(address)
'1[.]1[.]1[.]1'

>>> address = '255.100.50.0'
>>> defang_IP_addr(address)
'255[.]100[.]50[.]0'
"""

def defang_IP_addr(address: str) -> str:
    return address.replace('.', '[.]')


def defang_IP_addr_no_replace(address: str) -> str:
    replaced = ''
    for char in address:
        if char == '.':
            replaced += '[.]'
        else:
            replaced += char
    return replaced
