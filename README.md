
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

Same like this I have this program which just mimic this process. Here **self.r3.rotate()**
 right most rotar which rotates at every key stroke and **self.r2.rotate()** rotates when **self.r3.rotate()** complete 24 strokes and same as **self.r1.rotate()**. 

```python
def encript(self, letter):
        if self.r2.left[0] == self.r2.notch and self.r3.left[0] == self.r3.notch:
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        
        elif self.r3.left[0] == self.r3.notch:
            self.r2.rotate()
            self.r3.rotate()
        else:
            self.r3.rotate()
```

Then we take the letter argument then pass to **forward** functions of the **objects** and then to reflector and the back to **backward** function of the **objects.** and then to keyboard which then returns the letter.
```python
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
```
Below is working **visualization** of this **Enigma** program.

![App Screenshot](https://res.cloudinary.com/dwfdyavop/image/upload/v1731257415/Screenshot_2024-11-10_084913_m4kgps.png)



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
# Django Implementations

## [Settings.py🔗⚙️](https://github.com/Nishantrde/Enigma/blob/master/enigma/settings.py)

To make our django aplication easy for deployment we made `ALLOWED_HOSTS = ["*"]` so, that we can access it from any url provied by cloud platform.
```python
ALLOWED_HOSTS = ["*"]

```
We then mention our ap **machine** in the **list of installed apps.**
```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'machine',
]
```
and **database** we are using **railway cloud.**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'monorail.proxy.rlwy.net',
        'PORT': '',
    }
}

```
This project uses Django's static files system for serving CSS, JavaScript, images, and other assets. The `STATIC_URL` setting defines the base URL for static files, while `STATICFILES_DIRS` specifies the directory where Django looks for additional static files during development. For production, the `STATIC_ROOT` setting determines the directory where all static files are collected when running the `collectstatic` command. Additionally, the `DEFAULT_AUTO_FIELD` setting is used to define the default primary key field type for models.

## [Urls.py🔗](https://github.com/Nishantrde/Enigma/blob/master/machine/urls.py)

It defines two URL routes using Django's `path` function. The first route maps the URL path `"enigma"` to the `enigma` view, which likely handles the Enigma Machine simulation. The second route maps the root URL (`""`) to the `doc` view, which is probably used to display documentation or additional information about the project.
```python
from django.urls import path
from . import views

urlpatterns = [
    path("enigma", views.enigma),
    path("", views.doc),
]
```

## [Views.py🔗👁️](https://github.com/Nishantrde/Enigma/blob/master/machine/views.py)

## Inputs
- **Plugboard (`plugbd`)**: A string representing pairs of connected letters, which is used for initial letter substitution.
- **Reflector (`reflector`)**: The type of reflector used in the Enigma machine (`A`, `B`, or `C`).
- **Rotor Settings (`rotor1`, `rotor2`, `rotor3`)**: Integer values representing the rotor configuration (1 to 5), which determine the wiring and notch positions.
- **Notches (`notch1`, `notch2`, `notch3`)**: The positions of the notches on each rotor, affecting when the rotors will rotate.
- **Message (`textmsg`)**: The plaintext message to be encrypted.

## Process
1. **Data Collection**: The view gathers the user inputs via a `POST` request.
2. **Rotor Setup**: Based on the rotor choices (`rotor1`, `rotor2`, `rotor3`), the corresponding rotors and notches are selected from the `Inventory`.
3. **Plugboard Setup**: The plugboard configuration is created and used to swap letters.
4. **Reflector Setup**: The selected reflector (A, B, or C) is chosen from the `Inventory`.
5. **Rotor Rotation**: Each rotor is rotated according to its corresponding notch positions, and the machine's wiring configuration is applied.
6. **Encryption**: The input message (`textmsg`) is processed letter by letter:
   - The letter goes through the keyboard, plugboard, and rotors.
   - The signal is reflected by the reflector and then goes back through the rotors, plugboard, and keyboard.
   - The resulting letter is added to the output string.
7. **Display**: The encrypted message is displayed using Django's messages framework.

## Final Clean-Up
- The created components (keyboard, plugboard, rotors, and reflector) are deleted after processing the message to avoid unnecessary memory usage.

## Output
- The encrypted message is displayed to the user as an informational message.
  
## Example Workflow
1. The user inputs the plugboard configuration, rotor settings, notch positions, reflector type, and plaintext message via the form.
2. The Enigma machine processes the message and displays the encrypted result on the same page.

## Template Rendering
The view renders the `enigma2.html` template, where the encrypted message and configurations are displayed. Additionally, a `doc.html` template is rendered for documentation purposes.

---

This view provides a functional simulation of the Enigma machine, implementing key encryption concepts of substitution and rotor shifting.
```python
from django.shortcuts import render
from machine.models import *
from django.contrib import messages

