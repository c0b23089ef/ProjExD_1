import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))  
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    img = pg.image.load("fig/3.png")
    img = pg.transform.flip(img,True,False)
    img_rct = img.get_rect()
    img_rct.center = 300, 200
    tmr = 0  
    bg_x = 0  
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        bg_x = (bg_x - 1) % 1600  
        screen.blit(bg_img, [bg_x, 0])  
        screen.blit(bg_img, [bg_x - 1600, 0])  
        screen.blit(img, img_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)  

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
