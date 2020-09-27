def le(num):
    lenght = 0
    while num > 0:
        num //= 10
        lenght += 1
    return lenght


def squareSequenceDigit(n):
    main_len = 0
    num = 0
    while main_len < n:
        num += 1
        main_len += le(num * num)
    power = 10**(main_len - n)
    second_try = (num * num) // power % 10
    return second_try


if __name__ == "__main__":
    assert squareSequenceDigit(1) == 1, " "
    assert squareSequenceDigit(2) == 4, " "
    assert squareSequenceDigit(7) == 5, " "
    assert squareSequenceDigit(12) == 6, " "
    assert squareSequenceDigit(17) == 0, " "
    assert squareSequenceDigit(27) == 9, " "