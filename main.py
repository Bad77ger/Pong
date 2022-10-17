from pygame import*
dw = 900
dh = 600
window = display.set_mode((dw, dh))
display.set_caption("Ping Pong")


class GameSprite(sprite.Sprite):
    def __init__(self,filename,w,h,x,y,speed):
        super().__init__()
        self.image =transform.scale(image.load(filename), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        k = key.get_pressed()
        if k[K_UP]:
            self.rect.y -= self.speed
        if k[K_DOWN]:
            self.rect.y += self.speed


ball = GameSprite("ball2.png", 40, 40, 425, 260, 5)
racket_left = Player("left4.png", 20, 100, 10, 225, 10)
racket_right= Player("right4.png", 20, 100, 850, 225, 10)


run=True
while run:
    for e in event.get():
        if e.type == QUIT:
            run=False

    window.fill((150, 150, 250))
    ball.reset()
    racket_left.reset()
    racket_right.reset()

    racket_left.update()
    racket_right.update()

    display.update()
    time.delay(30)