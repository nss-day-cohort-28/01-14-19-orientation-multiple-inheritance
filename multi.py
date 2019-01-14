class Animal:
  def sayAnimal(self):
    return "I am an animal"

class AnimalFriend:
  def sayFriend(self):
    return "My friend is Mr. Farmer"

class Cow(Animal, AnimalFriend):
  def sayCowThing(self):
    print(f"{self.sayAnimal()} and {self.sayFriend()}")

# class Lion(Animal): Would not inherit from AnimalFriend

bossie = Cow()
bossie.sayCowThing()
# ======

class Flying:
  def __init__(self):
    self.can_fly = True

  @property
  def wings(self):
    try:
        return self.__wing_count
    except AttributeError:
        return 2

  @wings.setter
  def wings(self, count):
    if isinstance(count, int):
      self.__wing_count = count
    else:
      raise TypeError('Wing count must be a number')

  def fly(self):
    print("I want to fly like an eagle, to the sea. Fly like an eagle, let my spirit carry me.")


class Swimming:
  def __init__(self):
    self.can_swim = True

  def swim(self):
    print("I want to swim like a penguin, in the sea. Swim like a penguin, let my flippers carry me.")

class Running:
  def __init__(self, leg_length):
    self.can_run = True
    self.run_speed = 2.0
    self.leg_length = leg_length

  def run(self):
    if self.leg_length < 10 and self.run_speed <= 2.0:
      return "I'm waddling as fast as I can."
    elif self.leg_length < 20:
      return "I'm running now, but get closer and I'll fly instead."
    else:
      return "Catch me if you can."

class Bat(Flying):
  def __init__(self, species):
    self.has_feathers = False
    self.species = species
    super().__init__()

class Bird:
  def __init__(self, species, nest="tree"):
    self.has_feathers = True
    self.species = species
    self.nest = nest

  def layEgg(self):
    if self.nest == "tree":
      return("Push! Breathe! Push!")
    else:
      return("Push! Breathe! Watch your step, please!")

class Penguin(Bird, Running, Swimming):

  def __init__(self, species, nest="ground", leg_length=5):
      self.color = "black and white"
      # With multi inheritance, have to use base class name explicitly for init. Super won't work without some extra configuration having to do with Method Resolution Order (MRO). ALso, have to pass 'self' when doing this. super() does that automagically.
      Bird.__init__(self, species, nest)
      Swimming.__init__(self)
      Running.__init__(self, leg_length)

  def __str__(self):
    return f'can_run: {self.can_run}, can_swim: {self.can_swim}, has_feathers: {self.has_feathers}'

emperor_penguin = Penguin("Emperor Penguin")
print("Our running, swimming, feathery penguin", emperor_penguin)

fruity = Bat("fruit")
print(fruity.__dict__)
