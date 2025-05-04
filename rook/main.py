from rook.bitboard import Bitboard, File, Rank


def main():
    print("Hello from rook!")

    bitboard = Bitboard()
    # print(f"{bitboard.get_position_mask(Rank.A, File.EIGHT):>064b}")
    # print(f"{bitboard.get_position_mask(Rank.B, File.EIGHT):>064b}")
    # print(f"{bitboard.get_position_mask(Rank.A, File.SEVEN):>064b}")
    # print(f"{bitboard.get_position_mask(Rank.H, File.ONE):>064b}")

    print(bitboard.get_piece_at_position(Rank.A, File.EIGHT))
    print(bitboard.get_piece_at_position(Rank.B, File.EIGHT))
    print(bitboard.get_piece_at_position(Rank.B, File.SEVEN))
    # print(f"{bitboard.black_pawn:064b}")
    # print(f"{bitboard.white_pawn:064b}")
    # print(len(str(f"{bitboard.black_pawn:064b}")))
    # print(bitboard.white_pawn)


if __name__ == "__main__":
    main()
