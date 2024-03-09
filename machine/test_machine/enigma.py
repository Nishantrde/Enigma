class Enigma:
    def __init__(self,kb,pb,r1,r2,r3,re):
        self.kb = kb
        self.pb = pb
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.re = re
        
    def set_key(self, key):
        self.r1.rotate_to_letter(key[0])
        self.r2.rotate_to_letter(key[1])
        self.r3.rotate_to_letter(key[2])
        

    def encript(self, letter):
        if self.r2.left[0] == self.r2.notch and self.r3.left[0] == self.r3.notch:
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        # elif self.r2.left[0] == self.r2.notch:
        #     self.r1.rotate()
        #     self.r2.rotate()
        #     self.r3.rotate()
        elif self.r3.left[0] == self.r3.notch:
            self.r2.rotate()
            self.r3.rotate()
        else:
            self.r3.rotate()

        
        signal = self.kb.forward(letter)
        signal = self.pb.forward(signal)
        signal = self.r3.forward(signal)
        signal = self.r2.forward(signal)
        signal = self.r1.forward(signal)
        signal = self.re.reflector(signal)
        signal = self.r1.backward(signal)
        signal = self.r2.backward(signal)
        signal = self.r3.backward(signal)
        signal = self.pb.backward(signal)
        letter = self.kb.backward(signal)

        return letter       
