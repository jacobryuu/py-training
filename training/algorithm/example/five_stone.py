from enum import Enum
from typing import List, Tuple


class Stone(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2


class Board:
    def __init__(self, size: int):
        self.size = size
        self.grid = [[Stone.EMPTY for _ in range(size)] for _ in range(size)]
    
    def place_stone(self, x: int, y: int, stone: Stone) -> bool:
        """Place a stone on the board"""
        if self.is_out_of_board(x, y):
            return False
        if self.grid[x][y] != Stone.EMPTY:
            return False
        self.grid[x][y] = stone
        return True
    
    def is_out_of_board(self, x: int, y: int) -> bool:
        """Check if position is out of board"""
        return x < 0 or x >= self.size or y < 0 or y >= self.size
    
    def get_stone(self, x: int, y: int) -> Stone:
        """Get stone at position"""
        if self.is_out_of_board(x, y):
            return Stone.EMPTY
        return self.grid[x][y]


class Player:
    def __init__(self, name: str, stone: Stone):
        self.name = name
        self.stone = stone
    
    def get_name(self) -> str:
        return self.name
    
    def get_stone(self) -> Stone:
        return self.stone


class FiveStone:
    def __init__(self, board_size: int, player1_name: str, player2_name: str):
        self.board = Board(board_size)
        self.player1 = Player(player1_name, Stone.BLACK)
        self.player2 = Player(player2_name, Stone.WHITE)
        self.current = self.player1
    
    def play(self, x: int, y: int):
        """Make a move at position (x, y)"""
        if not self.board.place_stone(x, y, self.current.get_stone()):
            print("Invalid move!")
            return
        
        print(f"{self.current.get_name()} placed a stone at ({x}, {y})")
        if self.check_win(self.board, x, y, self.current.get_stone()):
            print(f"{self.current.get_name()} wins!")
            return
        
        # Switch player
        self.current = self.player2 if self.current == self.player1 else self.player1
    
    @staticmethod
    def check_win(board: Board, x: int, y: int, stone: Stone) -> bool:
        """Check if placing a stone at (x, y) results in a win"""
        directions = [
            (1, 0),   # Horizontal
            (0, 1),   # Vertical
            (1, 1),   # Diagonal \
            (1, -1)   # Diagonal /
        ]
        
        for dx, dy in directions:
            count = 1
            count += FiveStone.count_stones(board, x, y, dx, dy, stone)
            count += FiveStone.count_stones(board, x, y, -dx, -dy, stone)
            if count >= 5:
                return True
        return False
    
    @staticmethod
    def count_stones(board: Board, x: int, y: int, dx: int, dy: int, stone: Stone) -> int:
        """Count consecutive stones in a direction"""
        count = 0
        nx = x + dx
        ny = y + dy
        
        while not board.is_out_of_board(nx, ny) and board.get_stone(nx, ny) == stone:
            count += 1
            nx += dx
            ny += dy
        return count


def main():
    game = FiveStone(15, "Alice", "Bob")
    game.play(7, 7)
    game.play(7, 8)
    game.play(8, 7)
    game.play(8, 8)
    game.play(9, 7)
    game.play(9, 8)
    game.play(10, 7)
    game.play(10, 8)
    game.play(11, 7)  # Alice wins


if __name__ == "__main__":
    main()
