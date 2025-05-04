import pytest  # noqa: F401
from rook.bitboard import Bitboard, File, Rank


def test_bitboard_get_position_mask():
    bitboard = Bitboard()

    assert (
        bitboard.get_position_mask(Rank.A, File.EIGHT)
        == 0b_10000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000
    )
