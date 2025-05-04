import pytest  # type: ignore # noqa: F401
from rook.bitboard import Bitboard, File, Rank, ChessPiece


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


def test_bitboard_get_piece_at_position():
    bitboard = Bitboard()

    assert bitboard.get_piece_at_position(Rank.A, File.EIGHT) == ChessPiece.BLACK_ROOK
    assert bitboard.get_piece_at_position(Rank.B, File.EIGHT) == ChessPiece.BLACK_KNIGHT
    assert bitboard.get_piece_at_position(Rank.C, File.EIGHT) == ChessPiece.BLACK_BISHOP
    assert bitboard.get_piece_at_position(Rank.D, File.EIGHT) == ChessPiece.BLACK_QUEEN
    assert bitboard.get_piece_at_position(Rank.E, File.EIGHT) == ChessPiece.BLACK_KING
    assert bitboard.get_piece_at_position(Rank.F, File.EIGHT) == ChessPiece.BLACK_BISHOP
    assert bitboard.get_piece_at_position(Rank.G, File.EIGHT) == ChessPiece.BLACK_KNIGHT
    assert bitboard.get_piece_at_position(Rank.H, File.EIGHT) == ChessPiece.BLACK_ROOK
    assert bitboard.get_piece_at_position(Rank.A, File.SEVEN) == ChessPiece.BLACK_PAWN

    assert bitboard.get_piece_at_position(Rank.A, File.ONE) == ChessPiece.WHITE_ROOK
    assert bitboard.get_piece_at_position(Rank.B, File.ONE) == ChessPiece.WHITE_KNIGHT
    assert bitboard.get_piece_at_position(Rank.C, File.ONE) == ChessPiece.WHITE_BISHOP
    assert bitboard.get_piece_at_position(Rank.D, File.ONE) == ChessPiece.WHITE_QUEEN
    assert bitboard.get_piece_at_position(Rank.E, File.ONE) == ChessPiece.WHITE_KING
    assert bitboard.get_piece_at_position(Rank.F, File.ONE) == ChessPiece.WHITE_BISHOP
    assert bitboard.get_piece_at_position(Rank.G, File.ONE) == ChessPiece.WHITE_KNIGHT
    assert bitboard.get_piece_at_position(Rank.H, File.ONE) == ChessPiece.WHITE_ROOK
    assert bitboard.get_piece_at_position(Rank.A, File.TWO) == ChessPiece.WHITE_PAWN

    assert bitboard.get_piece_at_position(Rank.A, File.THREE) is None
