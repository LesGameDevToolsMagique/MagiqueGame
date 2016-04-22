#
#   TicTacToe class
#

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

    def init(self):
        self.random_form()

        # send player form
        self.cm.send_data('{"form": %s}' % (self.player_form))

        # send map
        self.cm.send_data('{"map": %s}' % (self.game_map))

    def run(self):
        stop = False

        while not stop:
            stop = True

    def destroy(self):
        # send end message
        pass

    #
    #
    #

    def random_form(self):
        import random
        r = random.randrange(100)

        if (r % 2) == 0:
            self.player_form = 'X'
            self.ia_form = 'O'
        else:
            self.player_form = 'O'
            self.ia_form = 'X'
