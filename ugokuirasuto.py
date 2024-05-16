import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))
img1 = pg.image.load("images/流れ星.jpg")
img1 = pg.transform.scale(img1, (200, 200))
myrect = pg.Rect(100,500,50,50)

# 2.この下をずっとループする
while True:
    # 3.画面を初期化する
    screen.fill(pg.Color("WHITE"))
    # 5.絵を描いたり、判定したりする
    myrect.x = myrect.x + 5
    myrect.y = myrect.y - 5
    screen.blit(img1, myrect)
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()