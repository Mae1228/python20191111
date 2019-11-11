'''用于统计游戏信息（相当于日志）'''

class Game_state:
    def __init__(self,setting):
        self.setting=setting
        self.reset_state()
        self.game_active = True
    # 重置飞船
    def reset_state(self):
        self.ship_left=self.setting.ship_limit