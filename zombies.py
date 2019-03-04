import random

class Zombie:

  max_speed = 5
  max_strength = 8
  horde = []
  plague_level = 10
  default_speed = 1
  default_strength = 3

  def __init__(self, speed, strength):
    """Initializes zombie's speed and strength
    """
    if speed > Zombie.max_speed:
      self.speed = Zombie.default_speed
    else:
      self.speed = speed


    if strength > Zombie.max_strength:
        self.strength = Zombie.default_strength
    else:
        self.strength = strength


  def __str__(self):
    return "This zombie has a speed of {} and a strength of {}.".format(self.speed,self.strength)


  @classmethod
  def spawn(cls):
    """Spawns a random number of new zombies, based on the plague level,
    adding each one to the horde.  Each zombie gets a random speed.
    """
    new_zombies = random.randint(1, Zombie.plague_level)
    count = 0

    while count < new_zombies:
      speed = random.randint(1, Zombie.max_speed)
      strength = random.randint(1, Zombie.max_strength)
      Zombie.horde.append(Zombie(speed,strength))
      count += 1

  @classmethod
  def new_day(cls):
    """Represents the events of yet another day of the zombie apocalypse.
    Every day some zombies die off (phew!), some new ones show up,
    and sometimes the zombie plague level increases.
    """
    Zombie.spawn()
    Zombie.some_die_off()
    Zombie.increase_plague_level()

  @classmethod
  def some_die_off(cls):
    """Removes a random number (between 0 and 10) of zombies from the horde.
    """
    how_many_die = random.randint(0, 10)
    counter = 0
    while counter < how_many_die and len(Zombie.horde) > 0:
      random_zombie = random.randint(0,len(Zombie.horde) - 1)
      Zombie.horde.pop(random_zombie)
      counter += 1


  @classmethod
  def increase_plague_level(cls):
    """ Zombie.plague_level is increased by a random number between 0 and 2. """
    plague_increase = random.randint(0, 2)
    Zombie.plague_level += plague_increase
    return Zombie.plague_level



  def encounter(self):
    """This instance method represents you coming across a zombie! This can end in two possible outcomes:
    1. You outrun the zombie and escape unscathed!
    2. You don't outrun the zombie. If you don't, you end up fighting it
    3. If you win the fight, you still catch the zombie plague and turn into a zombie
    4. If you lose the fight, it eats your brains and you die. :(
    Returns a summary of what happened.
    """
    outrun = self.chase()
    win_fight = self.fight()

    if outrun:
        return 'You escaped!'
    elif win_fight:
        new_zombie = Zombie(random.randint(1,Zombie.max_speed),random.randint(1,Zombie.max_strength))
        Zombie.horde.append(new_zombie)
        return 'You fought the zombie and caught the plague.  You are now a zombie too.  Raaaawrgh'
    else:
        return 'You died.'


  def chase(self):
    """Represents you trying to outrun this particular zombie.
    Uses `Zombie.max_speed` to generate a random number that represents how fast you manage to run.
    """
    your_speed = random.randint(1, Zombie.max_speed)
    return your_speed > self.speed

  def fight(self):
    """Represents you trying to fight a zombie.
    """
    your_strength = random.randint(1, Zombie.max_strength)
    return your_strength > self.strength

zombie1 = Zombie(4,3)
print(zombie1)
Zombie.horde.append(zombie1)
print(Zombie.horde)



Zombie.new_day()
print(Zombie.horde) # [<__main__.Zombie object at 0x7f6f594f0d30>, <__main__.Zombie object at 0x7f6f594f0b70>, <__main__.Zombie object at 0x7f6f594f0d68>]
zombie1 = Zombie.horde[0]
print(zombie1) # Speed: 1 -- Strength: 7
zombie2 = Zombie.horde[1]
print(zombie2) # Speed: 2 -- Strength: 7
print(zombie1.encounter()) # You escaped!
print(zombie2.encounter()) # You fought the zombie and caught the plague.  You are now a zombie too.  Raaaawrgh
Zombie.new_day()
print(Zombie.horde) # [<__main__.Zombie object at 0x7f6f594f0d30>, <__main__.Zombie object at 0x7f6f594efef0>, <__main__.Zombie object at 0x7f6f594f0c50>, <__main__.Zombie object at 0x7f6f594f0cc0>]
zombie1 = Zombie.horde[0]
zombie2 = Zombie.horde[1]
print(zombie1.encounter()) # You died!
print(zombie2.encounter()) # You escaped!
