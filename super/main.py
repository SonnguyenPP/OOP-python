class Shape:
     def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color,is_filled)
        self.radius = radius
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color,is_filled)
        self.width = width

circle = Circle(color="red",is_filled=True, radius=6)
square = Square(color="blue",is_filled=True, width=5)

print(circle.color)
