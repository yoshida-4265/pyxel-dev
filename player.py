"""
プレイヤーキャラクターを管理するクラス。
左右移動と描画を担当する。
"""
import pyxel

class Player():
    def __init__(self):
        """プレイヤーを初期位置（画面下寄せ）で生成する。"""
        self.x = 80
        self.y = 128 - 24
    
    def update(self):
        """左右キー入力を受けてプレイヤーを水平方向に移動する。"""
        if pyxel.btn(pyxel.KEY_LEFT) and self.x > 0:
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x <127 - 14:
            self.x += 2
        
        
    
    def draw(self):
        """現在の位置にプレイヤーのスプライトを描画する。"""
        pyxel.blt(self.x, self.y-8, 0, 16, 0, 16, 16, 0)
