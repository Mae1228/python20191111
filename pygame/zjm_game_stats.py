class GameStats():
    """跟踪统计游戏信息"""

    def __init__(self, set):
        """初始化游戏的统计信息"""
        self.set = set
        self.reset_stats()

        # 游戏刚启动时处于活动状态
        self.game_active = True

    def reset_stats(self):
        """初初始化在游戏中可能变化的统计信息"""
        self.ships_left = self.set.ship_limit
        self.count=self.set.count


