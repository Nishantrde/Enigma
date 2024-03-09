class Reflect:
    def __init__(self, wiring):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        
    def reflector(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal