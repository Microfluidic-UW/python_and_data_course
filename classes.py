class Cat():
    
    def __init__(self, sound, move):
        self.sound = sound
        self.move = move

    def kotek_meow(self):
        miau = self.sound
        return miau * 3
    
    def move_kotek(self):
        ruch = f'kotek {self.move} trzy razy'
        return ruch

