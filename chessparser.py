import chess
import chess.pgn

def makeNewGame():
    game = open('example.pgn', 'x') #need to add way to input author_id from twitter api
    return game

def pullMoveFromTweet():


def appendToExistingGame(str):
    pgn = open('example.pgn')
    currentGame = chess.pgn.read_game(pgn)
    addedMove = currentGame.add_variation(chess.Move.from_uci(str))