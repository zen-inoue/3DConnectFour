# === main.py（このファイルで「MyAI.get_move」以外は変更しないでください）===

from abc import ABC, abstractmethod
from typing import Tuple, List

Board = List[List[List[int]]]  # board[z][y][x]（0=空, 1=黒, 2=白）

# 変更禁止: 親インターフェース
class Alg3D(ABC):
    @abstractmethod
    def get_move(self, board: Board) -> Tuple[int, int]:
        """(x, y) を返す。0 <= x < 4, 0 <= y < 4"""
        ...

# ここから自由にアルゴリズムを記入 ----------------------------------------
class MyAI(Alg3D):
    def get_move(self, board: Board) -> Tuple[int, int]:
        # ここに自由にアルゴリズムを書いてください。
        # 必ず (x, y) を返してください（0 <= x < 4, 0 <= y < 4）。
        # 例・ヒントやサンプル実装は入れていません。
        raise NotImplementedError("ここに実装してください")
# ----------------------------------------------------------------------

# 変更禁止: サーバが呼ぶエントリポイント（削除・変更しない）
_ai = MyAI()

def get_move(board: Board) -> Tuple[int, int]:
    return _ai.get_move(board)
