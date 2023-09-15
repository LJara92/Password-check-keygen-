# Importar las bibliotecas necesarias
import random
import string

# Función para generar contraseñas
def generar_contrasena(longitud, letras, numeros, simbolos):

    # Asiganamos en la varible caracteres, los que definio el usuario
    caracteres = ''
    if letras == 'S':
        caracteres += string.ascii_letters
    if numeros == 'S':
        caracteres += string.digits
    if simbolos == 'S':
        caracteres += string.punctuation
    
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

# Función principal
def main():
    try:
        longitud = int(input("Ingrese la longitud deseada para la contraseña: "))
        
        if longitud <= 0:
            print("La longitud debe ser un número positivo.")
            return
        
        # Definimos que caracteres vamos a usar, letras, numeros y simbolos
        letras = input("Incluye letras (S/N): ").upper()
        while (letras != 'S' and letras != 'N'):
            letras = input("La respuesta debe ser S o N, reingrese: ").upper()

        numeros = input("Incluye numeros (S/N): ")
        while (numeros != 'S' and numeros != 'N'):
            numeros = input("La respuesta debe ser S o N, reingrese: ").upper()

        simbolos = input("Incluye simbolos (S/N): ")
        while (simbolos != 'S' and simbolos != 'N'):
            simbolos = input("La respuesta debe ser S o N, reingrese: ").upper()
        

        contrasena = generar_contrasena(longitud, letras, numeros, simbolos)
        print("Contraseña generada:", contrasena)
    except ValueError:
        print("Ingrese una longitud válida.")

if __name__ == "__main__":
    main()


