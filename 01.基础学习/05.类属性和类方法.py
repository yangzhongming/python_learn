class Game(object):
    top_score = 0

    @staticmethod
    def show_help():
        print("帮助信息...")

    @classmethod
    def show_top_score(cls):
        print("最高分：%d" %cls.top_score)

    def __init__(self,player_name):
        self.player_name = player_name

    def start_game(self):
         Game.top_score = 999

Game.show_help()
Game.show_top_score()
game = Game("小明")
game.start_game()
Game.show_top_score()