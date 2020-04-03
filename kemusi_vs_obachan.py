
import pygame
from pygame.locals import *
import sys
import random

# parameterの設定
(w,h)=(400,600)                   # スクリーンの大きさ
obachan_w = 88                    # おばちゃん幅
obachan_h = 100                   # おばちゃん高さ
obachan_x = w/2                   # おばちゃん初期中心 x
obachan_y = h - obachan_h/2       # おばちゃん初期中心 y
kemushi_w = 45                    # けむし幅
kemushi_h = 48                    # けむし高さ
kemushi_x = random.randint(0, w)  # 毛虫中心x座標
kemushi_y = 100                   # 毛虫中心y座標
kemushi_x6 = random.randint(0, w) # 毛虫中心x座標
kemushi_y6 = 100                  # 毛虫中心y座標
collision = 65                    # 衝突距離
score = 0                         # スコア
kemusi_speed_min = 5
kemusi_speed_max = 15
count = 0

game_mode = 0                  # Game mode(0:スタート画面 1:プレイ中 2:Game Over)

pygame.init()
window = pygame.display.set_mode((w,h))         #画面の大きさ
screen=pygame.display.get_surface()
pygame.display.set_caption("おばちゃん VS けむし")     #タイトルを設定

# playerの設定
# おばちゃん右向き
player1=pygame.image.load("th.jpg").convert_alpha()
rect_player1=player1.get_rect()
rect_player1.center=(obachan_x,obachan_y)

# おばちゃん右向き
player2=pygame.image.load("th2.jpg").convert_alpha()
rect_player2=player2.get_rect()
rect_player2.center=(obachan_x,obachan_y)

# けむし
player3=pygame.image.load("kemusi.jpg").convert_alpha()
rect_player3=player3.get_rect() 
rect_player3.center=(kemushi_x, kemushi_y)
dy_kemushi = random.randint(kemusi_speed_min, kemusi_speed_max) 

# けむし
player6=pygame.image.load("kemusi.png").convert_alpha()
rect_player6=player6.get_rect() 
rect_player6.center=(kemushi_x6, kemushi_y6)
dy_kemushi6 = random.randint(kemusi_speed_min, kemusi_speed_max) 

# おばちゃんオコ
player4=pygame.image.load("obachan_out2.png").convert_alpha()
rect_player4=player4.get_rect()
rect_player4.center=(obachan_x,obachan_y)

# おばちゃんスタート
player5=pygame.image.load("obachan_start.png").convert_alpha()
rect_player5=player5.get_rect()
rect_player5.center=(w/2,h/2)

player=player1
rect_player=rect_player1



# fontの設定
font = pygame.font.Font(None, 55)

