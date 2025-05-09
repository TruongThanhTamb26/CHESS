import chess
import random
import math

"""
Handling the AI moves.
Có sử dụng thuật toán Minimax và cắt tỉa Alpha-beta
"""

knight_scores = [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0,
                 0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1,
                 0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2,
                 0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2,
                 0.2, 0.55, 0.65, 0.7, 0.7, 0.65, 0.55, 0.2,
                 0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2,
                 0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1,
                 0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]

bishop_scores = [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0,
                 0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2,
                 0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2,
                 0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2,
                 0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2,
                 0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2,
                 0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2,
                 0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]

rook_scores = [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25,
               0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0,
               0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0,
               0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0,
               0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0,
               0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0,
               0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5,
               0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]

queen_scores = [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0,
                0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2,
                0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2,
                0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3,
                0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3,
                0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2,
                0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2,
                0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]

pawn_scores = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
               0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25,
               0.25, 0.15, 0.1, 0.2, 0.2, 0.1, 0.15, 0.25,
               0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2,
               0.25, 0.25, 0.3, 0.45, 0.45, 0.3, 0.25, 0.25,
               0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3,
               0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7,
               0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]

king_scores = [0.8, 1.0, 0.8, 0.6, 0.6, 0.8, 1.0, 0.8,
               0.5, 0.6, 0.3, 0.2, 0.2, 0.3, 0.6, 0.5,
               0.3, 0.4, 0.2, 0.1, 0.1, 0.2, 0.4, 0.3,
               0.2, 0.3, 0.1, 0.0, 0.0, 0.1, 0.3, 0.2,
               0.2, 0.3, 0.1, 0.0, 0.0, 0.1, 0.3, 0.2,
               0.2, 0.3, 0.1, 0.0, 0.0, 0.1, 0.3, 0.2,
               0.2, 0.3, 0.1, 0.0, 0.0, 0.1, 0.3, 0.2,
               0.2, 0.3, 0.1, 0.0, 0.0, 0.1, 0.3, 0.2]

pos_scores = {"wN": knight_scores,
              "bN": knight_scores[::-1],
              "wB": bishop_scores,
              "bB": bishop_scores[::-1],
              "wQ": queen_scores,
              "bQ": queen_scores[::-1],
              "wR": rook_scores,
              "bR": rook_scores[::-1],
              "wP": pawn_scores,
              "bP": pawn_scores[::-1],
              "wK": king_scores,
              "bK": king_scores[::-1]}

piece_values = { 
    chess.PAWN: 1,
    chess.KNIGHT: 3, 
    chess.BISHOP: 3, 
    chess.ROOK: 5, 
    chess.QUEEN: 9, 
    chess.KING: 0  # King is invaluable 
}

# CHECKMATE = 1000
# STALEMATE = 0
# DEPTH = 3

# Đánh giá mức độ quan trọng của từng quân cờ (VD: 0 là không thể để mất, Q là quan trọng nhất và chỉ mang tính tương đối)
def evaluate_board(board, ai_color):
    if board.is_game_over():
        if board.is_checkmate():
            return 1000 if board.turn != ai_color else -1000
        else:
            return 0
    
    evaluation = 0
    
    multiplier = 1 if ai_color == chess.WHITE else -1
    
    for piece in chess.PIECE_TYPES:
        symbol = chess.piece_symbol(piece).upper()
        for square in board.pieces(piece, chess.WHITE):
            evaluation += multiplier * (piece_values[piece] + pos_scores["w" + symbol][square])
        for square in board.pieces(piece, chess.BLACK):
            evaluation -= multiplier * (piece_values[piece] + pos_scores["b" + symbol][square])
     
    return evaluation

"""Hiện thưc thuật toán Minimax và tìm nước đi tối ưu"""
# Minimax Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, maximizing_player, ai_color):
    if board.is_game_over() or depth == 0:
        return evaluate_board(board, ai_color), None

    best_move = None
    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, False, ai_color)
            board.pop()

            if eval > max_eval:
                max_eval = eval
                best_move = move

            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, True, ai_color)
            board.pop()

            if eval < min_eval:
                min_eval = eval
                best_move = move

            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

# Chọn nước đi tốt nhất bằng Minimax
def best_move_minimax(board, depth, ai_color):
    _, move = minimax(board, depth, float('-inf'), float('inf'), board.turn == ai_color, ai_color)
    return move
