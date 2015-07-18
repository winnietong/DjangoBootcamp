__author__ = 'winnie'

class Pokemon(object):
    def __init__(self, name, skill, level):
        self.name = name
        # Skills: Fire, Water, Earth
        self.skill = skill
        self.level = level


    def __repr__(self):
        return self.name

    def level_up(self):
        self.level += 1
        print "Your new level is {}".format(self.level)

