def saludar(nombre, apellido, edad):
    print(f"¡Hola, {nombre} {apellido} tienes {edad} años!")

nombre = input("ingrese nombre")
apellido = input("ingrese apellido")
edad = input("ingrese su edad")

# Llamar a la función con un argumento
saludar(nombre, apellido, edad)  # Imprime "¡Hola, Ana!"


def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)  # Imprime 8