class Stats:
    '''отслеживание статистики'''

    def __init__(self):
        '''инициализирует статистику'''
        self.score = None
        self.guns_left = None

        self.reset_stats()
        self.run_game = True
        with open('../Text/high_score.txt', 'r') as f:
            self.high_score = int(f.readline())  # Хранится всегда (не сбрасывается)

    def reset_stats(self):
        '''статистика, изменяющаяся во время игры'''
        self.guns_left = 2
        self.score = 0