def enigma(request):
    keyboard = ""
    plugboard = []
    rotar_1 = []
    rotar_2 = []
    rotar_3 = []
    reflector_ = []
    if request.method == "POST":
        plgbd = str(request.POST.get("plugbd"))
        plugbd =  plgbd.upper().split()
        reflector = str(request.POST.get("reflector"))
        reflector = reflector.upper()
        keys = str(request.POST.get("notch3")) + str(request.POST.get("notch2")) + str(request.POST.get("notch1"))
        print(keys)
        keys = keys.upper()
        rotor1 = int(request.POST.get("rotor1"))
        rotor2 = int(request.POST.get("rotor2"))
        rotor3 = int(request.POST.get("rotor3"))
        
        textmsg = str(request.POST.get("textmsg"))
        textmsg = textmsg.upper()

        keybrd = Keyboard.objects.create()

        plgbrd = Plugboard.objects.create(pairs = plugbd)
        
        if rotor1 == 1:
            RotI = Inventory.RotorI[0]
        elif rotor1 == 2:
            RotI = Inventory.RotorII[0]
        elif rotor1 == 3:
            RotI = Inventory.RotorIII[0]
        elif rotor1 == 4:
            RotI = Inventory.RotorIV[0]
        elif rotor1 == 5:
            RotI = Inventory.RotorV[0]

        if rotor2 == 1:
            RotII = Inventory.RotorI[0]
            NotchII = Inventory.RotorI[1]
        elif rotor2 == 2:
            RotII = Inventory.RotorII[0]
            NotchII = Inventory.RotorII[1]
        elif rotor2 == 3:
            RotII = Inventory.RotorIII[0]
            NotchII = Inventory.RotorIII[1]
        elif rotor2 == 4:
            RotII = Inventory.RotorIV[0]
            NotchII = Inventory.RotorIV[1]
        elif rotor2 == 5:
            RotII = Inventory.RotorV[0]
            NotchII = Inventory.RotorV[1]

        if rotor3 == 1:
            RotIII = Inventory.RotorI[0]
            NotchIII = Inventory.RotorI[1]
        elif rotor3 == 2:
            RotIII = Inventory.RotorII[0]
            NotchIII = Inventory.RotorII[1]
        elif rotor3 == 3:
            RotIII = Inventory.RotorIII[0]
            NotchIII = Inventory.RotorIII[1]
        elif rotor3 == 4:
            RotIII = Inventory.RotorIV[0]
            NotchIII = Inventory.RotorIV[1]
        elif rotor3 == 5:
            RotIII = Inventory.RotorV[0]
            NotchIII = Inventory.RotorV[1]

        if reflector == "A":
            reflt = Inventory.ReflectorA
        elif reflector == "B":
            reflt = Inventory.ReflectorB
        elif reflector == "C":
            reflt = Inventory.ReflectorC

        Keys = Inventory.objects.create(Keys = keys)

        plgbrd.swap()

        RI = Rotor_I.objects.create(right = RotI)
        RII = Rotor_II.objects.create(right = RotII)
        RIII = Rotor_III.objects.create(right = RotIII)
        
        REFLT = Reflector.objects.create(right = reflt) 
        
        RI.rotate_to_char(Keys.Keys[0])
        RII.rotate_to_char(Keys.Keys[1])
        RIII.rotate_to_char(Keys.Keys[2])

        def encript(letter):
            
            if RIII.left[0] == NotchIII and RII.left[0] == NotchII:
                RI.rotate()
                RII.rotate()
                RIII.rotate()

            elif RIII.left[0] == NotchIII:
                RII.rotate()
                RIII.rotate()

            else:
                RIII.rotate()
            
            signal = keybrd.forward(letter)
            signal = plgbrd.forward(signal)
            signal = RIII.forward(signal)
            signal = RII.forward(signal)
            signal = RI.forward(signal)
            signal = REFLT.reflector(signal)
            signal = RI.backward(signal)
            signal = RII.backward(signal)
            signal = RIII.backward(signal)
            signal = plgbrd.backward(signal)
            letter = keybrd.backward(signal)
            
            return letter
        
        op = ""
        for msg in textmsg:
            op = op + encript(msg)
        print(op)
        messages.info(request, op)
        plugboard.append(plgbrd.left)
        rotar_1.append(RI.right)
        rotar_2.append(RII.right)
        rotar_3.append(RIII.right)
        reflector_.append(REFLT.right)
        keybrd.delete()
        plgbrd.delete()
        RI.delete()
        RII.delete()
        RIII.delete()
        REFLT.delete()
    keyboard = Keyboard.keys
    plugboard.append(Plugboard.right)
    rotar_1.append(Rotor_I.left)
    rotar_2.append(Rotor_II.left)
    rotar_3.append(Rotor_III.left)
    reflector_.append(Reflector.left)
    print(keyboard, plugboard)
    return render(request, "enigma2.html")

