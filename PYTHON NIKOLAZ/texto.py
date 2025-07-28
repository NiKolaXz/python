texto = "Hola, mundo"
print(texto.startswith("Hola"))  # True
print(texto.startswith("Mundo"))  # False

texto = "archivo.txt"
print(texto.endswith(".txt"))  # True
print(texto.endswith(".jpg"))  # False


texto = "12345"
print(texto.isdigit())  # True
print("123a".isdigit())  # False


texto = "Python"
print(texto.isalpha())  # True
print("Python3".isalpha())  # False


texto = "Python3"
print(texto.isalnum())  # True
print("Python 3".isalnum())  # False (espacio no es alfanumérico)

texto = "bienvenidos a python"
print(texto.title())  # "Bienvenidos A Python"


texto = "python es genial"
print(texto.capitalize())  # "Python es genial"


# Crear una tabla de traducción
tabla = str.maketrans("aeiou", "12345")

# Aplicar la traducción a una cadena
texto = "hola amigos"
nuevo_texto = texto.translate(tabla)

print(nuevo_texto)  # h4l1 1m3g4s
    