import chess
import AI
import random
import os
import pygame
import argparse
from ui import ChessUI


def print_unicode_board(board):
    piece_unicode = {
        'P': '♙', 'N': '♘', 'B': '♗', 'R': '♖', 'Q': '♕', 'K': '♔',
        'p': '♟', 'n': '♞', 'b': '♝', 'r': '♜', 'q': '♛', 'k': '♚',
        '.': '.'
    }
    board_str = str(board) 
    for line in board_str.split('\n'):
        print(' '.join(piece_unicode.get(ch, ch) for ch in line.split()))


def random_agent(board: chess.Board) -> chess.Move:
    """Randomly selects a legal move from the current board state."""
    return random.choice(list(board.legal_moves))

difficulties = {
    "easy": 2,
    "medium": 3,
    "hard": 4
}

results = {
    1: "WIN",
    -1: "LOSE",
    0: "DRAW"
}

def play_game(level: str):
    os.makedirs("logs", exist_ok=True)

    depth = difficulties.get(level.lower())
    if depth is None:
        raise ValueError("Invalid difficulty level. Choose from: easy, medium, hard.")

    ai_score = 0
    random_score = 0
    log_file = f"logs/minimax_{level}_vs_random.txt"

    with open(log_file, "w", encoding="utf-8") as f:
        for i in range(10):
            ai_color = chess.WHITE if i % 2 == 0 else chess.BLACK
            board = chess.Board()
            match_name = f"Match {i+1}"
            turn_info = f"AI goes {'first' if ai_color == chess.WHITE else 'second'}"

            print(f"\n{match_name} ({turn_info})")
            print("Game start!")
            print_unicode_board(board)

            ui = ChessUI(board)
            ui.draw_message(match_name, f"{turn_info} | Difficulty: {level.title()}", wait_time=1500)


            try:
                while not board.is_game_over():
                    ui.render(ai_score, random_score)
                    pygame.display.update()

                    if board.turn == ai_color:
                        print("Turn (AI):")
                        move = AI.best_move_minimax(board, depth, ai_color)
                    else:
                        print("Turn (Random Agent):")
                        move = random_agent(board)

                    if move in board.legal_moves:
                        board.push(move)
                        pygame.time.wait(500)
                    else:
                        print("Invalid move! Skipping.")
                
                # Game finished – evaluate result
                if board.result() == "1-0":
                    win = 1 if ai_color == chess.WHITE else -1
                elif board.result() == "0-1":
                    win = 1 if ai_color == chess.BLACK else -1
                else:
                    win = 0

                if win == 1:
                    ai_score += 1
                elif win == -1:
                    random_score += 1
                else:
                    ai_score += 1
                    random_score += 1

                result_msg = f"AI {results[win]}" if win in results else "Draw"
                print(f"Game over! Result: {ai_score}-{random_score}")
                ui.draw_message(f"End of {match_name}", f"Result: {result_msg}", wait_time=1500)

                log_line = f"[Level: {level}] {match_name}: {results[win]}\n"
                f.write(log_line)

            except Exception as e:
                print(f"Error in game: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI vs Random Chess")
    parser.add_argument("--level", type=str, choices=["easy", "medium", "hard"],
                        help="Difficulty level: easy, medium, or hard (if omitted, run all)")
    args = parser.parse_args()

    if args.level:
        play_game(args.level)
    else:
        for level in ["easy", "medium", "hard"]:
            play_game(level)

