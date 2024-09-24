import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))  
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    mir_bg_img = pg.transform.flip(bg_img,True,False)
    img = pg.image.load("fig/3.png")
    img = pg.transform.flip(img,True,False)
    img_rct = img.get_rect()
    img_rct.center = 300, 200
    kk_rct = img.get_rect() 
    kk_rct.center = 300, 200  
    tmr = 0  
    bg_x = 0  
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        mv_iplst = [-1, 0]
        key_lst = pg.key.get_pressed()  
        if key_lst[pg.K_UP]:  
           mv_iplst[1] += -1 
        if key_lst[pg.K_DOWN]:  
            mv_iplst[1] += 1  
        if key_lst[pg.K_LEFT]:  
            mv_iplst[0] += -1
        if key_lst[pg.K_RIGHT]:  
            mv_iplst[0] += +2

        kk_rct.move_ip(mv_iplst)
        
        bg_x = (bg_x - 1) % 1600  
        screen.blit(bg_img, [bg_x, 0])  
        screen.blit(bg_img, [bg_x - 1600, 0])
        screen.blit(mir_bg_img,[bg_x+1600,0])
        screen.blit(mir_bg_img,[bg_x+4800,0])  
        screen.blit(img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)  

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
