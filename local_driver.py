
#※変更禁止※
#ターミナルでpython local_driver.pyと打つと次の手をかえしてくれる。
# === local_driver.py ===
import importlib.util
from typing import List, Tuple
from abc import ABC, abstractmethod
from stub_board import board

# === Board 定義 ===
Board = List[List[List[int]]]  # board[z][y][x] (0=空,1=黒,2=白)

# === 抽象クラス（サーバーと同じ役割） ===
class Alg3D(ABC):
    @abstractmethod
    def get_move(self, board: Board) -> Tuple[int, int]:
        """次の一手 (x,y) を返す"""
        ...

# === 盤面作成（空盤） ===
def create_board() -> Board:
    return [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]

# === 石を置く ===
def place_disk(board: Board, x: int, y: int, player: int) -> bool:
    for z in range(4):
        if board[z][y][x] == 0:
            board[z][y][x] = player
            return True
    return False  # その列は満杯

# === 学生の AI 読み込み ===
def load_ai(path: str = "main.py"):
    spec = importlib.util.spec_from_file_location("student_ai", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore

    if not hasattr(module, "MyAI"):
        raise AttributeError("main.py に MyAI クラスが定義されていません")

    ai = module.MyAI()
    if not hasattr(ai, "get_move"):
        raise TypeError("MyAI は get_move を実装している必要があります")

    return ai

# === 動作確認用 ===
if __name__ == "__main__":
    ai = load_ai()

    # === 補助関数 ===
    def is_column_full(board, x, y) -> bool:
        for z in range(4):
            if board[z][y][x] == 0:
                return False
        return True

    # AI に次の手を聞く
    x, y = ai.get_move(board)

    print("AI の出力:", (x, y))
