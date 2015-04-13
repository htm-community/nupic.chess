## Work in Progress

Currently accepts a history of games in [PGN format](http://en.wikipedia.org/wiki/Portable_Game_Notation) and writes out each board state in [FEN format](http://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation).

Next: Create a ChessEncoder class that accepts FEN board states in `nupic/encoders/chessboard.py`.

## Dependencies

    pip install pgnparser python-chess

## Run it

    python gameparser.py ./samplegames/csvn1981.pgn output.txt
