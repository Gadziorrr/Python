class Rectangle:
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def __str__(self):
        return f"{type(self).__name__}\n" \
               f"długość: {self.length}\n" \
               f"wysokość: {self.height} \n" \
               f"pole: {self.area}"

    @property
    def area(self):
        return self.length * self.height

    def __repr__(self):
        return f"{type(self).__name__}"


rect = Rectangle(5, 6)
print(rect.__dict__)

