from dataclasses import dataclass, field
from enum import Enum
import math
from typing import Literal, Optional, Tuple

# --------------- CONSTANTS ----------

BOARD_SIZE = 8

# --------------- ENUMS ----------


class Rank(Enum):
    "Value corresponds to a column index"

    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7


class File(Enum):
    "Value corresponds to a row index"

    ONE = 7
    TWO = 6
    THREE = 5
    FOUR = 4
    FIVE = 3
    SIX = 2
    SEVEN = 1
    EIGHT = 0


# --------------- CLASS DEFINITIONS ----------


@dataclass
class ChessPiece:
    name: Literal["pawn", "bishop", "rook", "queen", "king", "knight"]
    colour: Literal["black", "white"]

    unicode_symbol: Literal[
        "♙", "♖", "♘", "♗", "♕", "♔", "♟", "♜", "♞", "♝", "♛", "♚"
    ] = field(init=False)
    bitboard: int = field(init=False)

    def __post_init__(self):
        match (self.colour, self.name):
            case ("white", "pawn"):
                self.bitboard = 0b_00000000_00000000_00000000_00000000_00000000_00000000_11111111_00000000
                self.unicode_symbol = "♙"
            case ("white", "rook"):
                self.bitboard = 0b_00000000_00000000_00000000_00000000_00000000_00000000_00000000_10000001
                self.unicode_symbol = "♖"
            case ("white", "knight"):
                self.bitboard = 0b_00000000_00000000_00000000_00000000_00000000_00000000_00000000_01000010
                self.unicode_symbol = "♘"
            case ("white", "bishop"):
                self.bitboard = 0b_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00100100
                self.unicode_symbol = "♗"
            case ("white", "queen"):
                self.bitboard = 0b_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00010000
                self.unicode_symbol = "♕"
            case ("white", "king"):
                self.bitboard = 0b_00000000_00000000_00000000_00000000_00000000_00000000_00000000_00001000
                self.unicode_symbol = "♔"
            case ("black", "pawn"):
                self.bitboard = 0b_00000000_11111111_00000000_00000000_00000000_00000000_00000000_00000000
                self.unicode_symbol = "♟"
            case ("black", "rook"):
                self.bitboard = 0b_10000001_00000000_00000000_00000000_00000000_00000000_00000000_00000000
                self.unicode_symbol = "♜"
            case ("black", "knight"):
                self.bitboard = 0b_01000010_00000000_00000000_00000000_00000000_00000000_00000000_00000000
                self.unicode_symbol = "♞"
            case ("black", "bishop"):
                self.bitboard = 0b_00100100_00000000_00000000_00000000_00000000_00000000_00000000_00000000
                self.unicode_symbol = "♝"
            case ("black", "queen"):
                self.bitboard = 0b_00010000_00000000_00000000_00000000_00000000_00000000_00000000_00000000
                self.unicode_symbol = "♛"
            case ("black", "king"):
                self.bitboard = 0b_00001000_00000000_00000000_00000000_00000000_00000000_00000000_00000000
                self.unicode_symbol = "♚"


@dataclass(frozen=True)
class ChessBoard:
    pieces: Tuple[ChessPiece, ...] = (
        ChessPiece(name="pawn", colour="white"),
        ChessPiece(name="bishop", colour="white"),
        ChessPiece(name="knight", colour="white"),
        ChessPiece(name="rook", colour="white"),
        ChessPiece(name="queen", colour="white"),
        ChessPiece(name="king", colour="white"),
        ChessPiece(name="pawn", colour="black"),
        ChessPiece(name="bishop", colour="black"),
        ChessPiece(name="knight", colour="black"),
        ChessPiece(name="rook", colour="black"),
        ChessPiece(name="queen", colour="black"),
        ChessPiece(name="king", colour="black"),
    )

    def get_position_mask(self, rank: Rank, file: File) -> int:
        return int(math.pow(2, 63 - rank.value - file.value * BOARD_SIZE))

    def get_piece_at_position(self, rank: Rank, file: File) -> Optional[ChessPiece]:
        position_mask = self.get_position_mask(rank, file)

        for chess_piece in self.pieces:
            if chess_piece.bitboard & position_mask:
                return chess_piece
        return None

    def __str__(self) -> str:
        result = f"{' ' * 2}{'-' * 4 * BOARD_SIZE}\n"

        for file in reversed(list(File)):
            result += f"{str(BOARD_SIZE - file.value)} "
            for rank in Rank:
                chess_piece = self.get_piece_at_position(rank, file)
                chess_piece_symbol = (
                    " " if chess_piece is None else chess_piece.unicode_symbol
                )
                result += f"| {chess_piece_symbol} "
            result += f"|\n  {'-' * 4 * BOARD_SIZE}\n"
        result += " " * 4 + "   ".join([rank.name for rank in Rank])
        return result
