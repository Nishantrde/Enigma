from django.shortcuts import render
from machine.models import *
from django.contrib import messages

def enigma(request):
    if request.method == "POST":
        plgbd = str(request.POST.get("plugbd"))
        plugbd =  plgbd.upper().split()
        reflector = str(request.POST.get("reflector"))
        reflector = reflector.upper()
        keys = str(request.POST.get("keys"))
        keys = keys.upper()
        rotor1 = int(request.POST.get("rotor1"))
        rotor2 = int(request.POST.get("rotor2"))
        rotor3 = int(request.POST.get("rotor3"))
        textmsg = str(request.POST.get("textmsg"))
        textmsg = textmsg.upper()

        keybrd = Keyboard.objects.create(user_id = "nis")

        plgbrd = Plugboard.objects.create(user_id = "nis", pairs = plugbd)
        
        if rotor1 == 1:
            RotI = Inventory.RotorI[0]
        elif rotor1 == 2:
            RotI = Inventory.RotorII[0]
        elif rotor1 == 3:
            RotI = Inventory.RotorIII[0]
        elif rotor1 == 4:int(
            RotI = Inventory.RotorIV[0])
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

        Keys = Inventory.objects.create(user_id = "nis", Keys = keys)

        plgbrd.swap()

        RI = Rotor_I.objects.create(user_id = "nis", right = RotI)
        RII = Rotor_II.objects.create(user_id = "nis", right = RotII)
        RIII = Rotor_III.objects.create(user_id = "nis", right = RotIII)
        
        REFLT = Reflector.objects.create(user_id = "nis", right = reflt) 
        
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
        keybrd.delete()
        plgbrd.delete()
        RI.delete()
        RII.delete()
        RIII.delete()
        REFLT.delete()

    return render(request, "enigma.html")




