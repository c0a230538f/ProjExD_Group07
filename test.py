import os  # OS関連の機能を提供するモジュールをインポート
import sys  # システム関連の機能を提供するモジュールをインポート
import pygame as pg #Pygameモジュールをpgという名前でインポート
import math # 数学関連の機能を提供するモジュールをインポート
import time # 時間関連の機能を提供するモジュールをインポート
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # スクリプトのディレクトリにカレントディレクトリを変更

def draw_blinker(screen, kt_rct, direction):  # ウインカーを描画する関数を定義
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
    brake_lamp_color = (255, 0, 0)  # ブレーキランプの色を赤色に設定
    brake_lamp_size = (20, 10)  # ブレーキランプのサイズを設定
    brake_lamp_positions = [  # ブレーキランプの位置を設定
        (kt_rct.left, kt_rct.bottom - brake_lamp_size[1]),
        (kt_rct.right - brake_lamp_size[0], kt_rct.bottom - brake_lamp_size[1])
    ]
    for pos in brake_lamp_positions:
        pg.draw.rect(screen, brake_lamp_color, (*pos, *brake_lamp_size))  # ブレーキランプを描画

def ending(screen: pg.Surface, WIDTH: int, HEIGHT: int, max_speed: int, elapsed_time: int, distance: int):
    """
    ゲームオーバー画面を表示する
    引数: screen, WIDTH, HEIGHT, max_speed, elapsed_time, distance
    戻り値: なし
    """
    background = pg.Surface(screen.get_size())#画面と同じサイズのSurfaceを作成
    
    pg.draw.rect(background, (0, 0, 0), (0,0,WIDTH, HEIGHT))#黒色の背景を描画
    pg.Surface.set_alpha(background, 100)#透明度を100に設定
    screen.blit(background, (0, 0))#背景を画面に描画
    font = pg.font.Font(None, 80)#フォントを作成
    moji = font.render("GAME OVER", True, (255, 0, 0))#文字の内容と色を指定
    screen.blit(moji, [WIDTH/2 - 265, HEIGHT/2])#文字を画面に描画


    font_small = pg.font.Font(None, 36)
    max_speed_text = font_small.render(f"Max Speed: {max_speed} km/h", True, (255, 255, 255))
    elapsed_time_text = font_small.render(f"Time: {elapsed_time} s", True, (255, 255, 255))
    distance_text = font_small.render(f"Distance: {distance} km", True, (255, 255, 255))

    screen.blit(max_speed_text, (WIDTH // 2 - 100, HEIGHT // 2 -50))
    screen.blit(elapsed_time_text, (WIDTH // 2 - 100, HEIGHT // 2 - 100))
    screen.blit(distance_text, (WIDTH // 2 - 100, HEIGHT // 2 - 150))
    pg.display.update()
    time.sleep(10)#5秒間待つ
    pg.quit()#Pygameを終了

def coment1(screen: pg.surface,yoko,tate, start_time):
    font = pg.font.Font(None, 120)#フォントを作成
    moji = font.render("ABS", True, (255, 0, 0))#文字の内容と色を指定
    screen.blit(moji, [yoko, tate])#文字を画面に描画
    pg.display.update()
    return start_time + 3


def main():
    sizex = 600
    sizey = 800
    pg.display.set_caption("走り切れ新四号国道！")  # ウィンドウのキャプションを設定
    screen = pg.display.set_mode((600, 800))  # ウィンドウのサイズを設定し、スクリーンサーフェースを作成
    clock  = pg.time.Clock()  # クロックオブジェクトを作成し、時間管理を行う
    bg_img = pg.image.load("fig/tuujyou_miti3.jpg")  # 背景画像をロード
    bg_img = pg.transform.scale(bg_img, (sizex, sizey))  # 背景画像のサイズを変更
    fire_img = pg.image.load("fig/fire.png")  # 爆発画像をロード
    fire_img = pg.transform.scale(fire_img, (500, 500))  # 爆発画像のサイズを変更
    kt_img = pg.image.load("fig/car1.png")  # 車の画像をロード
    kt_img = pg.transform.scale(kt_img, (100, 200))  # 車の画像のサイズを変更
    kt_img = pg.transform.flip(kt_img, True, False)  # 車の画像を左右反転

    kt_rct = kt_img.get_rect()  # 車の画像の矩形（Rect）オブジェクトを取得
    kt_rct.center = 300, 530  # 車の矩形オブジェクトの中心を設定
    font = pg.font.Font(None, 50)  #速度計のフォント
    
    tmr = 0  # タイマーを初期化
    e = 0 #車の運動エネルギー
    sokudo = 0 #車の速度の初期値
    power = 100#車のパワー
    idoukyori = 0
    blinker_timer = 0  # ウインカーのタイマーを初期化
    blinker_direction = None  # ウインカーの方向を初期化
    blinker_state = False  # ウインカーの状態を初期化
    framerate = 200
    brake_timer = 0  # ブレーキランプのタイマーを初期化
    explosion_migi = False  # 右の爆発の状態を初期化
    explosion_hidari = False  # 左の爆発の状態を初期化
    max_speed = 0  # 最高速度を初期化
    distance = 0  # 走った距離を初期化
    down_key_start_time = None  # 下キーが押され始めた時間を初期化
    brake_marks = []  # ブレーキ痕のリストを初期化
    
    while True:
        for event in pg.event.get():  # イベントキューからイベントを取得
            if event.type == pg.QUIT: return  # ウィンドウの閉じるボタンが押されたら終了
        
        #速度が一定になるまでは緩やかに加速
        if sokudo < (80*math.log(power, 280)):
            a = 0.00000001+(sokudo)/(80*math.log(power, 280))
            power2 = power*a
        else:
            power2 = power

            
        key_lst = pg.key.get_pressed()  # 押されているキーのリストを取得

        kx = 0  # x方向の移動量を初期化

        if key_lst[pg.K_UP]:  # 上矢印キーが押されたら
            e += power2 #車の持つエネルギーを加算し続ける
        elif key_lst[pg.K_DOWN]:  # 下矢印キーが押されたら
            e -= power2*3 #車の持つエネルギーを減らす
            
            if e < 0:
                e = 0
            brake_timer = 40
            # 下キーが押され始めた時間を記録
            if down_key_start_time is None:
                down_key_start_time = time.time()
            elif time.time() - down_key_start_time >= 1:
                # 下キーが3秒間押され続けた場合に実行する処理
                if sokudo > 0:
                    coment1(screen, 100, 100, time.time())
            
                #down_key_start_time = None  # 処理を実行した後にリセット
        else:
            down_key_start_time = None

        if key_lst[pg.K_LEFT]:  # 左矢印キーが押されたら
            if sokudo > 0.5:
                if sokudo < 25:
                    kx = -1-(sokudo/25)*2
                else:
                    kx = -3
            if key_lst[pg.K_DOWN]:
                kx *= 0.7
            blinker_direction = "left"  # ウインカーの方向を設定
            blinker_timer += 1  # ウインカーのタイマーを増加
        elif key_lst[pg.K_RIGHT]:  # 右矢印キーが押されたら
            if sokudo > 0.5:
                if sokudo < 25:
                    kx = 1+(sokudo/25)*2
                else:
                    kx = 3
            if key_lst[pg.K_DOWN]:
                kx *= 0.7
            blinker_direction = "right"  # ウインカーの方向を設定
            blinker_timer += 1  # ウインカーのタイマーを増加
        else:
            blinker_timer = 0
        
        if sokudo > max_speed:
            max_speed = sokudo  # 最高速度を更新
        #車への空気抵抗、最大速度が決まる
        if sokudo > 0:
            e -= (10*((1.014)**sokudo))-10
            if e < 0:
                e = 0
        #車の持つエネルギーを速度に変換する
        sokudo = math.sqrt(e)/4
        if sokudo < 0:
            sokudo = 0
        
        
 
        kt_rct.move_ip(kx, 0)  # 車の矩形オブジェクトを移動

        # 壁に衝突したかどうかを判定
        if kt_rct.right >= screen.get_width():
            explosion_migi = True  # 爆発の状態を設定

        elif kt_rct.left <= 0:
            explosion_hidari = True

        #ugoki = tmr % size * 5  # 背景画像の移動量を計算
        idoukyori += sokudo/15
        idoukyori %= sizey
        distance += sokudo/3600/(clock.get_fps()+1) # 走った距離を更新

        screen.blit(bg_img, [0, idoukyori])  # 背景画像をスクリーンに描画
    
            
        screen.blit(bg_img, [0, idoukyori - sizey * 1])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 2])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 3])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 4])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 5])  # 背景画像をスクリーンに描画
        screen.blit(kt_img, kt_rct)  # 車の画像をスクリーンに描画


        screen.blit(kt_img, kt_rct)  # 車の画像をスクリーンに描画

        #速度計
        text = font.render(f"{int(sokudo)}km/h", True, (255, 255, 255))
        screen.blit(text, (sizex-150, sizey-50))
        # メーターを描画
        meter_x, meter_y = sizex-sizex/7, sizey-sizey/8  # メーターの中心座標
        meter_radius = sizey/15  # メーターの半径
        meter_angle = -45+(sokudo / 150) * 180  # 速度に応じた角度（0-150km/hを180-45度の位置に変換）
        # メーターの背景円を描画
        pg.draw.circle(screen, (255, 255, 255), (meter_x, meter_y), meter_radius, 2)
        # メーターの針を描画
        needle_length = meter_radius - 10
        needle_x = meter_x + needle_length * math.cos(math.radians(180 - meter_angle))
        needle_y = meter_y - needle_length * math.sin(math.radians(180 - meter_angle))
        pg.draw.line(screen, (255, 0, 0), (meter_x, meter_y), (needle_x, needle_y), 2)

        if blinker_timer > 0:  # ウインカーのタイマーが0より大きい場合
            if blinker_timer % 80 < 40:  # 0.4秒間隔でウインカーを点滅させる
                draw_blinker(screen, kt_rct, blinker_direction)  # ウインカーを描画

        if brake_timer > 0:
            draw_brake_lamp(screen, kt_rct)
            brake_timer -= 1
        # 爆発画像を描画
        if explosion_hidari:
            fire_rct = fire_img.get_rect(midleft=(kt_rct.right - 250, kt_rct.centery))  # 爆発画像の矩形を車の右側に設定
            screen.blit(fire_img, fire_rct.topleft)  # 爆発画像を描画
            ending(screen,sizey,sizex,int(max_speed), tmr // framerate, ("%.3f"%(distance)))
            return
        if explosion_migi:
            fire_rct = fire_img.get_rect(midright=(kt_rct.left + 250, kt_rct.centery))  # 爆発画像の矩形を車の左側に設定
            screen.blit(fire_img, fire_rct.topleft)  # 爆発画像を描画
            ending(screen,sizey,sizex,int(max_speed), tmr // framerate, ("%.3f"%(distance)))
            return
        #0-400計測
        #if distance >= 0.4:
        #   ending(screen,sizey,sizex,int(max_speed), tmr // framerate, ("%.3f"%(distance)))
        pg.display.update()  # 画面を更新
        tmr += 1  # タイマーを更新
        clock.tick(framerate)  # フレームレートを設定

if __name__ == "__main__":
    pg.init()  # Pygameを初期化
    main()  # メイン関数を実行
    pg.quit()  # Pygameを終了
    sys.exit()  # プログラムを終了