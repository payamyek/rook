import pytest  # type: ignore # noqa: F401
from rook.chess_board import File, Rank, ChessPiece, ChessBoard


def test_bitboard_get_position_mask():
    chess_board = ChessBoard()

    assert (
        chess_board.get_position_mask(Rank.A, File.EIGHT)
        == 0b_10000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000
    )

    assert (
        chess_board.get_position_mask(Rank.H, File.EIGHT)
        == 0b_00000001_00000000_00000000_00000000_00000000_00000000_00000000_00000000
    )

    assert (
        chess_board.get_position_mask(Rank.A, File.ONE)
        == 0b_00000000_00000000_00000000_00000000_00000000_00000000_00000000_10000000
    )

    assert (
        chess_board.get_position_mask(Rank.H, File.ONE)
        == 0b_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000001
    )


def test_bitboard_get_piece_at_position():
    chess_board = ChessBoard()

    assert chess_board.get_piece_at_position(Rank.A, File.EIGHT) == ChessPiece(
        "rook", colour="black"
    )
    assert chess_board.get_piece_at_position(Rank.B, File.EIGHT) == ChessPiece(
        "knight", colour="black"
    )
    assert chess_board.get_piece_at_position(Rank.C, File.EIGHT) == ChessPiece(
        "bishop", colour="black"
    )
    assert chess_board.get_piece_at_position(Rank.D, File.EIGHT) == ChessPiece(
        "queen", colour="black"
    )
    assert chess_board.get_piece_at_position(Rank.E, File.EIGHT) == ChessPiece(
        "king", colour="black"
    )
    assert chess_board.get_piece_at_position(Rank.F, File.EIGHT) == ChessPiece(
        "bishop", colour="black"
    )
    assert chess_board.get_piece_at_position(Rank.G, File.EIGHT) == ChessPiece(
        "knight", colour="black"
    )
    assert chess_board.get_piece_at_position(Rank.H, File.EIGHT) == ChessPiece(
        "rook", colour="black"
    )
    assert chess_board.get_piece_at_position(Rank.A, File.SEVEN) == ChessPiece(
        "pawn", colour="black"
    )

    assert chess_board.get_piece_at_position(Rank.A, File.ONE) == ChessPiece(
        "rook", colour="white"
    )
    assert chess_board.get_piece_at_position(Rank.B, File.ONE) == ChessPiece(
        "knight", colour="white"
    )
    assert chess_board.get_piece_at_position(Rank.C, File.ONE) == ChessPiece(
        "bishop", colour="white"
    )
    assert chess_board.get_piece_at_position(Rank.D, File.ONE) == ChessPiece(
        "queen", colour="white"
    )
    assert chess_board.get_piece_at_position(Rank.E, File.ONE) == ChessPiece(
        "king", colour="white"
    )
    assert chess_board.get_piece_at_position(Rank.F, File.ONE) == ChessPiece(
        "bishop", colour="white"
    )
    assert chess_board.get_piece_at_position(Rank.G, File.ONE) == ChessPiece(
        "knight", colour="white"
    )
    assert chess_board.get_piece_at_position(Rank.H, File.ONE) == ChessPiece(
        "rook", colour="white"
    )
    assert chess_board.get_piece_at_position(Rank.A, File.TWO) == ChessPiece(
        "pawn", colour="white"
    )

    assert chess_board.get_piece_at_position(Rank.A, File.THREE) is None
