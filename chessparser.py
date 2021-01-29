import chess
import chess.pgn
import io

pgn = open("fischer_v_spassky.pgn")

first_game = chess.pgn.read_game(pgn)

print(first_game)

