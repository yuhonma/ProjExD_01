import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230418/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01-20230418/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imgs = [kk_img,pg.transform.rotozoom(kk_img, 3.3, 1.0),pg.transform.rotozoom(kk_img, 6.6, 1.0),
               pg.transform.rotozoom(kk_img, 10, 1.0),pg.transform.rotozoom(kk_img, 6.6, 1.0),pg.transform.rotozoom(kk_img, 3.3, 1.0)]

    


    tmr = 0
    x = 1

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x += 1
        if x >= 1599:
            x = 1
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [-x+1600, 0])

        screen.blit(kk_imgs[(tmr//5)%6],[300,200])


        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()