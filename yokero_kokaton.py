import os  # OS関連の機能を提供するモジュールをインポート
import sys  # システム関連の機能を提供するモジュールをインポート
import pygame as pg #Pygameモジュールをpgという名前でインポート
import math # 数学関連の機能を提供するモジュールをインポート
import time # 時間関連の機能を提供するモジュールをインポート
import random # 乱数関連の機能を提供するモジュールをインポート
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # スクリプトのディレクトリにカレントディレクトリを変更

def main():
    sizex = 600 # ウィンドウの幅を設定
    sizey = 800 # ウィンドウの高さを設定
    framerate = 200 # フレームレートを設定
    idoukyori = 0

    pg.display.set_caption("こうかとんをよけろ！")  # ウィンドウのキャプションを設定
    screen = pg.display.set_mode((sizex, sizey))  # ウィンドウのサイズを設定し、スクリーンサーフェースを作成
    clock  = pg.time.Clock()  # クロックオブジェクトを作成し、時間管理を行う
    bg_img = pg.image.load("fig/tuujyou_miti3.jpg")  # 背景画像をロード
    bg_img = pg.transform.scale(bg_img, (sizex, sizey))  # 背景画像のサイズを変更
    while True:
        #key_lst = pg.key.get_pressed()  # 押されているキーのリストを取得

        idoukyori += 5
        idoukyori %= sizey
        screen.blit(bg_img, [0, idoukyori])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 1])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 2])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 3])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 4])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 5])  # 背景画像をスクリーンに描画
        
        pg.display.update() # 画面を更新
        clock.tick(framerate)  # フレームレートを設定

if __name__ == "__main__":
    pg.init()  # Pygameを初期化
    main()  # メイン関数を実行
    pg.quit()  # Pygameを終了
    sys.exit()  # プログラムを終了