import turtle


class L2DF:

    def __init__(self, t, f, color, length, angle):
        self.axiom = f
        self.state = f
        # self.line_color = color
        self.t = t
        self.t.pencolor(color)
        self.rules = {}
        self.length = length
        self.angle = angle

    def drow(self, start_x, start_y):
        turtle.tracer(1, 0)
        self.t.up()
        self.t.goto(start_x, start_y)
        self.t.down()
        for move in self.state:
            if move == "f":
                self.t.fd(self.length)
            elif move == "+":
                self.t.lt(self.angle)
            elif move == "-":
                self.t.rt(self.angle)
            elif move =="s":
                self.t.up()
                self.t.fd(self.length)
                self.t.down()

t = turtle.Turtle()
f = L2DF(t, "f+f--f+f--f+f--f+f--f+f--f+f", "#123726937", 120, 60)
f.drow(-100, -100)
f2 = L2DF(t, "f+s-ff+f+ff+fs+ff", "magenta", 20, 90)
f2.drow(10, 200)
turtle.mainloop()
