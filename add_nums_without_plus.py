# Add two numbers without using the arithmetic operator +


def add_no_op(a, b):
    if not a or not b:
        raise AttributeError("Please pass valid integers for a and b")

    if not isinstance(a, int) or not isinstance(b, int):
        raise AttributeError("Both numbers must be valid integers")

    while b != 0:
        sum = a ^ b
        carry = (a & b) << 1
        a = sum
        b = carry

    return a

if __name__ == "__main__":
    print add_no_op(1, 2)
