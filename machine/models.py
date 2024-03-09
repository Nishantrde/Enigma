from django.db import models

class Inventory(models.Model):
    user_id = models.CharField(max_length = 20, default='DOG')
    RotorI = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"] 
    RotorII = ["AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"] 
    RotorIII = ["BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"] 
    RotorIV = ["ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"] 
    RotorV = ["VZBRGITYUPSDNHLXAWMJQOFECK", "Z"] 

    ReflectorA = "EJMZALYXVBWFCRQUONTSPIKHGD"
    ReflectorB = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    ReflectorC = "FVPJIAOYEDRZXWGCTKUQSBNMHL"

    Keys = models.CharField(max_length=3, default='DOG')
    def __str__(self):
        return self.Keys

class Keyboard(models.Model):
    user_id = models.CharField(max_length = 20, default='DOG')
    keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter = models.CharField(max_length=1, default='A')
    signal = models.IntegerField(default=0)

    def forward(self, letter):
        signal = self.keys.find(letter)
        return signal

    def backward(self, signal):
        letter = self.keys[signal]
        return letter

    def __str__(self):
        return self.keys


class Plugboard(models.Model):
    user_id = models.CharField(max_length = 20, default='DOG')
    right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pairs = models.JSONField(default=list)
    signal = models.IntegerField(default=0)

    def swap(self):
        for pair in self.pairs:
            a = pair[0]
            b = pair[1]
            pos_a = self.right.find(a)
            pos_b = self.right.find(b)
            self.left = self.left[:pos_a] + b + self.left[pos_a+1:]
            self.left = self.left[:pos_b] + a + self.left[pos_b+1:]

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

    def __str__(self):
        return self.left

class Rotor_I(models.Model):
    user_id = models.CharField(max_length = 20, default='DOG')
    right = models.CharField(max_length=26, default="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = models.IntegerField(default=1)

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

    def rotate(self, n=1):
        for _ in range(n):
            self.left = self.left[1:] + self.left[0]
            self.right = self.right[1:] + self.right[0]

    def rotate_to_char(self, letter):
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.rotate(n)

    def __str__(self):
        return self.right


class Rotor_II(models.Model):
    user_id = models.CharField(max_length = 20, default='DOG')
    right = models.CharField(max_length=26, default="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = models.IntegerField(default=1)

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

    def rotate(self, n=1):
        for _ in range(n):
            self.left = self.left[1:] + self.left[0]
            self.right = self.right[1:] + self.right[0]

    def rotate_to_char(self, letter):
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.rotate(n)

    def __str__(self):
        return self.right


class Rotor_III(models.Model):
    user_id = models.CharField(max_length = 20, default='DOG')
    right = models.CharField(max_length=26, default="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = models.IntegerField(default=1)

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

    def rotate(self, n=1):
        for _ in range(n):
            self.left = self.left[1:] + self.left[0]
            self.right = self.right[1:] + self.right[0]

    def rotate_to_char(self, letter):
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.rotate(n)

    def __str__(self):
        return self.right

class Reflector(models.Model):
    user_id = models.CharField(max_length = 20, default='DOG')
    right = models.CharField(max_length=26, default="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    signal = models.IntegerField(default=0)

    def reflector(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def __str__(self):
        return self.right
