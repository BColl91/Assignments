from livewires import games, color
import random

games.init(screen_width=640, screen_height=440, fps=50)

class Net(games.Sprite):
    image = games.load_image("Paddle.png")

    def __init__(self):
        super(Net, self).__init__(image=Net.image,
                                  x=games.mouse.x,
                                  bottom=games.screen.height)
        self.score = games.Text(value=0, size=40, color=color.red,
                                top=5, right=games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()

    def check_catch(self):
        for ball in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            ball.handle_caught()

class PingPongBall(games.Sprite):
    image = games.load_image("PingPongBall.png")
    speed = 3

    def __init__(self, x, y=70):
        super(PingPongBall, self).__init__(image=PingPongBall.image,
                                           x=x, y=y,
                                           dx=PingPongBall.speed, dy=PingPongBall.speed)

    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        if self.top < 0:
            self.dy = -self.dy
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        self.dy = -self.dy

    def end_game(self):
        end_message = games.Message(value="Game Over!", size=90,
                                    color=color.yellow,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)

def main():
    court = games.load_image("PingPongTable.gif", transparent=False)
    games.screen.background = court

    ball = PingPongBall(x=320, y=70)
    games.screen.add(ball)

    paddle = Net()
    games.screen.add(paddle)

    games.mouse.is_visible = False
    games.screen.event_grab = True

    games.screen.mainloop()

main()
