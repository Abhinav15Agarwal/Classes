#Classes - Classes are used to define new types eg - shopping basket

# The first letter will be capital since wew are following Pascal's naming conventions
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Point(10,20)
print(point1.x)
#Objects are the instance of a class