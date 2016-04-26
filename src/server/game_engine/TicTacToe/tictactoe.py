#
#   TicTacToe class
#

from time import sleep

class TicTacToe(object):
    """
    """
    game_map = []

    player_form = ''
    ia_form = ''

    #
    def __init__(self, socket):
        self.s = socket
        for i in range(0, 9):
            self.game_map.append("")


    #
    #   REQUIRED FUNCTION
    #

    #
    def init(self):
        self.random_form()

        #
        #   If other initialization between the server and client or on the game, do it here
        #

        # send player form
        self.s.send_data('{"form": "%s", "map-width": 3, "map-height": 3}' % (self.player_form))

        # send map
        self.s.send_data('%s' % (self.json_map()))



    #
    def run(self):
        first = True

        self.ia_first_play()

        while True:
            self.player_turn()

            if self.check_form(self.player_form, '') is True:
                self.s.send_data('{"message": "You win"}')
                break

            self.ia_turn()

            if self.check_form(self.ia_form, '') is True:
                self.s.send_data('{"message": "You loose"}')
                break

            if self.check_map_full() is True:
                self.s.send_data('{"message": "Draw"}')
                break

        self.destroy()


    #
    def destroy(self):
        #
        #   If other end message between the server and client or on the game, do it here
        #

        # send end message
        self.s.send_data('{"message": "Thank you for playing, byebye"}')
        self.game_map = []


    #
    #
    #

    #
    def json_map(self):
        return str({
            "map": self.game_map
        })


    #
    #   Random
    #

    #
    def get_rand(self, max):
        import random
        return random.randrange(max)

    #
    def random_form(self):
        if (self.get_rand(100) % 2) == 0:
            self.player_form = 'X'
            self.ia_form = 'O'
        else:
            self.player_form = 'O'
            self.ia_form = 'X'

    #
    #   IA
    #

    #
    def ia_first_play(self):
        if (self.get_rand(50) % 3) == 0:
            self.game_map[4] = self.ia_form
        self.s.send_data(self.json_map())

    #
    def play_or_check(self, case, play, check_form, form):
        if play is True and self.game_map[case] == '':
            self.game_map[case] = form
            return True
        return False

    #
    def check_map_full(self):
        isFull = True

        for c in self.game_map:
            if c == '':
                isFull = False

        return isFull

    #
    def check_form(self, check_form, form, play=False):
        # check lines
        # column 1
        if self.game_map[1] == check_form and self.game_map[2] == check_form:
            return self.play_or_check(0, play, check_form, form)
        elif self.game_map[4] == check_form and self.game_map[5] == check_form:
            return self.play_or_check(3, play, check_form, form)
        elif self.game_map[7] == check_form and self.game_map[8] == check_form:
            return self.play_or_check(6, play, check_form, form)

        # column 2
        if self.game_map[0] == check_form and self.game_map[2] == check_form:
            return self.play_or_check(1, play, check_form, form)
        elif self.game_map[3] == check_form and self.game_map[5] == check_form:
            return self.play_or_check(4, play, check_form, form)
        elif self.game_map[6] == check_form and self.game_map[8] == check_form:
            return self.play_or_check(7, play, check_form, form)

        # column 3
        if self.game_map[0] == check_form and self.game_map[1] == check_form:
            return self.play_or_check(2, play, check_form, form)
        elif self.game_map[3] == check_form and self.game_map[4] == check_form:
            return self.play_or_check(5, play, check_form, form)
        elif self.game_map[6] == check_form and self.game_map[7] == check_form:
            return self.play_or_check(8, play, check_form, form)

        # check columns
        # line 1
        if self.game_map[3] == check_form and self.game_map[6] == check_form:
            return self.play_or_check(0, play, check_form, form)
        elif self.game_map[4] == check_form and self.game_map[7] == check_form:
            return self.play_or_check(1, play, check_form, form)
        elif self.game_map[5] == check_form and self.game_map[8] == check_form:
            return self.play_or_check(2, play, check_form, form)

        # line 2
        if self.game_map[0] == check_form and self.game_map[6] == check_form:
            return self.play_or_check(3, play, check_form, form)
        elif self.game_map[1] == check_form and self.game_map[7] == check_form:
            return self.play_or_check(4, play, check_form, form)
        elif self.game_map[2] == check_form and self.game_map[8] == check_form:
            return self.play_or_check(5, play, check_form, form)

        # line 3
        if self.game_map[0] == check_form and self.game_map[3] == check_form:
            return self.play_or_check(6, play, check_form, form)
        elif self.game_map[1] == check_form and self.game_map[4] == check_form:
            return self.play_or_check(7, play, check_form, form)
        elif self.game_map[2] == check_form and self.game_map[5] == check_form:
            return self.play_or_check(8, play, check_form, form)

        # check diagonals
        # diago right
        if self.game_map[0] == check_form and self.game_map[4] == check_form:
            return self.play_or_check(8, play, check_form, form)
        elif self.game_map[0] == check_form and self.game_map[8] == check_form:
            return self.play_or_check(4, play, check_form, form)
        elif self.game_map[8] == check_form and self.game_map[4] == check_form:
            return self.play_or_check(0, play, check_form, form)

        # diago left
        if self.game_map[2] == check_form and self.game_map[4] == check_form:
            return self.play_or_check(6, play, check_form, form)
        elif self.game_map[2] == check_form and self.game_map[6] == check_form:
            return self.play_or_check(4, play, check_form, form)
        elif self.game_map[6] == check_form and self.game_map[4] == check_form:
            return self.play_or_check(2, play, check_form, form)

        return False

    #
    def ia_random_play(self):
        stop = False

        while not stop:
            r = self.get_rand(9)
            if self.game_map[r] == '':
                self.game_map[r] = self.ia_form
                stop = True

    #
    def ia_turn(self):
        # attack
        print('ia attack')
        play = self.check_form(self.ia_form, self.ia_form, True)

        # def
        if play is False:
            print('ia defense')
            play = self.check_form(self.player_form, self.ia_form, True)

        # play a random case
        if play is False:
            print('ia osef')
            for i in range(0, len(self.game_map)):
                if self.game_map[i] == '':
                    self.game_map[i] = self.ia_form
                    break

        # send map after ia turn
        self.s.send_data(self.json_map())


    #
    #   Player
    #

    #
    def player_turn(self):
        import json
        case = -1

        # transform event into a map case
        play = json.loads(self.s.recv_data())

        if 'x' in play and 'y' in play:
            x = int(play['x'])
            y = int(play['y'])
            print("%d ; %d" % (x , y))
            if (x >= 0 and x <= 2) and (y >= 0 and y <= 2):
                case = x + (y * 3)
            else:
                self.s.send_data('{"error": "Bad position"}')
                self.player_turn()
        else:
            self.s.send_data('{"error": "No required data x and y"}')
            self.player_turn()

        # check if case is free
        #   if free accept and send the new map to client
        #   else send error to client
        if self.game_map[case] == '':
            self.game_map[case] = self.player_form
            self.s.send_data(self.json_map())
        else:
            self.s.send_data('{"error": "Can not play on this case"}')
            self.player_turn()
