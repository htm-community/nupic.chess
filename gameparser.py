import sys
import pgn
import chess


def populateStartGameBoardState():
  board = chess.Board().fen()
  return board


def getNextBoardState(board, move):
  chessBoard = chess.Board(fen=board)
  chessBoard.push_san(move)
  return chessBoard.fen()

def processGame(game):
  # Initial board state.
  fenBoardHistory = [populateStartGameBoardState()]

  # For each move in the game, add new board state.
  for move in game.moves:
    if move in ["0-1", "1-0", "1/2-1/2"]:
      print "Skipping %s..." % move
    else:
      fenBoardHistory.append(getNextBoardState(fenBoardHistory[-1], move))
  return fenBoardHistory

def parseGames(gameText):
  game = pgn.PGNGame()
  games = pgn.loads(gameText)
  return games


def readMovesFromFile(f):
  gameHistories = []
  with open(f) as inputPgn:
    games = parseGames(inputPgn.read())
    for game in games:
      gameHistories.append(processGame(game))
  return gameHistories



if __name__ == "__main__":
  with open(sys.argv[2], "wb") as outputFile:
    for game in readMovesFromFile(sys.argv[1]):
      outputFile.write("\n".join(game))
      outputFile.write("\n\n")