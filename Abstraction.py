class Coordinate(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return ("x: {}, y: {}").format(self.x, self.y)

  def distance(self, other):
    x_diff_sq = (self.x - other.x)**2
    y_diff_sq = (self.y - other.y)**2
    return (x_diff_sq + y_diff_sq)** 0.5

c = Coordinate(3, 4)
origin = Coordinate(0, 0)
print(c.x)
print(origin.y)

d = Coordinate(1,18)
print(d)

print(c.distance(origin))
print(c)

# Animal Class

class Animal:
  def __init__(self, age):
    self.age = age
    self.name = None

  ## Getter methods
  def get_age(self):
    return self.age

  # Setter methods
  def set_age(self, newage):
    self.age = newage
  def set_name(self, newname=""):
    self.name = newname

  def __str__(self):
    return "animal:" + str(self.name) + ":" + str(self.age)

  # Getters and Setters should be used outside the class to access data attributes.

a = Animal(3)
print(a.age)
print(a.get_age())