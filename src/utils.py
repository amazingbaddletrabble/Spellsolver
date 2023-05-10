from datetime import datetime


points = {'a': 1, 'b': 4, 'c': 5, 'd': 3, 'e': 1, 'f': 5, 'g': 3, 'h': 4, 'i': 1, 'j': 7, 'k': 6, 'l': 3, 'm': 4,
            'n': 2, 'o': 1, 'p': 4, 'q': 8, 'r': 2, 's': 2, 't': 2, 'u': 4, 'v': 5, 'w': 5, 'x': 7, 'y': 4, 'z': 8}

def letter_points(letter):
    return points[letter]


class Timer:
    def __init__(self):
        self.reset_timer()
    
    def reset_timer(self):
        self.start_time = datetime.now()
    
    def elapsed_seconds(self):
        end_time = datetime.now()
        elapsed_time = (end_time - self.start_time).total_seconds()
        return round(elapsed_time, 2)
    
    def elapsed_millis(self):
        end_time = datetime.now()
        elapsed_time = (end_time - self.start_time).total_seconds() * 1000
        return round(elapsed_time, 0)
