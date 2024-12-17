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
    fire_img = pg.image.load("fig/fire.jpg")  # 爆発画像をロード
    fire_img = pg.transform.scale(fire_img, (500, 500))  # 爆発画像のサイズを変更
    idoukyori = 0
    explosion_migi = False  # 右の爆発の状態を初期化
    explosion_hidari = False  # 左の爆発の状態を初期化

    pg.display.set_caption("こうかとんをよけろ！")  # ウィンドウのキャプションを設定
    screen = pg.display.set_mode((sizex, sizey))  # ウィンドウのサイズを設定し、スクリーンサーフェースを作成
    clock  = pg.time.Clock()  # クロックオブジェクトを作成し、時間管理を行う
    bg_img = pg.image.load("fig/tuujyou_miti3.jpg")  # 背景画像をロード
    bg_img = pg.transform.scale(bg_img, (sizex, sizey))  # 背景画像のサイズを変更


    # kt_img = pg.image.load("fig/fire.jpg")  # 車の画像をロード
    # kt_img = pg.transform.scale(kt_img, (100, 200))  # 車の画像のサイズを変更
    # kt_img = pg.transform.flip(kt_img, True, False)  # 車の画像を左右反転

    # kt_rct = kt_img.get_rect()  # 車の画像の矩形（Rect）オブジェクトを取得
    # kt_rct.center = 300, 530  # 車の矩形オブジェクトの中心を設定
    while True:
        #key_lst = pg.key.get_pressed()  # 押されているキーのリストを取得
        # if key_lst[pg.K_LEFT]:  # 左矢印キーが押されたら
        #     if sokudo > 0.5:
        #         if sokudo < 25:
        #             kx = -1-(sokudo/25)*2
        #         else:
        #             kx = -3
        # elif key_lst[pg.K_RIGHT]:  # 右矢印キーが押されたら
        #     if sokudo > 0.5:
        #         if sokudo < 25:
        #             kx = 1+(sokudo/25)*2
        #         else:
        #             kx = 3
        # kt_rct.move_ip(kx, 0)  # 車の矩形オブジェクトを移動


        idoukyori += 5
        idoukyori %= sizey
        screen.blit(bg_img, [0, idoukyori])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 1])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 2])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 3])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 4])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 5])  # 背景画像をスクリーンに描画
        #screen.blit(kt_img, kt_rct)  # 車の画像をスクリーンに描画

        #  壁に衝突したかどうかを判定
        # if kt_rct.right >= screen.get_width():
        #     explosion_migi = True  # 爆発の状態を設定

        # elif kt_rct.left <= 0:
        #     explosion_hidari = True
        
        # if brake_timer > 0:
        #     draw_brake_lamp(screen, kt_rct)
        #     brake_timer -= 1
        
        fire_rct = fire_img.get_rect()  # 爆発画像の矩形を車の右側に設定
        screen.blit(fire_img, fire_rct)  # 爆発画像を描画
        # 爆発画像を描画
        # if explosion_hidari:
        #     fire_rct = fire_img.get_rect(midleft=(kt_rct.right - 250, kt_rct.centery))  # 爆発画像の矩形を車の右側に設定
        #     screen.blit(fire_img, fire_rct.topleft)  # 爆発画像を描画
        #     # ending(screen,sizey,sizex,int(max_speed), tmr // framerate, ("%.3f"%(distance)))
        #     return
        # if explosion_migi:
        #     fire_rct = fire_img.get_rect(midright=(kt_rct.left + 250, kt_rct.centery))  # 爆発画像の矩形を車の左側に設定
        #     screen.blit(fire_img, fire_rct.topleft)  # 爆発画像を描画
        #     # ending(screen,sizey,sizex,int(max_speed), tmr // framerate, ("%.3f"%(distance)))
        #     return
        
        pg.display.update() # 画面を更新
        clock.tick(framerate)  # フレームレートを設定

if __name__ == "__main__":
    pg.init()  # Pygameを初期化
    main()  # メイン関数を実行
    pg.quit()  # Pygameを終了
    sys.exit()  # プログラムを終了