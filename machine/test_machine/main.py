from key_board import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflect import Reflect
from enigma import Enigma

I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

A = Reflect("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflect("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflect("FVPJIAOYEDRZXWGCTKUQSBNMHL")

KB = Keyboard()
PB = Plugboard(["AR", "GK", "OX"])

ENIGMA = Enigma(KB,PB,I,II,III,A)

op = ""
ENIGMA.set_key("DOG")
for msg in "NGMC":
    op = op + ENIGMA.encript(msg)
print(op)

# print(ENIGMA.encript("A"))

