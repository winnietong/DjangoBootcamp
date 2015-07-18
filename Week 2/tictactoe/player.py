__author__ = 'winnie'


class Player(object):
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker
        self.wins = 0

    def __repr__(self):
        print "{} with move {} has {} win(s).".format(self.name, self.marker, self.wins)