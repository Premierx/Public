
#!/usr/bin/env python3
import math
shape_list = ["krychle", "kvadr", "koule", "ctverec", "obdelnik", "kruh"]

shape_input = input("Vyberte si těleso, se kterým chcete počítat (krychle, kvadr, koule, ctverec, obdelnik, kruh): ")

try:
    if shape_input in shape_list:
        print("Teleso je definovano.")

        if shape_input == "krychle":
            a = float(input("Zadejte hodnotu a: "))

            result = a * a * a
            result1 = 6 * a * a
            if ( a == 0):
                print("Výpočet není možny")
            else:
                print(f" Objem krychle je: {result} a povrch krychle je : {result1} ")

        if shape_input == "kvadr":
            
            a = float(input("Zadejte hodnotu a: "))
            b = float(input("Zadejte hodnotu b: "))
            c = float(input("Zadejte hodnotu c: "))
            
            result = a * b * c
            result1 = (2 * a * b) + (2 * a * c) + (2 * b * c)
            if ( a == 0, b == 0, c == 0):
                print("Výpočet není možný")
            else:
                print(f" Objem kvadru je: {result} a povrch kvadru je  {result1}")

        if shape_input == "koule":

            r = float(input("Zadejte polomer r: "))

            result = 4/3 * math.pi * r * r * r
            result1 = 4 * math.pi * r * r
            if ( r == 0):
                print("Výpočet není možny")
            else:
                print(f" Objem koule je {result} a povrch koule je  {result1}")

        if shape_input == "ctverec":
            a= float(input("Zadejte hodnotu a: "))

            result1 = 4 * a
            result2 = a * a
            if ( a == 0):
                print("Výpočet není možny")
            else:
                print(f" Obvod ctverce je: {result1} a obsah ctverce je {result2} ")

        if shape_input == "obdelnik":
            a= float(input("Zadejte hodnotu a: "))
            b= float(input("Zadejte hodnotu b: "))

            result1 = 2 * (a + b)
            result2 = a * b
            if ( a == 0, b == 0):
                print("Výpočet není možny")
            else:
                print(f" Obvod obdelniku je: {result1} a obsah obdelniku je {result2} ")
            
        if shape_input == "kruh":
            r = float(input("Zadejte polomer r:"))

            result1 = 2 * math.pi * r
            result2 = math.pi * r * r
            if ( r == 0):
                print("Výpočet není možny")
            else:
                print(f" Obvod kruhu je: {result1} a obsah kruhu je {result2} ")

    else:
        print("Teleso neni definovano.")
except:
    print("Výpočet nebyl možný")
