import random
from tarfile import LENGTH_LINK
import time
from turtle import delay

letras = ["a","b","c","d","e","f","g","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numeros = ["1","2","3","4","5","6","7","8","9","0"]
simbolos = ["!",".","&","_","+","$","?","(","{","}","&"]

print("This console based program was made by C0MPL3X and it is completly free and open source!\nFor more details about this project check my portofolio at: http://samuelsampaio.great-site.net/?i=1 \n")
b = input("Press any key to continue to the app\n")

def inic():
    numCaracteres = input("Password lenght: ")
    print("Do you want your password to have: ")
    pLetras = upper(input("Letters?[Y/N] "))
    if (pLetras == "Y"):
        pMaiusculas = upper(input("Capital Letters?[Y/N] "))
    pNum = upper(input("Numbers?[Y/N] "))
    pSimb = upper(input("Simbols?[Y/N] "))
    password = ""
    gerarPasse(numCaracteres,pLetras,pMaiusculas,pNum,pSimb,password)

def upper(a):
    return a.upper()

def gerarPasse(numCaracteres,pLetras,pMaiusculas,pNum,pSimb,password):
    #tudo
    if (pLetras == "Y" and pMaiusculas == "Y" and pNum == "Y" and pSimb == "Y"):
        for i in range(int(numCaracteres)):
            lns = random.randint(0,2)
            if (lns == 0):
                maiuscula = random.randint(0,1)
                if (maiuscula == 0):
                    password = password + upper(letras[random.randint(0,len(letras)-1)])
                else:
                    password = password + letras[random.randint(0,len(letras)-1)]
            elif (lns == 1):
                password = password + numeros[random.randint(0,len(numeros)-1)]
            elif (lns == 2):
                password = password + simbolos[random.randint(0,len(simbolos)-1)]
    #tudo menos maiusculas
    elif (pLetras == "Y" and pMaiusculas == "N" and pNum == "Y" and pSimb == "Y"):
        for i in range(int(numCaracteres)):
            lns = random.randint(0,2)
            if (lns == 0):
                password = password + letras[random.randint(0,len(letras)-1)]
            elif (lns == 1):
                password = password + numeros[random.randint(0,len(numeros)-1)]
            elif (lns == 2):
                password = password + simbolos[random.randint(0,len(simbolos)-1)]
    #tudo menos simbolos
    elif (pLetras == "Y" and pMaiusculas == "Y" and pNum == "Y" and pSimb == "N"):
        for i in range(int(numCaracteres)):
            lns = random.randint(0,1)
            if (lns == 0):
                maiuscula = random.randint(0,1)
                if (maiuscula == 0):
                    password = password + upper(letras[random.randint(0,len(letras)-1)])
                else:
                    password = password + letras[random.randint(0,len(letras)-1)]
            elif (lns == 1):
                password = password + numeros[random.randint(0,len(numeros)-1)]
    #tudo menos numeros
    elif (pLetras == "Y" and pMaiusculas == "Y" and pNum == "N" and pSimb == "Y"):
        for i in range(int(numCaracteres)):
            lns = random.randint(0,1)
            if (lns == 0):
                maiuscula = random.randint(0,1)
                if (maiuscula == 0):
                    password = password + upper(letras[random.randint(0,len(letras)-1)])
                else:
                    password = password + letras[random.randint(0,len(letras)-1)]
            elif (lns == 1):
                password = password + simbolos[random.randint(0,len(simbolos)-1)]
    #tudo menos maiusculas e numeros
    elif (pLetras == "Y" and pMaiusculas == "N" and pNum == "N" and pSimb == "Y"):
        for i in range(int(numCaracteres)):
            lns = random.randint(0,1)
            if (lns == 0):
                password = password + letras[random.randint(0,len(letras)-1)]
            elif (lns == 1):
                password = password + simbolos[random.randint(0,len(simbolos)-1)]
    #tudo menos maiusculas e simbolos
    elif (pLetras == "Y" and pMaiusculas == "N" and pNum == "Y" and pSimb == "N"):
        for i in range(int(numCaracteres)):
            lns = random.randint(0,1)
            if (lns == 0):
                password = password + letras[random.randint(0,len(letras)-1)]
            elif (lns == 1):
                password = password + numeros[random.randint(0,len(numeros)-1)]
    #só letras com maiusculas
    elif (pLetras == "Y" and pMaiusculas == "Y" and pNum == "N" and pSimb == "N"):
        for i in range(int(numCaracteres)):
            maiuscula = random.randint(0,1)
            if (maiuscula == 0):
                password = password + upper(letras[random.randint(0,len(letras)-1)])
            else:
                password = password + letras[random.randint(0,len(letras)-1)]
    #so letras sem maisculas
    elif (pLetras == "Y" and pMaiusculas == "N" and pNum == "N" and pSimb == "N"):
        for i in range(int(numCaracteres)):
            password = password + letras[random.randint(0,len(letras)-1)]
    #so numeros e simbolos
    elif(pLetras == "N" and pNum == "Y" and pSimb == "Y"):
        for i in range(int(numCaracteres)):
            lns = random.randint(0,1)
            if (lns == 0):
                password = password + numeros[random.randint(0,len(numeros)-1)]
            elif (lns == 1):
                password = password + simbolos[random.randint(0,len(simbolos)-1)]
    #so simbolos
    elif(pLetras == "N" and pNum == "N" and pSimb == "Y"):
        for i in range(int(numCaracteres)):
            password = password + simbolos[random.randint(0,len(simbolos)-1)]
    #so numeros
    elif(pLetras == "N" and pNum == "Y" and pSimb == "N"):
        for i in range(int(numCaracteres)):
            password = password + numeros[random.randint(0,len(numeros)-1)]
    #nada
    elif(pLetras == "N" and pNum == "N" and pSimb == "N"):
        print("You anwsered 'N' on all options please try again with at least one 'Y'")
        inic()
    #caso o utilizador nao insira corretamente os dados
    elif(pLetras != "N" and pLetras != "Y" or pNum != "N" and pNum != "Y" or pSimb != "N" and pSimb != "Y"):
        print("You have entered wrong characters please try again!")
        inic()
    
    printp(password)



def printp(password):
    print("\nPassword generated: " + password + "\n")
    pRepetir = input("Generate another password?[Y/N] ")
    if (upper(pRepetir) == "Y"):
        inic()
    else:
        print("\nThanks for using this app, i hope it helps you stay protected!")
        time.sleep(2)
        print("\nConsole will automatically close in 5 seconds")
        time.sleep(5)
        
    
inic()
