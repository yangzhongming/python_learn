class MusicPlayer(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if not MusicPlayer.init_flag:
            print("初始化音乐播放器...")
            MusicPlayer.init_flag = True

player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)