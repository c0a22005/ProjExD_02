import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1600, 900

delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0)
    }



def check_bound(rct: pg.Rect) ->  tuple[bool, bool]:
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:
        tate = False
    return yoko, tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kkg_img = pg.image.load("ex02/fig/8.png")
    kkg_img = pg.transform.rotozoom(kkg_img, 0, 5.0)
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    
    muki = {(-5, 0): pg.transform.rotozoom(kk_img, 0, 1.0),
            (0,-5): pg.transform.flip(pg.transform.rotozoom(kk_img, -90, 1.0),True, False),
            (+5, -5): pg.transform.flip(pg.transform.rotozoom(kk_img, -45, 1.0),True, False),
            (+5, 0): pg.transform.flip(pg.transform.rotozoom(kk_img, 0, 1.0),True, False),
            (+5, +5): pg.transform.flip(pg.transform.rotozoom(kk_img, 45, 1.0),True, False),
            (0, +5): pg.transform.flip(pg.transform.rotozoom(kk_img, 90, 1.0),True, False),
            (-5, +5): pg.transform.rotozoom(kk_img, 45, 1.0),
            (-5, -5): pg.transform.rotozoom(kk_img, -45, 1.0)
            }
            
    
    kk_rct = kk_img.get_rect()  #練習3 こうかとんsurfaceのrectを抽出
    kk_rct.center = 900, 400 #練習3　こうかとんの初期座標
    bb_img = pg.Surface((20, 20))   #練習1　透明のsurfaceをつくる
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)
    bb_rct = bb_img.get_rect()
    bb_rct.centerx = random.randint(0, WIDTH)
    bb_rct.centery = random.randint(0, HEIGHT)
    vx, vy = +5, +5
    
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        if kk_rct.colliderect(bb_rct):
            kk_img == kkg_img #泣いているこうかとんに変更
            screen.blit(kkg_img,[630,60])  #サイズを拡大
            pg.display.update()
            clock.tick(0.4)
            print("Game Over")
            return
            
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k,tpl in delta.items():
            if key_lst[k]:  #キーが押されたら
                sum_mv[0] += tpl[0] 
                sum_mv[1] += tpl[1]   
            for l, m in muki.items():
                if sum_mv[0] == l[0] and sum_mv[1] == l[1]:
                    kk_img = m
                
                

        screen.blit(bg_img, [0, 0])
        kk_rct.move_ip(sum_mv[0], sum_mv[1])
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(vx, vy)  #練習2　爆弾を移動させる
        yoko, tate = check_bound(bb_rct)
        if not yoko:  #横方向にはみ出たら
            vx *= -1
        if not tate: #縦方向にはみ出たら
            vy *= -1
        screen.blit(bb_img, bb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()