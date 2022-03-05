class Brush:
    NUMBER_OF_BRISTLES = 200
    BRUSH_SIZE = 20
    BRUSH_THICKNESS = 20
    BRUSH_STAGGER = 6

    def __init__(self, painting):
        self.painting = painting
        self.x = 0
        self.y = 0
        self.bristles = list()

        # Brush settings
        self.num_bristles = Brush.NUMBER_OF_BRISTLES
        self.brush_size = Brush.BRUSH_SIZE
        self.max_brush_thickness = Brush.BRUSH_THICKNESS
        self.brush_stagger = Brush.BRUSH_STAGGER

        self.initialize_bristles()

    def initialize_bristles(self):
        for i in range(self.num_bristles):
            bristle_x = random(-self.brush_size, self.brush_size)
            bristle_y = random(-self.brush_size, self.brush_size)
            bristle_radius = random(self.max_brush_thickness)

            self.bristles.append(Brush.Bristle(self, bristle_x, bristle_y, bristle_radius))

    def update(self):
        self.x += ((mouseX - self.x) / self.brush_stagger)
        self.y += ((mouseY - self.y) / self.brush_stagger)

        if self.x < 0:
            self.x = 0
        elif self.x > width:
            self.x = width

        if self.y < 0:
            self.y = 0
        elif self.y > height:
            self.y = height

    def draw(self):
        # Must run whether mouse is pressed or not to keep bristle
        # x/y positions up to date
        for bristle in self.bristles:
            if mousePressed:
                bristle.draw()

            # Must be placed after draw
            bristle.update()

    class Bristle:
        def __init__(self, brush, bx, by, br):
            self.brush = brush
            self.start_x = bx
            self.end_x = bx
            self.start_y = by
            self.end_y = by
            self.radius = br
            self.start_radius = br

        def update(self):
            if self.end_x == (self.brush.x + self.start_x) and \
               self.end_y == (self.brush.y + self.start_y):
                self.radius += 1
            else:
                self.radius = self.start_radius

            self.end_x = self.brush.x + self.start_x
            self.end_y = self.brush.y + self.start_y

        def draw(self):
            pixel = self.brush.painting.get(int(self.end_x), int(self.end_y))
            stroke(pixel)

            if self.end_x == (self.brush.x + self.start_x) and \
               self.end_y == (self.brush.y + self.start_y):
                strokeWeight(self.radius / 50)
                point(self.end_x, self.end_y)
            else:
                distance = dist(self.brush.x + self.start_x, self.brush.y + self.start_y,
                                self.end_x, self.end_y)

                # The bigger the distance, i.e. the faster the mouse is moved,
                # the bigger and more coarse the line width
                strokeWeight((self.radius * distance) / 50)
                line(self.brush.x + self.start_x, self.brush.y + self.start_y,
                     self.end_x, self.end_y)
