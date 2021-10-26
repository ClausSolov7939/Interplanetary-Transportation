key=pg.key.get_pressed()
if key[pg.K_UP]: sq2.y-=1
elif key[pg.K_DOWN]: sq2.y+=1
if key[pg.K_RIGHT]: sq2.x+=1
elif key[pg.K_LEFT]: sq2.x-=1

sq1.update(root)
sq2.update(root)