def int_to_string(x: int) -> str:
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s = []
    while True:
        s.append(chr(ord('0') + (x % 10)))
        x //= 10
        if x == 0:
            break

    # Adds the negative sign back if is_negative
    return ('-' if is_negative else '') + ''.join(s)


# def string_to_int(s: str) -> int:

print(int_to_string(234))