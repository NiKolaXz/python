temperatura = float(input("ingrese la temperatura faremheit"))

def convertir(temperatura):
    celcius = (temperatura - 32) * 5/9
    print(celcius)

    print(str(celcius) + "grados celcius")

convertir(temperatura)