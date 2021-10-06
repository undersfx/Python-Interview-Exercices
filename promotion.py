'''
    Given a list "code" (code: List[List]) where code elements represents
    group of strings (code[n]: List[str]) and a list "cart" (cart: List[str]).

    Write a function that returns 1 if all groups of "code" are inside "cart"
    maintaning its order, otherwise return 0.

    Note:
    - "code" group items can have the string "anything" that can match to any string in cart.
    - "anything" needs to match to any string, but its position cannot be skipped.
    - if "code" are empty, the return should be 1.
'''

def calculate_winner(code, cart):
    """
        >>> code =  [["apple", "apple"], ["banana", "anything", "banana"]]
        >>> cart = ["orange", "apple", "apple", "banana", "orange", "banana"]
        >>> calculate_winner(code, cart)
        1

        >>> code =  [["apple", "apple"], ["banana", "anything", "banana"]]
        >>> cart = ["banana", "orange", "banana", "apple", "apple"]
        >>> calculate_winner(code, cart)
        0

        >>> code =  [["apple", "apple"], ["apple", "apple", "banana"]]
        >>> cart =  ["apple", "apple", "apple", "banana"]
        >>> calculate_winner(code, cart)
        0

        >>> code =  []
        >>> cart = ["orange", "apple", "apple", "banana", "orange", "banana"]
        >>> calculate_winner(code, cart)
        1
    """
    code_index = 0
    cart_index = 0

    while code_index < len(code) and cart_index < len(cart):
        group_index = 0

        while group_index < len(code[code_index]) and cart_index < len(cart):
            if code[code_index][group_index] == cart[cart_index] or code[code_index][group_index] == 'anything':
                group_index += 1
                cart_index += 1
            else:
                group_index = 0
                cart_index += 1
                if cart_index >= len(cart):
                    return 0

        code_index += 1

    if code_index >= len(code):
        return 1
    return 0

if __name__ == "__main__":
    code =  [["apple", "apple"], ["banana", "anything", "banana"]]
    cart = ["orange", "apple", "apple", "banana", "orange", "banana"]
    print(f'code: {code} \ncart: {cart} \nresult: {calculate_winner(code, cart)}\n')

    code =  [["apple", "apple"], ["banana", "anything", "banana"]]
    cart = ["banana", "orange", "banana", "apple", "apple"]
    print(f'code: {code} \ncart: {cart} \nresult: {calculate_winner(code, cart)}\n')

    code =  [["apple", "apple"], ["apple", "apple", "banana"]]
    cart =  ["apple", "apple", "apple", "banana"]
    print(f'code: {code} \ncart: {cart} \nresult: {calculate_winner(code, cart)}\n')

    code =  []
    cart = ["orange", "apple", "apple", "banana", "orange", "banana"]
    print(f'code: {code} \ncart: {cart} \nresult: {calculate_winner(code, cart)}\n')