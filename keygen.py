# Importar las bibliotecas necesarias
import random
import string

# Función para generar contraseñas
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation     # Se obtienen todos los caracteres (letras mayusc y minusc + numeros + simbolos)
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

# Función principal
def main():
    try:
        longitud = int(input("Ingrese la longitud deseada para la contraseña: "))
        if longitud <= 0:
            print("La longitud debe ser un número positivo.")
            return

        contrasena = generar_contrasena(longitud)
        print("Contraseña generada:", contrasena)
    except ValueError:
        print("Ingrese una longitud válida.")

if __name__ == "__main__":
    main()


