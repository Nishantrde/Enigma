
# Enigma simulation 📜

A Python simulation to accurately replicate the Enigma Machine’s encryption and decryption
processes and expanded it into a web-based version using Django for backend logic.

# About Enigma ℹ️

The Enigma machine is a cipher device developed and used in the early- to mid-20th century to protect commercial, diplomatic, and military communication. It was employed extensively by Nazi Germany during World War II, in all branches of the German military. The Enigma machine was considered so secure that it was used to encipher the most top-secret messages.

![App Screenshot](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Enigma_%28crittografia%29_-_Museo_scienza_e_tecnologia_Milano.jpg/800px-Enigma_%28crittografia%29_-_Museo_scienza_e_tecnologia_Milano.jpg)


# Machines implementations
## [Keyboard.py🔗⌨️](https://github.com/Nishantrde/Enigma/blob/master/machine/test_machine/key_board.py)

Below is the **WW II Enigma Keyboard** just look and also sounded as a typewriter.

(*Fun fact it also QWERTY System*)

![App Screenshot](https://res.cloudinary.com/dwfdyavop/image/upload/v1731223928/key_board_vyphgw.jpg)

This program takes the letter and **returns the index as a signal.**


```python
class Keyboard:

    def forward(self, letter):
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        return signal
    def backward(self, signal):
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter


```
![App Screenshot](https://res.cloudinary.com/dwfdyavop/image/upload/v1730796825/index_0_myaqhq.png)

## [Plugboard.py🔗🔌](https://github.com/Nishantrde/Enigma/blob/master/machine/test_machine/plugboard.py)

This is a **Plugboard** just loacted below the **keyboard.** Generely it uses 10 **Plug Wires** to **swap** the **letters.** 

![App Screenshot](https://res.cloudinary.com/dwfdyavop/image/upload/v1731224218/plugboard_ivbnlw.jpg)

This program takes a **list** as an argument which contains **strings** of two letters which are to be swapped, ( e.g **["AR", "GK", "OX"]**) by finding the index form **left** and swaps its.

```python
class Plugboard:
    def __init__(self, pairs):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            A = pair[0]
            B = pair[1]
            pos_a = self.left.find(A)
            pos_b = self.left.find(B)
            self.left = self.left[:pos_a] + B + self.left[pos_a+1:]
            self.left = self.left[:pos_b] + A + self.left[pos_b+1:]

```
The **forward** and **backward** functions takes the signal and then searches the letters in the **right** and then it searches the letter **left** which is swapped and the index as a signal.

```python
def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

```

![App Screenshot](https://res.cloudinary.com/dwfdyavop/image/upload/v1730799281/Screenshot_2024-11-05_013348_ah36ti.png)


## [Rotor.py🔗⚙️](https://github.com/Nishantrde/Enigma/blob/master/machine/test_machine/rotor.py)

This program takes two argument a **rotar wiring** and a **notch**.

**e.g**
```python
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")

```
**"EKMFLGDQVZNTOWYHXUSPAIBRCJ"** is an historical rotar wiring used by Nazis during **WW II**. During the starting of the war there were three rotars but as the allied forces starting cracking the messages they started keeping 5 rotars.

Each rotars had a **Notch** as shown in the image below where we could set stating point of the rotars from where they will start rotatating.  

![App Screenshot](https://res.cloudinary.com/dwfdyavop/image/upload/v1731220568/rotar_enigma_favojs.jpg)

When we call the the Rotar functions we assin the variable **self.left** and **self.right**
to **"ABCDEFGHIJKLMNOPQRSTUVWXYZ"** and **wiring**
```python
class Rotor:
    def __init__(self, wiring, notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.notch = notch
```
Then we call the **rotate_to_letter(self, letter)** which first finds out how much the rotar should raote by finding the index of the letter in the string **"ABCDEFGHIJKLMNOPQRSTUVWXYZ"** and then it calls the **rotate(self, n=1)** function which rotates the rotar that many times so that it **index** or **notch.**
```python
def rotate(self, n=1):
        for _ in range(n):
            self.left = self.left[1:] + self.left[0]
            self.right = self.right[1:] + self.right[0]

    def rotate_to_letter(self, letter):
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.rotate(n)
```
![App Screenshot](https://res.cloudinary.com/dwfdyavop/image/upload/v1731219074/Screenshot_2024-11-09_221055_fsoeaw.png)

## [Reflector.py🔗🪞](https://github.com/Nishantrde/Enigma/blob/master/machine/test_machine/reflect.py)

This program just take the **signal** and **throws back** the signal to **rotars** by changing the **signals.**
**e.g**

```python
A = Reflect("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflect("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflect("FVPJIAOYEDRZXWGCTKUQSBNMHL")
```
**"EJMZALYXVBWFCRQUONTSPIKHGD"** is a historical refletor used during the war. below is the a reflector which shows where and how it was placed in the machine.

![App Screenshot](https://res.cloudinary.com/dwfdyavop/image/upload/v1731223579/reflector_bjvg3j.jpg)

It takes argument **wiring** and assin it to **self.right** and **self.left** gets assin by **"ABCDEFGHIJKLMNOPQRSTUVWXYZ"**. Then we call this function **reflector(self, signal)**
takes the **signal** and finds it in letter in **self.right** and then it find the index of the letter in **self.left** and returns the **signal.**

```python
class Reflect:
    def __init__(self, wiring):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        
    def reflector(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal
```
![App Screenshot](https://res.cloudinary.com/dwfdyavop/image/upload/v1731223237/Screenshot_2024-11-09_232016_nxalqq.png)

## [Enigma.py📜(journey of the messages)🔗](https://github.com/Nishantrde/Enigma/blob/master/machine/test_machine/main.py)

This program is the **heart** of the machine. Which takes **Keyboard, Plugboard, Rotar, Reflector**
```python
class Enigma:
    def __init__(self,kb,pb,r1,r2,r3,re):
        self.kb = kb
        self.pb = pb
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.re = re
```
**set_key(self, key)** This function set the Key which will rotate the **rotars.**

```python
def set_key(self, key):
        self.r1.rotate_to_letter(key[0])
        self.r2.rotate_to_letter(key[1])
        self.r3.rotate_to_letter(key[2])
```
The **Rotars** had **gears.** The right most **rotar** have 24 teeth which is equal to **24 letter** which rotate the rotar at every key stroke and other rotars have one teeth which rotates the when the right most rotar complete **24 strokes.** 

![App Screenshot](https://res.cloudinary.com/dwfdyavop/image/upload/v1731251199/Screenshot_2024-11-10_070617_xnfgqy.png)

## [Main.py🔗🧑‍💻](https://github.com/Nishantrde/Enigma/blob/master/machine/test_machine/main.py)
Here we imported all the parts of machine like **Keyboard, Plugboard, Rotar, Reflector** and the machine **Enigma.**

```python
from key_board import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflect import Reflect
from enigma import Enigma
```
We spacified the object for Rotars, Reflectors, Keyboard, Plugboard, Enigma
```python
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
```
Then we pass the **key** e.g **"DOG"** and then we pass the **msg** from the **string: "NGMC"** and then append the output in the string **op**
```python
op = ""
ENIGMA.set_key("DOG")
for msg in "NGMC":
    op = op + ENIGMA.encript(msg)
print(op)

```


