import os  # OS関連の機能を提供するモジュールをインポート
import sys  # システム関連の機能を提供するモジュールをインポート
import pygame as pg #Pygameモジュールをpgという名前でインポート
import time # 時間関連の機能を提供するモジュールをインポート
import random # 乱数関連の機能を提供するモジュールをインポート
import math # 数学関連の機能を提供するモジュールをインポート
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # スクリプトのディレクトリにカレントディレクトリを変更

# スピードメーターを描画するクラス
class Speedometer:
    def __init__(self, screen:pg.display, sizex:int, sizey:int):
        self.screen = screen # スクリーンサーフェースを設定
        self.sizex = sizex # ウィンドウの幅を設定
        self.sizey = sizey # ウィンドウの高さを設定
        self.meter_x = sizex - sizex / 7 # メーターのx座標を設定
        self.meter_y = sizey - sizey / 11 # メーターのy座標を設定
        self.meter_radius = 100 # メーターの半径を設定

    def draw(self, sokudo:float):
        meter_huti = self.meter_radius//10 # メーターの縁の太さ
        meter_angle = -45 + (sokudo / 150) * 180  # 速度に応じた角度（0-150km/hを180-45度の位置に変換）
        # メーターの縁を描画
        pg.draw.circle(self.screen, (50, 50, 50), (self.meter_x, self.meter_y), self.meter_radius, meter_huti) # メーターの背景円を描画
        # メーターの内側を透明にする
        transparent_surface = pg.Surface((self.meter_radius * 2, self.meter_radius * 2), pg.SRCALPHA) # 透明なサーフェスを作成
        pg.draw.circle(transparent_surface, (0, 0, 10, 50), (self.meter_radius, self.meter_radius), self.meter_radius - meter_huti) # 透明な円を描画
        self.screen.blit(transparent_surface, (self.meter_x - self.meter_radius+1, self.meter_y - self.meter_radius + 1)) # 透明な円をスクリーンに描画
        # メーターの内側円を描画(デザイン用)
        pg.draw.circle(self.screen, (100, 100, 255), (self.meter_x, self.meter_y), self.meter_radius - meter_huti + 1, self.meter_radius//30) # メーターの内側円を描画
        # メーターのメモリを描画
        for i in range(-44, 226, 24):  # 0度から180度まで24度刻みでメモリを描画
            angle = 180 - i # 角度を計算
            start_x = self.meter_x + (self.meter_radius - meter_huti - self.meter_radius//20) * math.cos(math.radians(angle)) # メモリの始点のx座標
            start_y = self.meter_y - (self.meter_radius - meter_huti - self.meter_radius//20) * math.sin(math.radians(angle)) # メモリの始点のy座標
            end_x = self.meter_x + (self.meter_radius - meter_huti - self.meter_radius//6) * math.cos(math.radians(angle)) # メモリの終点のx座標
            end_y = self.meter_y - (self.meter_radius - meter_huti - self.meter_radius//6) * math.sin(math.radians(angle)) # メモリの終点のy座標
            pg.draw.line(self.screen, (255, 255, 255), (start_x, start_y), (end_x, end_y), 2) # メモリを描画
        # メーターの細かなメモリを描画
        for i in range(-44, 225, 6):  # 0度から180度まで6度刻みで細かなメモリを描画
            angle = 180 - i # 角度を計算
            start_x = self.meter_x + (self.meter_radius - meter_huti - self.meter_radius//20) * math.cos(math.radians(angle)) # メモリの始点のx座標
            start_y = self.meter_y - (self.meter_radius - meter_huti - self.meter_radius//20) * math.sin(math.radians(angle)) # メモリの始点のy座標
            end_x = self.meter_x + (self.meter_radius - meter_huti - self.meter_radius//10) * math.cos(math.radians(angle)) # メモリの終点のx座標
            end_y = self.meter_y - (self.meter_radius - meter_huti - self.meter_radius//10) * math.sin(math.radians(angle)) # メモリの終点のy座標
            pg.draw.line(self.screen, (255, 255, 255), (start_x, start_y), (end_x, end_y), 1) # メモリを描画
        # メーターの針を描画
        needle_length = self.meter_radius * 0.8 # 針の長さ
        needle_x = self.meter_x + needle_length * math.cos(math.radians(180 - meter_angle)) # 針の先端のx座標
        needle_y = self.meter_y - needle_length * math.sin(math.radians(180 - meter_angle)) # 針の先端のy座標
        pg.draw.line(self.screen, (255, 0, 0), (self.meter_x, self.meter_y), (needle_x, needle_y), 4) # 針を描画
        # メーターの中心に透明な小さい円を描画
        transparent_center = pg.Surface((self.meter_radius//5, self.meter_radius//5), pg.SRCALPHA) # 透明なサーフェスを作成
        pg.draw.circle(transparent_center, (0, 0, 0, 200), (self.meter_radius//10, self.meter_radius//10), self.meter_radius//10) # 透明な円を描画
        self.screen.blit(transparent_center, (self.meter_x - self.meter_radius//10 + self.meter_radius//40, self.meter_y - self.meter_radius//13)) # 透明な円をスクリーンに描画
        # 速度計の数値をメーター内に表示
        font = pg.font.Font(None, int(self.meter_radius/3))  # 速度計のフォント
        text = font.render(f"{int(sokudo)}km/h", True, (255, 255, 255))  # 速度計の文字列を作成
        text_rect = text.get_rect(center=(self.meter_x + self.meter_radius//80, self.meter_y + self.meter_radius - self.meter_radius//3))  # 文字列の位置を設定
        self.screen.blit(text, text_rect)  # 速度計の文字列をスクリーンに描画


def cal_power(sokudo:float, power:int):
    """
    車のパワーを計算する関数
    速度に応じて車のパワーを変化させる
    sokudo: 車の速度
    power: 車のパワー
    """
    #速度が一定になるまでは緩やかに加速
    if sokudo < (80*math.log(power, 280)):
        a = 0.00000001+(sokudo)/(80*math.log(power, 280)) #速度が80になるまでは、0.???倍のパワーになる
        power2 = power*a
    else: #速度が80を超えたら、パワーを一定にする
        power2 = power

    return power2

def cal_speed(sokudo:float, energy:float):
    """
    車の速度を計算する関数
    速度に応じて車の持つエネルギーを空気抵抗として減少させ、エネルギーを速度に変換する。
    sokudo: 車の速度
    energy: 車の持つエネルギー
    """
    #車への空気抵抗、最大速度が決まる
    if sokudo > 0:
        energy -= (10*((1.014)**sokudo))-10
        if energy < 0:
            energy = 0
    #車の速度が12km/h以下の場合は、クリープ現象を再現する
    if sokudo < 12.3:
        energy += random.randint(0, 4)
    #車の持つエネルギーを速度に変換する
    sokudo = math.sqrt(energy)/4
    if sokudo < 0:
        sokudo = 0
    return energy, sokudo



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


class CarLights:
    def __init__(self):
        self.blinker_timer = 0
        self.brake_timer = 0
        self.blinker_direction = None

    def draw_blinker(self, screen, kt_rct, direction):
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
            pg.draw.rect(screen, blinker_color, (*pos, *blinker_size))  # ウインカーを描画

    def draw_brake_lamp(self, screen, kt_rct):
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
    sizex = 600  # ウィンドウの幅を設定
    sizey = 800  # ウィンドウの高さを設定
    framerate = 200  # フレームレートを設定
    idoukyori = 0
    energy = 0 # 車のエネルギー(速度の算出に使用)
    sokudo = 0 # 速度の初期値
    power = 300 # 車のパワー

    pg.display.set_caption("こうかとんをよけろ！")  # ウィンドウのキャプションを設定
    screen = pg.display.set_mode((sizex, sizey))  # ウィンドウのサイズを設定し、スクリーンサーフェースを作成
    clock = pg.time.Clock()  # クロックオブジェクトを作成し、時間管理を行う
    tmr = 0  # タイマーを初期化
    bg_img = pg.image.load("fig/tuujyou_miti3.jpg")  # 背景画像をロード
    bg_img = pg.transform.scale(bg_img, (sizex, sizey))  # 背景画像のサイズを変更
    kt_img = pg.image.load("fig/car1.png")  # 車の画像をロード
    kt_img = pg.transform.scale(kt_img, (100, 200))  # 車の画像のサイズを変更
    kt_img = pg.transform.flip(kt_img, True, False)  # 車の画像を左右反転
    kt_rct = kt_img.get_rect()  # 車の画像の矩形（Rect）オブジェクトを取得
    kt_rct.center = 300, 530  # 車の矩形オブジェクトの中心を設定
    car_lights = CarLights()  # CarLightsクラスのインスタンスを作成
    down_key_start_time = None  # 下キーが押され始めた時間を初期化
    kks = [] #こうかとんのリスト
    spawn_timer = 600 #こうかとんが出現する頻度
    
    while True:
        for event in pg.event.get():  # イベントキューからイベントを取得
            if event.type == pg.QUIT: return  # ウィンドウの閉じるボタンが押されたら終了

        key_lst = pg.key.get_pressed()  # 押されているキーのリストを取得
        if key_lst[pg.K_UP]:  # 上矢印キーが押されたら    
            energy += cal_power(sokudo, power) #車の持つエネルギーを加算し続ける
        elif key_lst[pg.K_DOWN]:  # 下矢印キーが押されたら
            energy -= cal_power(sokudo, power)*2 #車の持つエネルギーを減らす
            if energy < 0:
                energy = 0
            car_lights.brake_timer = 40
            # 下キーが押され始めた時間を記録
            if down_key_start_time is None:
                down_key_start_time = time.time()
        else:
            down_key_start_time = None
        
        if key_lst[pg.K_LEFT]:  # 左矢印キーが押されたら
            car_lights.blinker_direction = "left"  # ウインカーの方向を設定
            car_lights.blinker_timer += 1  # ウインカーのタイマーを増加
        elif key_lst[pg.K_RIGHT]:  # 右矢印キーが押されたら
            car_lights.blinker_direction = "right"  # ウインカーの方向を設定
            car_lights.blinker_timer += 1  # ウインカーのタイマーを増加
        else:
            car_lights.blinker_timer = 0


        #車速度を計算
        cal = cal_speed(sokudo, energy) #空気抵抗を計算し、車の持つエネルギーを速度に変換する
        energy = cal[0]#車の持つエネルギーを更新
        sokudo = cal[1] #車の速度を更新

        if spawn_timer < 0:  # 120フレームごとにこうかとんを生成
            kks.append(Bird())
            spawn_timer = 600
        spawn_timer -= 5
        

        for obj in kks[:]:
            obj.update(5)
           # if obj.rect.colliderect( ): #車の変数を入れる
                 # 衝突したらゲームオーバー
            if obj.off_screen(sizey):
                kks.remove(obj)


        #背景画像を描画
        idoukyori += sokudo/20 # 背景画像の移動量を計算
        idoukyori %= sizey
        screen.blit(bg_img, [0, idoukyori])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 1])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 2])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 3])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 4])  # 背景画像をスクリーンに描画
        screen.blit(bg_img, [0, idoukyori - sizey * 5])  # 背景画像をスクリーンに描画
        screen.blit(kt_img, kt_rct)  # 車の画像をスクリーンに描画
        speedometer = Speedometer(screen, sizex, sizey) # Speedometerクラスを使用
        speedometer.draw(sokudo) # スピードメーターを描画
        
        for obj in kks:
            obj.draw(screen)

        

        if car_lights.blinker_timer > 0:  # ウインカーのタイマーが0より大きい場合
            if car_lights.blinker_timer % 80 < 40:  # 0.4秒間隔でウインカーを点滅させる
                car_lights.draw_blinker(screen, kt_rct, car_lights.blinker_direction)  # ウインカーを描画

        if car_lights.brake_timer > 0:
            car_lights.draw_brake_lamp(screen, kt_rct)
            car_lights.brake_timer -= 1

        pg.display.update() # 画面を更新
        clock.tick(framerate)  # フレームレートを設定
        pg.display.update()
        tmr += 1


if __name__ == "__main__":
    pg.init()  # Pygameを初期化
    main()  # メイン関数を実行
    pg.quit()  # Pygameを終了
    sys.exit()  # プログラムを終了
