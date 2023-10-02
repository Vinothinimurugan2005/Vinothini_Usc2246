class Player:
  def play(self):
    print("The player is playing cricket.")
    
class Batsman(player):
  def play(self):
    print("The batsman is batting.")

class Bowler(player):
  def play(self):
    print("The bowler is bowling.")

#Create objects of Batsman and Bowler classes and call the play()method for each object.
if_name_=="_main_":
batsman=Batsman()
bowler=Bowler()

batsman.play()
bowler.play()

    
    
    
  