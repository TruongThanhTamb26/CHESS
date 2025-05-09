import pygame
import chess

SQ_SIZE = 80
WIDTH, HEIGHT = 8 * SQ_SIZE, 8 * SQ_SIZE
WHITE = (255,255,224)
BROWN = (107,142,35)
FONT_COLOR = (255, 255, 255)
HIGHLIGHT_COLOR = (135,206,235)  
SHADOW_COLOR = (106,90,205)

class ChessUI:
    def __init__(self, board):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT + 100))  
        pygame.display.set_caption("AI Chess vs Agent")
        self.board = board
        self.clock = pygame.time.Clock()
        self.images = self.load_images()

    def load_images(self):
        images = {}
        pieces = ['P', 'N', 'B', 'R', 'Q', 'K']
        for piece in pieces:
            images['w' + piece] = pygame.transform.scale(pygame.image.load(f"images/w{piece}.png"), (SQ_SIZE, SQ_SIZE))
            images['b' + piece] = pygame.transform.scale(pygame.image.load(f"images/b{piece}.png"), (SQ_SIZE, SQ_SIZE))
        return images

    def draw_message(self, message, sub_message=None, wait_time=2000):
        self.screen.fill(SHADOW_COLOR)
        font = pygame.font.SysFont("Times New Roman", 40, bold=True)
        text = font.render(message, True, FONT_COLOR)
        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
        self.screen.blit(text, rect)

        if sub_message:
            sub_font = pygame.font.SysFont("Times New Roman", 30)
            sub_text = sub_font.render(sub_message, True, HIGHLIGHT_COLOR)
            sub_rect = sub_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
            self.screen.blit(sub_text, sub_rect)

        pygame.display.flip()
        pygame.time.wait(wait_time)


    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = WHITE if (row + col) % 2 == 0 else BROWN
                pygame.draw.rect(self.screen, color, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def draw_pieces(self):
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                col = chess.square_file(square)
                row = 7 - chess.square_rank(square)
                symbol = piece.symbol().upper()
                color = 'w' if piece.color == chess.WHITE else 'b'
                self.screen.blit(self.images[color + symbol], pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def draw_score(self, ai_score, random_score):
        font = pygame.font.SysFont("Times New Roman", 36, bold=True)
        
        # Vẽ lại nền cho khu vực hiển thị bảng tỉ số và lượt đi
        pygame.draw.rect(self.screen, SHADOW_COLOR, pygame.Rect(0, HEIGHT, WIDTH, 100))  
        
        # Vẽ bóng đổ cho bảng tỉ số
        score_text = font.render(f"AI {ai_score} - {random_score} Random Agent", True, FONT_COLOR)
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT + 30))
        pygame.draw.rect(self.screen, SHADOW_COLOR, score_rect.inflate(5, 5), 3) 
        self.screen.blit(score_text, score_rect)

        # Thêm thông báo ai đang đi
        turn_text = font.render(f"Turn: {'AI' if self.board.turn == chess.WHITE else 'Random Agent'}", True, HIGHLIGHT_COLOR)
        turn_rect = turn_text.get_rect(center=(WIDTH // 2, HEIGHT + 70))
        pygame.draw.rect(self.screen, SHADOW_COLOR, turn_rect.inflate(5, 5), 3)  
        self.screen.blit(turn_text, turn_rect)

    def render(self, ai_score, random_score):
        self.draw_board()
        self.draw_pieces()
        self.draw_score(ai_score, random_score)
        pygame.display.flip()
        self.clock.tick(15)

    def quit(self):
        pygame.quit()
