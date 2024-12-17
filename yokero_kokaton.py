import os  # OS関連の機能を提供するモジュールをインポート
import sys  # システム関連の機能を提供するモジュールをインポート
import pygame as pg #Pygameモジュールをpgという名前でインポート
import math # 数学関連の機能を提供するモジュールをインポート
import time # 時間関連の機能を提供するモジュールをインポート
import random # 乱数関連の機能を提供するモジュールをインポート
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # スクリプトのディレクトリにカレントディレクトリを変更


class Bird():
    def __init__(self):
        """
        こうかとんの初期化
        """
        self.img = pg.image.load("fig/5.png") #こうかとん画像をロード
        self.rect = self.img.get_rect() #こうかとんの画像のオブジェクトを取得
         
        bird_x = random.randint(0,2)  # #こうかとんのオブジェクトのx座標の種類を設定
        if bird_x == 0:
            self.rect.x = 100 #左車線に生成
        elif bird_x == 1:
            self.rect.x = 300 #真ん中車線に生成
        elif bird_x == 2:
            self.rect.x = 500 #右車線に生成
        self.rect.y = -100  # 初期位置は画面の上
        
    
    def update(self, speed):
        """
        こうかとんを下に移動する
        """
        self.speed = speed  # こうかとんが動く速度
        self.rect.y += self.speed

    def draw(self, screen):
        """
        こうかとんを描画する
        """
        screen.blit(self.img, self.rect)

    
    def off_screen(self, screen_height):
        """
        画面外に出たか判定
        """
        return self.rect.y > screen_height

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
    kks = [] #こうかとんのリスト
    spawn_timer = 600 #こうかとんが出現する頻度
    
    while True:
        #key_lst = pg.key.get_pressed()  # 押されているキーのリストを取得

        spawn_timer -= 5
        if spawn_timer < 0:  # 120フレームごとにこうかとんを生成
            kks.append(Bird())
            spawn_timer = 600

        for obj in kks[:]:
            obj.update(5)
           # if obj.rect.colliderect( ): #車の変数を入れる
                 # 衝突したらゲームオーバー
            if obj.off_screen(sizey):
                kks.remove(obj)

        idoukyori += 5
        idoukyori %= sizey
        screen.blit(bg_img, [0, idoukyori])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 1])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 2])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 3])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 4])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 5])  # 背景画像をスクリーンに描画
        
        for obj in kks:
            obj.draw(screen)

        pg.display.update() # 画面を更新
        clock.tick(framerate)  # フレームレートを設定

if __name__ == "__main__":
    pg.init()  # Pygameを初期化
    main()  # メイン関数を実行
    pg.quit()  # Pygameを終了
    sys.exit()  # プログラムを終了