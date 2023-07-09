import chess
import chess.engine

def play_chess():
    board = chess.Board()
    engine = chess.engine.SimpleEngine.popen_uci("path/to/chess/engine")

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            result = engine.play(board, chess.engine.Limit(time=2.0))
        else:
            result = engine.play(board, chess.engine.Limit(time=2.0))

        board.push(result.move)
        print("AI's move:", result.move)

    engine.quit()

play_chess()