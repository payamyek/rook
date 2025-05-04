from dataclasses import dataclass
from enum import Enum
import math
from typing import Optional

# --------------- GLOBAL CONSTANTS ----------

BOARD_SIZE = 8


# --------------- ENUMS ----------


class Rank(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7


class File(Enum):
    ONE = 7
    TWO = 6
    THREE = 5
    FOUR = 4
    FIVE = 3
    SIX = 2
    SEVEN = 1
    EIGHT = 0


class ChessPiece(Enum):
    WHITE_PAWN = "white_pawn"
    WHITE_ROOK = "white_rook"
    WHITE_KNIGHT = "white_knight"
    WHITE_BISHOP = "white_bishop"
    WHITE_QUEEN = "white_queen"
    WHITE_KING = "white_king"
    BLACK_PAWN = "black_pawn"
    BLACK_ROOK = "black_rook"
    BLACK_KNIGHT = "black_knight"
    BLACK_BISHOP = "black_bishop"
    BLACK_QUEEN = "black_queen"
    BLACK_KING = "black_king"


# ---------------  MAPPINGS ----------

CHESS_PIECE_UNICODE_MAP = {
    ChessPiece.WHITE_PAWN: "♙",
    ChessPiece.WHITE_ROOK: "♖",
    ChessPiece.WHITE_KNIGHT: "♘",
    ChessPiece.WHITE_BISHOP: "♗",
    ChessPiece.WHITE_QUEEN: "♕",
    ChessPiece.WHITE_KING: "♔",
    ChessPiece.BLACK_PAWN: "♟",
    ChessPiece.BLACK_ROOK: "♜",
    ChessPiece.BLACK_KNIGHT: "♞",
    ChessPiece.BLACK_BISHOP: "♝",
    ChessPiece.BLACK_QUEEN: "♛",
    ChessPiece.BLACK_KING: "♚",
}


# --------------- CLASS DEFINITIONS ----------


@dataclass
class Bitboard:
    # ------------------ WHITE PIECES ------------------
    white_pawn: int = (
        0b_00000000_00000000_00000000_00000000_00000000_00000000_11111111_00000000
    )
    white_rook: int = (
        0b_00000000_00000000_00000000_00000000_00000000_00000000_00000000_10000001
    )
    white_knight: int = (
        0b_00000000_00000000_00000000_00000000_00000000_00000000_00000000_01000010
    )
    white_bishop: int = (
        0b_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00100100
    )
    white_queen: int = (
        0b_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00010000
    )
    white_king: int = (
        0b_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00001000
    )

    # ------------------ BLACK PIECES ------------------
    black_pawn: int = (
        0b_00000000_11111111_00000000_00000000_00000000_00000000_00000000_00000000
    )
    black_rook: int = (
        0b_10000001_00000000_00000000_00000000_00000000_00000000_00000000_00000000
    )
    black_knight: int = (
        0b_01000010_00000000_00000000_00000000_00000000_00000000_00000000_00000000
    )
    black_bishop: int = (
        0b_00100100_00000000_00000000_00000000_00000000_00000000_00000000_00000000
    )
    black_queen: int = (
        0b_00010000_00000000_00000000_00000000_00000000_00000000_00000000_00000000
    )
    black_king: int = (
        0b_00001000_00000000_00000000_00000000_00000000_00000000_00000000_00000000
    )

    def get_position_mask(self, rank: Rank, file: File) -> int:
        return int(math.pow(2, 63 - rank.value - file.value * BOARD_SIZE))

    def get_piece_at_position(self, rank: Rank, file: File) -> Optional[ChessPiece]:
        position_mask = self.get_position_mask(rank, file)

        for piece, bitboard in self.__dict__.items():
            if bitboard & position_mask:
                return ChessPiece(piece)
        return None

    def __str__(self) -> str:
        result = ""

        for file in reversed(list(File)):
            result += f"{str(8 - file.value)} "
            for rank in Rank:
                chess_piece = self.get_piece_at_position(rank, file)
                chess_piece_symbol = (
                    " " if chess_piece is None else CHESS_PIECE_UNICODE_MAP[chess_piece]
                )
                result += f"| {chess_piece_symbol} "
            result += f"|\n  {'-' * 4 * 8}\n"
        result += " " * 4 + "   ".join([rank.name for rank in Rank])
        return result
