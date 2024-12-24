import os  # OS関連の機能を提供するモジュールをインポート
import sys  # システム関連の機能を提供するモジュールをインポート
import pygame as pg #Pygameモジュールをpgという名前でインポート
import math # 数学関連の機能を提供するモジュールをインポート
import time # 時間関連の機能を提供するモジュールをインポート
import random # 乱数関連の機能を提供するモジュールをインポート
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # スクリプトのディレクトリにカレントディレクトリを変更


def draw_blinker(screen, kt_rct, direction):  # ウインカーを描画する関数を定義
    """
    ウインカーを描画する関数

    screen: 描画する
    kt_rct: 車の矩形オブジェクト
    direction: ウインカーの方向(left, right)
    Returns: なし

    """
    blinker_color = (255, 255, 0)  # ウインカーの色を黄色に設定
    blinker_size = (10, 20)  # ウインカーのサイズを設定
    if direction == "left":  # 左に動く場合
        blinker_positions = [  # 左ウインカーの位置を設定
            (kt_rct.left - blinker_size[0], kt_rct.top),
            (kt_rct.left - blinker_size[0], kt_rct.bottom - blinker_size[1])
        ]
    elif direction == "right":  # 右に動く場合
        blinker_positions = [  # 右ウインカーの位置を設定
            (kt_rct.right, kt_rct.top),
            (kt_rct.right, kt_rct.bottom - blinker_size[1])
        ]
    for pos in blinker_positions:
        pg.draw.rect(screen, blinker_color, (*pos, *blinker_size))  # ウインカーを描画  # ウインカーを描画


def draw_brake_lamp(screen, kt_rct):  # ブレーキランプを描画する関数を定義
    """
    ブレーキランプを描画する関数

    screen: 描画する
    kt_rct: 車の矩形オブジェクト

    Returns: なし
    """
    brake_lamp_color = (255, 0, 0)  # ブレーキランプの色を赤色に設定
    brake_lamp_size = (20, 10)  # ブレーキランプのサイズを設定
    brake_lamp_positions = [  # ブレーキランプの位置を設定
        (kt_rct.left, kt_rct.bottom - brake_lamp_size[1]),
        (kt_rct.right - brake_lamp_size[0], kt_rct.bottom - brake_lamp_size[1])
    ]
    for pos in brake_lamp_positions:
        pg.draw.rect(screen, brake_lamp_color, (*pos, *brake_lamp_size))  # ブレーキランプを描画



def main():
    """
    メイン関数
    
    Returns: なし
    """
    sizex = 600 # ウィンドウの幅を設定
    sizey = 800 # ウィンドウの高さを設定
    framerate = 200 # フレームレートを設定
    idoukyori = 0

    pg.display.set_caption("こうかとんをよけろ！")  # ウィンドウのキャプションを設定
    screen = pg.display.set_mode((sizex, sizey))  # ウィンドウのサイズを設定し、スクリーンサーフェースを作成
    clock  = pg.time.Clock()  # クロックオブジェクトを作成し、時間管理を行う
    tmr = 0  # タイマーを初期化
    bg_img = pg.image.load("fig/tuujyou_miti3.jpg")  # 背景画像をロード
    bg_img = pg.transform.scale(bg_img, (sizex, sizey))  # 背景画像のサイズを変更
    kt_img = pg.image.load("fig/car1.png")  # 車の画像をロード
    kt_img = pg.transform.scale(kt_img, (100, 200))  # 車の画像のサイズを変更
    kt_img = pg.transform.flip(kt_img, True, False)  # 車の画像を左右反転
    kt_rct = kt_img.get_rect()  # 車の画像の矩形（Rect）オブジェクトを取得
    kt_rct.center = 300, 530  # 車の矩形オブジェクトの中心を設定
    blinker_timer = 0  # ウインカーのタイマーを初期化
    brake_timer = 0  # ブレーキランプのタイマーを初期化
    blinker_direction = None  # ウインカーの方向を初期化
    brake_timer = 0  # ブレーキランプのタイマーを初期化
    down_key_start_time = None  # 下キーが押され始めた時間を初期化

    while True:
        #key_lst = pg.key.get_pressed()  # 押されているキーのリストを取得
        for event in pg.event.get():  # イベントキューからイベントを取得
            if event.type == pg.QUIT: return  # ウィンドウの閉じるボタンが押されたら終了
        key_lst = pg.key.get_pressed()  # 押されているキーのリストを取
        kx = 0  # x方向の移動量を初期化
        if key_lst[pg.K_DOWN]:  # 下矢印キーが押されたら
            
            brake_timer = 40
            # 下キーが押され始めた時間を記録
            if down_key_start_time is None:
                down_key_start_time = time.time()
            #elif time.time() - down_key_start_time >= 1:
                
        else:
            down_key_start_time = None

        if key_lst[pg.K_LEFT]:  # 左矢印キーが押されたら
            blinker_direction = "left"  # ウインカーの方向を設定
            blinker_timer += 1  # ウインカーのタイマーを増加
        elif key_lst[pg.K_RIGHT]:  # 右矢印キーが押されたら
            blinker_direction = "right"  # ウインカーの方向を設定
            blinker_timer += 1  # ウインカーのタイマーを増加
        else:
            blinker_timer = 0

        kt_rct.move_ip(kx, 0)  # 車の矩形オブジェクトを移動

        idoukyori += 5
        idoukyori %= sizey
        screen.blit(bg_img, [0, idoukyori])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 1])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 2])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 3])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 4])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 5])  # 背景画像をスクリーンに描画
        screen.blit(kt_img, kt_rct)  # 車の画像をスクリーンに描画

        clock.tick(framerate)  # フレームレートを設定

        if blinker_timer > 0:  # ウインカーのタイマーが0より大きい場合
            if blinker_timer % 80 < 40:  # 0.4秒間隔でウインカーを点滅させる
                draw_blinker(screen, kt_rct, blinker_direction)  # ウインカーを描画

        if brake_timer > 0:
            draw_brake_lamp(screen, kt_rct)
            brake_timer -= 1

        pg.display.update()
        tmr += 1
        clock.tick(framerate)
if __name__ == "__main__":
    pg.init()  # Pygameを初期化
    main()  # メイン関数を実行
    pg.quit()  # Pygameを終了
    sys.exit()  # プログラムを終了