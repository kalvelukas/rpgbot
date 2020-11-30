#class Mob:
#    condition = 100
#
#    rollMob = shadowroll.shadowroll()
#
#    result = rollMob.rollnpc("5d6")
#
#    print(str(result))
#
#    def __init__(self,name,race):
#        self.name = name
#        self.race = race
#    
#    def defend(self):
#        pass
#    
#    def attack(self):
#        pass

class Player:
    
    rollPlayer = shadowroll()

    result = rollPlayer.rollplayer("5d6s4")

    print(result)

        
