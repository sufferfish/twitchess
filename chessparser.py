import chess
import chess.pgn
import io

def openPGN():
    pgn = open("fischer_v_spassky.pgn")
    first_game = chess.pgn.read_game(pgn)
    return first_game

print(first_game)