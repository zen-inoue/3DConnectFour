1. 🔧 提出物の仕様	
項目	内容
ファイル拡張子	.py
必須関数	get_move(board: list[list[list[int]]]) -> tuple[int, int]
戻り値	(x, y) のタプル（0〜3 の範囲）
出力制御	最初に必ず print("send_board") を出力すること（ハンドシェイク用）。その他のデバッグ出力は自由（stderrに流れます）。
利用可能ライブラリ	Python標準ライブラリのみ（一部禁止あり）
禁止ライブラリ	os, sys, subprocess, socket, requests, urllib, http, asyncio, threading, multiprocessing, など
禁止関数	open, eval, exec, compile, __import__, system, popen
Pythonバージョン	サーバは Python 3.9 互換 で実行（match文など3.10以降専用構文は不可）
実行制限	メモリ最大 約1GB、CPU時間 約3秒、1手あたり待ち時間上限 30秒
失敗時の扱い	タイムアウト／異常終了／無効座標 → 左上から置けるマスに強制配置し、理由が記録されます
✔️ サンプル実装	
	
"# === main.py（このファイルで「MyAI.get_move」以外は変更しないでください）===

from abc import ABC, abstractmethod
from typing import Tuple, List

Board = List[List[List[int]]]  # board[z][y][x]（0=空, 1=黒, 2=白）

# 変更禁止: 親インターフェース
class Alg3D(ABC):
    @abstractmethod
    def get_move(self, board: Board) -> Tuple[int, int]:
        """"""(x, y) を返す。0 <= x < 4, 0 <= y < 4""""""
        ...

# ここから自由にアルゴリズムを記入 ----------------------------------------
class MyAI(Alg3D):
    def get_move(self, board: Board) -> Tuple[int, int]:
        # ここに自由にアルゴリズムを書いてください。
        # 必ず (x, y) を返してください（0 <= x < 4, 0 <= y < 4）。
        # 例・ヒントやサンプル実装は入れていません。
        raise NotImplementedError(""ここに実装してください"")
# ----------------------------------------------------------------------

# 変更禁止: サーバが呼ぶエントリポイント（削除・変更しない）
_ai = MyAI()

def get_move(board: Board) -> Tuple[int, int]:
    return _ai.get_move(board)
"	
	
2. 📦 提出方法（GitHub 経由）	
	
	
"提出は、以下のリポジトリを フォーク（Fork） して、自分のアカウントにコピーしてください。
フォークした後のリポジトリを編集して提出用に使います。
Private（非公開）ではなく Public（公開）リポジトリにしてください。"	
リポジトリURL: https://github.com/zen-integration/algorithm_code	
	
上記形式で main.py を保存（ファイル名は必ず main.py）	
