class Settings():
    """存储《外星人入侵》的基本参数"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        self.count=0

        #子弹参数配置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #外星人参数
        self.alien_speed = 1
        self.fleet_speed = 10

        self.fleet_direction = 1