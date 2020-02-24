# https://edabit.com/challenge/dLnZLi8FjaK6qKcvv
# Shiritori Game

class Shiritori():
  words = []
  game_over = False
  
  def __init__(self):
    self.words = []
    self.game_over = False

  def play(self, word):
    if len(self.words) == 0 or (self.words[-1][-1] == word[0] and word not in self.words):
      self.words.append(word)
      print(self.words)
    else:
      self.game_over = True
      print("game over")

  def restart(self):
    self.words = []
    self.game_over = False
    print("game restarted")

my_shiritori = Shiritori()

my_shiritori.play("apple") # ["apple"]
my_shiritori.play("ear") # ["apple", "ear"]
my_shiritori.play("rhino") # ["apple", "ear", "rhino"]
my_shiritori.play("corn") # "game over"

# Corn does not start with an "o".

my_shiritori.words # ["apple", "ear", "rhino"]

# Words should be accessible.

my_shiritori.restart # "game restarted"
my_shiritori.words # []

# Words list should be set back to empty.

my_shiritori.play("hostess") # ["hostess"]
my_shiritori.play("stash") # ["hostess", "stash"]
my_shiritori.play("hostess") # "game over"

# Words cannot have already been said.