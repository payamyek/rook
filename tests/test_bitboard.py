import pytest  # noqa: F401
from rook.bitboard import Bitboard, File, Rank


def test_bitboard_get_position_mask():
    bitboard = Bitboard()

    assert (
        bitboard.get_position_mask(Rank.A, File.EIGHT)
        == 0b_10000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000
    )

    assert (
        bitboard.get_position_mask(Rank.H, File.EIGHT)
        == 0b_00000001_00000000_00000000_00000000_00000000_00000000_00000000_00000000
    )

    assert (
        bitboard.get_position_mask(Rank.A, File.ONE)
        == 0b_00000000_00000000_00000000_00000000_00000000_00000000_00000000_10000000
    )

    assert (
        bitboard.get_position_mask(Rank.H, File.ONE)
        == 0b_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000001
    )