# def main():
while(1):
    pressed_key=pygame.key.get_pressed()        #すべてのキーの入力を取得
    if game_mode == 0:

        start_text = font.render("START",True,(0,0,255))
        start_inst = font.render("PUSH SPACE",True,(0,0,255))
        window.blit(start_text,(140,300)) 
        count = count + 1
        if ((count % 4) != 1): 
            window.blit(start_inst,(85,400))
    
        pygame.display.update()             # 画面の更新
        pygame.time.wait(30)                # 更新間隔
        screen.fill((255,255,255,0))
        screen.blit(player5,rect_player5)
        
        if pressed_key[K_SPACE]:
            rect_player3.move_ip(0,-700)
            kemushi_y = kemushi_y - 700
            kemushi_x2 = random.randint(0, w)
            dx_kemushi = kemushi_x2 - kemushi_x
            rect_player3.move_ip(dx_kemushi, 0)
            kemushi_x = kemushi_x2
            dy_kemushi = random.randint(kemusi_speed_min, kemusi_speed_max)

            rect_player6.move_ip(0,-700)
            kemushi_y6 = kemushi_y6 - 700
            kemushi_x7 = random.randint(0, w)
            dx_kemushi6 = kemushi_x7 - kemushi_x6
            rect_player6.move_ip(dx_kemushi6, 0)
            kemushi_x6 = kemushi_x7
            dy_kemushi6 = random.randint(kemusi_speed_min, kemusi_speed_max)

            score = 0
            game_mode = 1

    else:    
        if game_mode == 1:
            # おばちゃんの移動
            if pressed_key[K_LEFT]:
                obachan_x=obachan_x-20
                player=player1
                if obachan_x>=0:
                    rect_player1.move_ip(-20,0)      #obachan_x方向にマイナス１
                    rect_player2.move_ip(-20,0)      #obachan_x方向にマイナス１
                    rect_player4.move_ip(-20,0)
                if obachan_x<0:
                    obachan_x=w
                    rect_player1.move_ip(w,0)        #obachan_x方向にマイナス１
                    rect_player2.move_ip(w,0)        #obachan_x方向にマイナス１
                    rect_player4.move_ip(w,0)        #obachan_x方向にマイナス１
                rect_player=rect_player1
                
            if pressed_key[K_RIGHT]:
                obachan_x=obachan_x+20
                player=player2
                if obachan_x<=w:
                    rect_player1.move_ip(20,0)
                    rect_player2.move_ip(20,0)
                    rect_player4.move_ip(20,0)
                if obachan_x>w:
                    obachan_x=0
                    rect_player1.move_ip(-w,0)
                    rect_player2.move_ip(-w,0)
                    rect_player4.move_ip(-w,0)
                rect_player=rect_player2

            rect_player3.move_ip(0,dy_kemushi)
            kemushi_y = kemushi_y + dy_kemushi
            dy_kemushi = dy_kemushi

            
            rect_player6.move_ip(0,dy_kemushi6)
            kemushi_y6 = kemushi_y6 + dy_kemushi6
            dy_kemushi6 = dy_kemushi6
            
            # けむしの移動
            if kemushi_y > 700:
                rect_player3.move_ip(0,-700)
                kemushi_y = kemushi_y - 700
                kemushi_x2 = random.randint(0, w)
                dx_kemushi = kemushi_x2 - kemushi_x
                rect_player3.move_ip(dx_kemushi, 0)
                kemushi_x = kemushi_x2
                dy_kemushi = random.randint(kemusi_speed_min, kemusi_speed_max)
                score = score + 10
                
            if kemushi_y6 > 700:
                rect_player6.move_ip(0,-700)
                kemushi_y6 = kemushi_y6 - 700
                kemushi_x7 = random.randint(0, w)
                dx_kemushi6 = kemushi_x7 - kemushi_x6
                rect_player6.move_ip(dx_kemushi6, 0)
                kemushi_x6 = kemushi_x7
                dy_kemushi6 = random.randint(kemusi_speed_min, kemusi_speed_max)
                score = score + 10

            # おばちゃんとけむしの距離を算出
            distance = ((obachan_x - kemushi_x)**2 + (obachan_y - kemushi_y)**2)**0.5
            distance2 = ((obachan_x - kemushi_x6)**2 + (obachan_y - kemushi_y6)**2)**0.5
    
            # GAME OVER
            if ((distance < collision) or (distance2 < collision)):
                game_mode = 2
        
        # GAME OVER を画面表示
        if game_mode == 2:
            player=player4
            rect_player=rect_player4
            end_text = font.render("GAME OVER",True,(255,0,0))
            restart_inst = font.render("PUSH TAB",True,(0,0,255))
            window.blit(end_text,(85,200))
            count = count + 1
            if ((count % 4) != 1): 
                window.blit(restart_inst,(100,300))

            if pressed_key[K_TAB]:
                game_mode = 0
                player=player1
                rect_player=rect_player1

        # 座標を表示
        text = font.render(str(score), True, (0,255,255))
        screen.blit(text, [20, 60])          

        pygame.display.update()             # 画面の更新
        pygame.time.wait(30)                # 更新間隔
        screen.fill((255,255,255,0))
        screen.blit(player3,rect_player3)
        screen.blit(player6,rect_player6)
        screen.blit(player,rect_player)


    for event in pygame.event.get():
        if event.type==QUIT:            #終了イベント
            pygame.quit()
            sys.exit(0)
