"""Arithmetic functions."""

def list_pow(a, b):
    """Raises a^b without rolling over by using a list. 
    a < 10 in this implementation."""
    result_list = list()
    result_list.append(1)
    carry = 0
    for i in xrange(b):
        for i, digit in enumerate(result_list):
            product = digit * a
            result_list[i] = (product % 10) + carry
            carry = product / 10
        if carry:
            result_list.append(carry)
            carry = 0
    return ''.join([str(i) for i in reversed(result_list)])