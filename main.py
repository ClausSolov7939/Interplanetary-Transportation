import pygame as pg
from init import *
clock=pg.time.Clock()
game=True
root=pg.display.set_mode((width, height))
run=True
script=False
while game:
    for event in pg.event.get():
        if event.type==pg.QUIT: game=False
        if event.type==pg.KEYDOWN and event.key==pg.K_s:
            script=True; run=True

    root.fill((128,128,128))
    if run==True and script:
        try: exec(open('setup.py').read())
        except Exception as e: print(e); script=False
        finally: run=False
    if script:
        try: exec(open('loop.py').read())
        except Exception as e: print(e); script=False
#    finally: print()#; run=False

    pg.display.update()
    clock.tick(60)
pg.quit()