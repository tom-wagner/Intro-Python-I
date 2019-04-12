def print_pairs(class_obj):
  for k in class_obj.__dict__:
    print(k, getattr(class_obj, k))

# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon():
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon

  def __str__(self):
    return " - ".join(['{}: {}'.format(k, getattr(self, k)) for k in self.__dict__])

x = LatLon(12, 15)

# print(x.lat, x.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
  def __init__(self, lat, lon, name):
    super().__init__(lat, lon)
    self.name = name

y = Waypoint(12, 15, 'steve')
# print_pairs(y)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
  def __init__(self, lat, lon, name, difficulty, size):
    super().__init__(lat, lon, name)
    self.size = size
    self.difficulty = difficulty
  
z = Geocache(12, 15, 'steve', 'easy', 'big')
# print_pairs(z)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
wp = Waypoint(2131, 2414, "Catacombs")
print(wp)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
# print(geocache)

# SKIPPED