```
## [Models.py🔗🗄️](https://github.com/Nishantrde/Enigma/blob/master/machine/models.py)


This document provides an overview of the Django models used to simulate the Enigma Machine.

## 1. Inventory Model

The `Inventory` model represents the configurations for the rotors and reflectors, along with the initial key setting.

### Code:

```python
class Inventory(models.Model):
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
```
### Fields:
- **RotorI, RotorII, RotorIII, RotorIV, RotorV**: Rotor wiring configurations and initial positions.
- **ReflectorA, ReflectorB, ReflectorC**: Reflector wiring configurations.
- **Keys**: User-defined key for encryption (default: 'DOG').

---

## 2. Keyboard Model

The `Keyboard` model represents the Enigma machine's keyboard with letters A-Z.

### Code:

```python
class Keyboard(models.Model):
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
```
### Methods:
- forward(letter): Maps a letter to its corresponding signal (index in the alphabet).
- backward(signal): Maps a signal (index) back to the corresponding letter.

## 3. Plugboard Model

The `Plugboard` model allows for letter pair swapping, which modifies the signal.

### Code:

```python
class Plugboard(models.Model):
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
```
## Methods 
- **swap()**: Swaps pairs of letters in the left wiring.
- **forward(signal)**: Maps a signal through the plugboard.
- **backward(signal)**: Maps a signal backward through the plugboard.

---

## 4. Rotor Models (Rotor_I, Rotor_II, Rotor_III)

Each rotor has a right and left wiring, with methods to map signals forward and backward. The rotors also rotate with each key press.

### Code (for Rotor_I):

```python
class Rotor_I(models.Model):
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
```
## Methods 
- **forward(signal)**: Maps a signal through the rotor.
- **backward(signal)**: Maps a signal in reverse through the rotor.
- **rotate(n)**: Rotates the rotor by `n` positions.
- **rotate_to_char(letter)**: Rotates the rotor to a specific letter.

---

## 5. Reflector Model

The `Reflector` model reflects the signal back after passing through the rotors.

### Code:

```python
class Reflector(models.Model):
    right = models.CharField(max_length=26, default="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    signal = models.IntegerField(default=0)

    def reflector(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def __str__(self):
        return self.right
```
## Methods:
**reflector(signal):** Reflects the signal through the reflector.

## Enigma Machine Projectℹ️

I have developed and deployed an Enigma Machine simulation in Django. You can learn more about the project from the following YouTube videos:

1. [Enigma Machine Overview](https://www.youtube.com/watch?v=ybkkiGtJmkM&t=967s) 📹
2. [Detailed Walkthrough and Explanation](https://www.youtube.com/watch?v=sbm2dmkmqgQ&t=365s) 🎥



