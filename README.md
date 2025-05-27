# Rook – UCI Chess Engine

**Rook** is a high-performance chess engine that implements the [Universal Chess Interface (UCI)](https://en.wikipedia.org/wiki/Universal_Chess_Interface). Designed for speed, intelligence, and forward-thinking play, Rook offers a unique and efficient approach to computer chess.

The engine is built upon four foundational components:

1. **Board Representation**
2. **Move Generation**
3. **Search**
4. **Evaluation**

Each of these components is outlined below, with an overview of the key methods and techniques used in the implementation.

---

## 1. Board Representation

Rook uses a **piece-centric** model to represent the game state. Unlike the more traditional **square-centric** approach (which focuses on individual squares), the piece-centric design tracks each individual chess piece directly.

To efficiently represent and manipulate positions, the engine uses [bitboards](https://pages.cs.wisc.edu/~psilord/blog/data/chess-pages/rep.html)—64-bit integers where each bit corresponds to a square on the board. Bitboards enable fast and parallelizable bitwise operations, making them ideal for modern chess engine development.

For clarity and readability, binary literals are used directly in the codebase:

> **Tip:** In Python, binary numbers can be defined using the `0b` prefix. For example, `num = 0b10` represents the binary number `10`, which equals `2` in decimal.

### Implementation Details

The board representation is implemented in `rook/chess_board.py` and consists of two primary classes:

- `ChessBoard`: Maintains an immutable tuple of all active chess pieces.
- `ChessPiece`: Represents individual pieces, with their positions encoded via bitboards.

---

More documentation coming soon for the remaining core components (Move Generation, Search, and Evaluation). Stay tuned!
