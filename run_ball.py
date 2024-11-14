import turtle
import random

class Ball:
    def __init__(self, xpos, ypos, vx, vy, color, radius):
        self.xpos = xpos
        self.ypos = ypos
        self.vx = vx
        self.vy = vy
        self.color = color
        self.radius = radius

    def draw(self):
        """Draw the ball on the screen."""
        turtle.penup()
        turtle.goto(self.xpos, self.ypos - self.radius)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(self.color)
        turtle.circle(self.radius)
        turtle.end_fill()

    def move(self, dt):
        """Move the ball based on its velocity."""
        self.xpos += self.vx * dt
        self.ypos += self.vy * dt

    def update_velocity(self, canvas_width, canvas_height):
        """Update the ball's velocity if it hits the walls."""
        if abs(self.xpos) + self.radius > canvas_width:
            self.vx = -self.vx
        if abs(self.ypos) + self.radius > canvas_height:
            self.vy = -self.vy

class Simulation:
    def __init__(self, num_balls):
        self.num_balls = num_balls
        self.balls = []
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.create_balls()

    def create_balls(self):
        """Create balls with random positions, velocities, and colors."""
        for _ in range(self.num_balls):
            xpos = random.randint(int(-1 * self.canvas_width + self.ball_radius), int(self.canvas_width - self.ball_radius))
            ypos = random.randint(int(-1 * self.canvas_height + self.ball_radius), int(self.canvas_height - self.ball_radius))
            vx = 2 * random.uniform(-1.0, 1.0)
            vy = 2 * random.uniform(-1.0, 1.0)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            ball = Ball(xpos, ypos, vx, vy, color, self.ball_radius)
            self.balls.append(ball)

    def draw_border(self):
        """Draw the canvas border."""
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for _ in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)

    def run(self):
        """Run the simulation."""
        dt = 1  # time step
        while True:
            turtle.clear()
            self.draw_border()
            for ball in self.balls:
                ball.draw()
                ball.move(dt)
                ball.update_velocity(self.canvas_width, self.canvas_height)
            turtle.update()

# Main execution
num_balls = int(input("Number of balls to simulate: "))
simulation = Simulation(num_balls)
simulation.run()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
