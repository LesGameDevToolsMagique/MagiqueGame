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
    def __init__(self, cm):
        self.cm = cm
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
        self.cm.send_data('{"form": "%s", "map-width": 3, "map-height": 3}' % (self.player_form))

        sleep(1)
        # send map
        self.cm.send_data(self.json_map())



    #
    def run(self):
        first = True

        self.ia_first_play()

        while True:
            self.player_turn(self.cm.recv_data())

            if self.check_form(self.player_form, '') is True:
                self.cm.send_data('{"message": "You win"}')
                break

            self.ia_turn()

            if self.check_form(self.ia_form, '') is True:
                self.cm.send_data('{"message": "You loose"}')
                break

    #
    def destroy(self):
        #
        #   If other end message between the server and client or on the game, do it here
        #

        # send end message
        self.cm.send_data('{"message": "Thank you for playing, byebye"}')
        pass

    #
    #
    #

    #
    def json_map(self):
        return str({
            "map": {
                1: self.game_map[0],
                2: self.game_map[1],
                3: self.game_map[2],
                4: self.game_map[3],
                5: self.game_map[4],
                6: self.game_map[5],
                7: self.game_map[6],
                8: self.game_map[7],
                9: self.game_map[8],
            }
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
            self.game_map[5] = self.ia_form
            self.cm.send_data(self.json_map())

    #
    def check_form(self, check_form, form, play=False):
        # check lines
        # column 1
        if self.game_map[1] == check_form and self.game_map[2] == check_form:
            if play is True:
                self.game_map[0] = form
            return True
        elif self.game_map[4] == check_form and self.game_map[5] == check_form:
            if play is True:
                self.game_map[3] = form
            return True
        elif self.game_map[7] == check_form and self.game_map[8] == check_form:
            if play is True:
                self.game_map[6] = form
            return True

        # column 2
        if self.game_map[0] == check_form and self.game_map[2] == check_form:
            if play is True:
                self.game_map[1] = form
            return True
        elif self.game_map[3] == check_form and self.game_map[5] == check_form:
            if play is True:
                self.game_map[4] = form
            return True
        elif self.game_map[6] == check_form and self.game_map[8] == check_form:
            if play is True:
                self.game_map[7] = form
            return True

        # column 3
        if self.game_map[0] == check_form and self.game_map[1] == check_form:
            self.game_map[2] = form
            return True
        elif self.game_map[3] == check_form and self.game_map[4] == check_form:
            self.game_map[5] = form
            return True
        elif self.game_map[6] == check_form and self.game_map[7] == check_form:
            self.game_map[8] = form
            return True

        # check columns
        # line 1
        if self.game_map[3] == check_form and self.game_map[6] == check_form:
            if play is True:
                self.game_map[0] = form
            return True
        elif self.game_map[4] == check_form and self.game_map[7] == check_form:
            if play is True:
                self.game_map[1] = form
            return True
        elif self.game_map[5] == check_form and self.game_map[8] == check_form:
            if play is True:
                self.game_map[2] = form
            return True

        # line 2
        if self.game_map[0] == check_form and self.game_map[3] == check_form:
            if play is True:
                self.game_map[6] = form
            return True
        elif self.game_map[1] == check_form and self.game_map[4] == check_form:
            if play is True:
                self.game_map[7] = form
            return True
        elif self.game_map[2] == check_form and self.game_map[5] == check_form:
            if play is True:
                self.game_map[8] = form
            return True

        # line 3
        if self.game_map[0] == check_form and self.game_map[3] == check_form:
            if play is True:
                self.game_map[6] = form
            return True
        elif self.game_map[1] == check_form and self.game_map[4] == check_form:
            if play is True:
                self.game_map[7] = form
            return True
        elif self.game_map[2] == check_form and self.game_map[5] == check_form:
            if play is True:
                self.game_map[8] = form
            return True

        # check diagonals
        # diago right
        if self.game_map[0] == check_form and self.game_map[4] == check_form:
            if play is True:
                self.game_map[8] = form
            return True
        elif self.game_map[0] == check_form and self.game_map[8] == check_form:
            if play is True:
                self.game_map[4] = form
            return True
        elif self.game_map[8] == check_form and self.game_map[4] == check_form:
            if play is True:
                self.game_map[0] = form
            return True

        # diago left
        if self.game_map[2] == check_form and self.game_map[4] == check_form:
            if play is True:
                self.game_map[6] = form
            return True
        elif self.game_map[2] == check_form and self.game_map[6] == check_form:
            if play is True:
                self.game_map[4] = form
            return True
        elif self.game_map[6] == check_form and self.game_map[4] == check_form:
            if play is True:
                self.game_map[2] = form
            return True

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
        play = self.check_form(self.ia_form, self.ia_form, True)

        # def
        if play is False:
            play = self.check_form(self.player_form, self.ia_form, True)

        # play a random case
        if play is False:
            self.ia_random_play()

        # send map after ia turn
        self.cm.send_data(self.json_map())


    #
    #   Player
    #

    #
    def player_turn(self, play):
        case = 0

        # TODO
        #   transform into map case

        # check if case is free
        #   if free accept and send the new map to client
        #   else send error to client
        if self.game_map[case] == '':
            self.game_map[case] = self.player_form
            self.cm.send_data(self.json_map())
        else:
            self.cm.send_data('{"error": "Can\'t play on this case"}')
