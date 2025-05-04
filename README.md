# Rook (Chess Engine)

Rook is an elite chess engine that implements the Universal Chess Interface (UCI) that plays the game like no one has seen before. It is smart, fast, and most importantly thinking-ahead at all times.

A chess engine is built in 4 major parts:

1. Board Representation
2. Move Generation
3. Search
4. Evaluation

Each step will be briefly explained to communicate to the reader the methods and techniques that were used to achieve each goal.

## 1. Board Representation

This engine uses a **piece-centric** approach to represent the chess board. This means that we are tracking the individual pieces as opposed to tracking individual squares on the chess board, that approach is known as **square-centric**.

We use [bitboards](https://pages.cs.wisc.edu/~psilord/blog/data/chess-pages/rep.html) to track the locations of the pieces using 64 bit numbers. The engine defines those numbers in the codebase using their binary representation since it's more intuitive to view them in that format.

> **_How do I define a number using binary in Python?:_** You can simply prefix a number with `0b` to define a number using it's binary representation. For example, `num = 0b10` defines the binary number `10` which is the decimal number `2`.

The board representation is composed of two classes in `rook/chess_board.py`:

1. `ChessBoard` -> stores a immutable list (i.e. tuple) of all the chess pieces
2. `ChessPiece` -> represents a chess piece where the piece's positions are encoded in a bitboard
