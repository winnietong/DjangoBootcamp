__author__ = 'winnie'

class Board(object):
    def __init__(self):
        self.x_locations = []
        self.o_locations = []
        self.board =[
            ['   |   |   '],
            ['   |   |   '],
            ['   |   |   '],
            ['-----------'],
            ['   |   |   '],
            ['   |   |   '],
            ['   |   |   '],
            ['-----------'],
            ['   |   |   '],
            ['   |   |   '],
            ['   |   |   ']]
        self.help_board =[
            ['     |     |     '],
            ['(0 0)|(0 1)|(0 2)'],
            ['     |     |     '],
            ['-----------------'],
            ['     |     |     '],
            ['(1 0)|(1 1)|(1 2)'],
            ['     |     |     '],
            ['-----------------'],
            ['     |     |     '],
            ['(2 0)|(2 1)|(2 2)'],
            ['     |     |     ']]


    def print_help_board(self):
        for x in self.help_board:
            for y in x:
                print y

    def print_board(self):
        for x in self.board:
            for y in x:
                print y


    @staticmethod
    def get_board_location(x, y):
        x = x*4 +1
        y = y*4 +1
        return x, y


    def get_board_char(self, pretty_x, pretty_y):
        x, y = self.get_board_location(pretty_x, pretty_y)
        my_list = list(self.board[x][0])
        return my_list[y]


    @staticmethod
    def check_array(array):
        x = []
        y = []
        for num in array:
            x.append(num[0])

        for num in array:
            y.append(num[1])

        for num in range(2):
            if x.count(num) == 3 or y.count(num) == 3:
                print "THERE IS A WIN!"
                return True

        if [0, 0] in array and [1, 1] in array and [2, 2] in array:
            print "THERE IS A WIN!!"
            return True
        elif [0, 2] in array and [1, 1] in array and [2, 0] in array:
            return True


    def check_wins(self, x_or_o):
        if x_or_o == 'X':
            return self.check_array(self.x_locations)
        else:
            return self.check_array(self.o_locations)


    def check_move(self, marker, pretty_x, pretty_y):
        # Check that move is within boards
        if pretty_x > 2 or pretty_x < 0 or pretty_y > 2 or pretty_y < 0:
            print "Please enter a number between 0 to 2"
            return False
        # Check that move is not taken by X or O
        elif self.get_board_char(pretty_x, pretty_y) != " ":
            print "This move is already taken!"
            return False
        # Check if the board is full
        else:
            x, y = self.get_board_location(pretty_x, pretty_y)
            my_list = list(self.board[x][0])
            my_list[y] = marker
            str2 = "".join(my_list)
            self.board[x][0] = str2
            self.print_board()

            if marker == "X":
                self.x_locations.append([pretty_x, pretty_y])
            else:
                self.o_locations.append([pretty_x, pretty_y])
            return True
