import pytest  # type: ignore # noqa: F401
from rook.chess_board import File, Rank, ChessPiece, ChessBoard


def test_bitboard_get_position_mask():
    chess_board = ChessBoard()

    assert (
        chess_board.get_position_mask(Rank.EIGHT, File.A)
        == 0b_10000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000
    )

    assert (
        chess_board.get_position_mask(Rank.EIGHT, File.H)
        == 0b_00000001_00000000_00000000_00000000_00000000_00000000_00000000_00000000
    )

    assert (
        chess_board.get_position_mask(Rank.ONE, File.A)
        == 0b_00000000_00000000_00000000_00000000_00000000_00000000_00000000_10000000
    )

    assert (
        chess_board.get_position_mask(Rank.ONE, File.H)
        == 0b_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000001
    )


def test_bitboard_get_piece_at_position():
    chess_board = ChessBoard()

    assert chess_board.get_piece_at_position(Rank.EIGHT, File.A) == ChessPiece(
        "rook", colour="black"
    )
    assert chess_board.get_piece_at_position(Rank.EIGHT, File.B) == ChessPiece(
        "knight", colour="black"
    )
    assert chess_board.get_piece_at_position(Rank.EIGHT, File.C) == ChessPiece(
        "bishop", colour="black"
    )
    assert chess_board.get_piece_at_position(Rank.EIGHT, File.D) == ChessPiece(
        "queen", colour="black"
    )
    assert chess_board.get_piece_at_position(Rank.EIGHT, File.E) == ChessPiece(
        "king", colour="black"
    )
    assert chess_board.get_piece_at_position(Rank.EIGHT, File.F) == ChessPiece(
        "bishop", colour="black"
    )
    assert chess_board.get_piece_at_position(Rank.EIGHT, File.G) == ChessPiece(
        "knight", colour="black"
    )
    assert chess_board.get_piece_at_position(Rank.EIGHT, File.H) == ChessPiece(
        "rook", colour="black"
    )
    assert chess_board.get_piece_at_position(Rank.SEVEN, File.A) == ChessPiece(
        "pawn", colour="black"
    )

    assert chess_board.get_piece_at_position(Rank.ONE, File.A) == ChessPiece(
        "rook", colour="white"
    )
    assert chess_board.get_piece_at_position(Rank.ONE, File.B) == ChessPiece(
        "knight", colour="white"
    )
    assert chess_board.get_piece_at_position(Rank.ONE, File.C) == ChessPiece(
        "bishop", colour="white"
    )
    assert chess_board.get_piece_at_position(Rank.ONE, File.D) == ChessPiece(
        "queen", colour="white"
    )
    assert chess_board.get_piece_at_position(Rank.ONE, File.E) == ChessPiece(
        "king", colour="white"
    )
    assert chess_board.get_piece_at_position(Rank.ONE, File.F) == ChessPiece(
        "bishop", colour="white"
    )
    assert chess_board.get_piece_at_position(Rank.ONE, File.G) == ChessPiece(
        "knight", colour="white"
    )
    assert chess_board.get_piece_at_position(Rank.ONE, File.H) == ChessPiece(
        "rook", colour="white"
    )
    assert chess_board.get_piece_at_position(Rank.TWO, File.A) == ChessPiece(
        "pawn", colour="white"
    )

    assert chess_board.get_piece_at_position(Rank.THREE, File.A) is None
