class Ball:

    def __init__(self, mass):
        self.mass = mass
        self.image = 'hexagon'
        self.x = 0
        self.y = 0
    def drop(self):
        print('Я подбросился')
        self.y = 2
    def kick(self):
        print('Я пнулся')
        self.x += 1
    def fail(self):
        self.mass = mass - 0.1

ball = Ball(0.5)
ball.drop()
ball.kick()
print(ball.y)
print(ball.x)
print(ball.mass)