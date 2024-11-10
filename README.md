
# Enigma simulation 

A Python simulation to accurately replicate the Enigma Machine’s encryption and decryption
processes and expanded it into a web-based version using Django for backend logic.

# About Enigma

The Enigma machine is a cipher device developed and used in the early- to mid-20th century to protect commercial, diplomatic, and military communication. It was employed extensively by Nazi Germany during World War II, in all branches of the German military. The Enigma machine was considered so secure that it was used to encipher the most top-secret messages.

![App Screenshot](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Enigma_%28crittografia%29_-_Museo_scienza_e_tecnologia_Milano.jpg/800px-Enigma_%28crittografia%29_-_Museo_scienza_e_tecnologia_Milano.jpg)


# Machines implementations
## [Keyboard.py🔗](https://github.com/Nishantrde/Enigma/blob/master/machine/test_machine/key_board.py)

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

## [Plugboard.py🔗](https://github.com/Nishantrde/Enigma/blob/master/machine/test_machine/plugboard.py)

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


## [Rotor.py🔗](https://github.com/Nishantrde/Enigma/blob/master/machine/test_machine/rotor.py)

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
