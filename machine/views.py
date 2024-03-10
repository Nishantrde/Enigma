from django.shortcuts import render, redirect
from machine.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
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

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect("/")
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Invalid password")
            return redirect("/")
        else:
            login(request, user)
            return redirect("/enigma")
        
    messages.info(request, "login")
    return render(request, "login.html")

def logout_page(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('First_name')
        last_name = request.POST.get('Last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, 'Username alredy taken')
            return redirect('/register')
         
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()
        messages.info(request, 'Account created successfully')
        return redirect('/register')
    
    return render(request, "register.html")




