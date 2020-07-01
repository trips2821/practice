import pytest


def insert(original_num, insert_num, position_start, position_end):
    mask = ((1 << position_start - position_end) - 1) << position_end
    mask = mask & original_num
    cleared_bits_num = original_num ^ mask

    shifted_insert_num = insert_num << position_end
    new_num = cleared_bits_num | shifted_insert_num
    return new_num


def test_bit_insert_over_zeros():
    m = 0b10011
    n = 0b10000000000

    r = insert(n, m, 6, 2)

    expected_result = 0b10001001100
    assert bin(r) == bin(expected_result)


def test_bit_insert_over_ones():
    m = 0b10011
    n = 0b10001101101

    r = insert(n, m, 6, 2)

    expected_result = 0b10001001101
    assert bin(r) == bin(expected_result)
