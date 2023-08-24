class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)
        self.name = "square"


s1 = Square(4)
s1.show_attributes()
