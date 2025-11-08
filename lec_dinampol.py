class Ball:

    def __init__(self, mass):

        self.mass = mass
        self.image = 'hexagon'

ball = Ball(0.5)

print(ball.image)
print(ball.mass)
ball.image = 'lines'
print(ball.image)
