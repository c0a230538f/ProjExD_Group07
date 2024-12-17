import os  # OS関連の機能を提供するモジュールをインポート
import sys  # システム関連の機能を提供するモジュールをインポート
import pygame as pg #Pygameモジュールをpgという名前でインポート
import math # 数学関連の機能を提供するモジュールをインポート
import time # 時間関連の機能を提供するモジュールをインポート
import random # 乱数関連の機能を提供するモジュールをインポート
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # スクリプトのディレクトリにカレントディレクトリを変更

def coment1(screen: pg.surface,yoko,tate, start_time):
    """
    画面に「急ブレーキ」という文字を表示する
    引数: screen, yoko, tate, start_time
    戻り値: start_time + 3
    """
    # 日本語を描画するために、フォントファイルを指定
    font_path = pg.font.match_font('msgothic')  # MS ゴシックフォントを使用
    font = pg.font.Font(font_path, 120)  # フォントを作成
    moji = font.render("急ブレーキ", True, (255, 0, 0))  # 文字の内容と色を指定
    screen.blit(moji, [yoko-100, tate])  # 文字を画面に描画
    pg.display.update()
    return start_time + 3

class GameOverScreen:
    """
    ゲームオーバー画面を表示するクラス
    """
    def __init__(self, screen: pg.Surface, WIDTH: int, HEIGHT: int):
        """
        ゲームオーバー画面を表示するクラスのコンストラクタ
        引数: screen, WIDTH, HEIGHT
        戻り値: なし
        """
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def display(self, max_speed: int, elapsed_time: int, distance: int):
        """
        ゲームオーバー画面を表示する
        引数: max_speed, elapsed_time, distance
        戻り値: なし
        """
        background = pg.Surface(self.screen.get_size())  # 画面と同じサイズのSurfaceを作成
        pg.draw.rect(background, (0, 0, 0), (0, 0, self.WIDTH, self.HEIGHT))  # 黒色の背景を描画
        pg.Surface.set_alpha(background, 130)  # 透明度を130に設定
        self.screen.blit(background, (0, 0))  # 背景を画面に描画

        # ハイライトのための背景矩形を描画
        highlight_rect = pg.Rect(self.WIDTH / 2 - 175, self.HEIGHT / 2 - 10, 365, 70)
        pg.draw.rect(self.screen, (255,255,153), highlight_rect)

        font = pg.font.Font(None, 80)  # フォントを作成
        moji = font.render("GAME OVER", True, (255, 0, 0))  # 文字の内容と色を指定
        self.screen.blit(moji, [self.WIDTH / 2 - 165, self.HEIGHT / 2])  # 文字を画面に描画

        font_small = pg.font.Font(None, 36)
        max_speed_text = font_small.render(f"Max Speed: {max_speed} km/h", True, (255, 255, 255))
        elapsed_time_text = font_small.render(f"Time: {elapsed_time} s", True, (255, 255, 255))
        distance_text = font_small.render(f"Distance: {distance} km", True, (255, 255, 255))

        self.screen.blit(max_speed_text, (self.WIDTH // 2 - 100, self.HEIGHT // 2 - 50))
        self.screen.blit(elapsed_time_text, (self.WIDTH // 2 - 100, self.HEIGHT // 2 - 100))
        self.screen.blit(distance_text, (self.WIDTH // 2 - 100, self.HEIGHT // 2 - 150))
        pg.display.update()
        time.sleep(10)  # 10秒間待つ
        pg.quit()  # Pygameを終了

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
    down_key_start_time = None  # 下キーが押され始めた時間を初期化

    while True:
        for event in pg.event.get():  # イベントキューからイベントを取得
            if event.type == pg.QUIT: return  # ウィンドウの閉じるボタンが押されたら終了

        key_lst = pg.key.get_pressed()  # 押されているキーのリストを取得

        if key_lst[pg.K_DOWN]: # 下キーが押されている場合
            if down_key_start_time is None: # 下キーが押され始めた時間が未設定の場合
                down_key_start_time = time.time() # 下キーが押され始めた時間を記録
            elif time.time() - down_key_start_time >= 1: # 下キーが1秒以上押され続けている場合
                # 下キーが3秒間押され続けた場合に実行する処理
                if sokudo > 0:
                    coment1(screen, 100, 100, time.time())    

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