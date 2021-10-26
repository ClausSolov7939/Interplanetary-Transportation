class Square():
    def __init__(self, x,y, size, color):
        self.x=x
        self.y=y
        self.size=size
        self.color=color
    def update(self, root):
        pg.draw.rect(root, self.color, (self.x, self.y, self.size, self.size))
sq1=Square(0,0,4,(255,0,0))

sq2=Square(50,60,50,(255,0,255))
