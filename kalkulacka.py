#!/usr/bin/env python3
import math
shape_list = ["krychle", "kvadr", "koule", "ctverec", "obdelnik", "kruh"]
shape_input = input("Vyberte si těleso, se kterým chcete počítat (krychle, kvadr, koule, ctverec, obdelnik, kruh): ")

if shape_input in shape_list:
    print("Teleso je definovano.")

    if shape_input == "krychle":
        a = float(input("Zadejte hodnotu a: "))
        print(f" Objem krychle je: {a*a*a} a povrch krychle je : {6*a*a} ")

    if shape_input == "kvadr":
        a = float(input("Zadejte hodnotu a: "))
        b = float(input("Zadejte hodnotu b: "))
        c = float(input("Zadejte hodnotu c: "))
        print(f" Objem kvadru je: {a * b * c} a povrch kvadru je  {(2 * a * b) + (2 * a * c) + (2 * b * c)}")

    if shape_input == "koule":
        r = float(input("Zadejte polomer r: "))
        print(f" Objem koule je {4/3 * math.pi * r * r * r} a povrch koule je  {4 * math.pi * r * r}")

    if shape_input == "ctverec":
        a= float(input("Zadejte hodnotu a: "))
        print(f" Obvod ctverce je: {4 * a} a obsah ctverce je {a * a} ")

    if shape_input == "obdelnik":
        a= float(input("Zadejte hodnotu a: "))
        b= float(input("Zadejte hodnotu b: "))
        print(f" Obvod obdelniku je: {2 * (a + b)} a obsah obdelniku je {a * b} ")
        
    if shape_input == "kruh":
        r = float(input("Zadejte polomer r:"))
        print(f" Obvod kruhu je: {2 * math.pi * r} a obsah kruhu je {math.pi * r * r} ")

else:
    print("Teleso neni definovano.")
