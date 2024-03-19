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

# Funcion donde seteamos que caractes usar en nuestra clave (letras, numeros y/o simbolos)
def crear_clave():
    try:
        longitud = int(input("Ingrese la longitud deseada para la contraseña: "))
        
        if longitud <= 0:
            print("La longitud debe ser un numero positivo.")
            return
        
        letras = 'N'
        numeros = 'N'
        simbolos = 'N'

        while letras == 'N' and numeros == 'N' and simbolos == 'N':
            letras = input("Incluye letras (S/N): ").upper()
            while (letras != 'S' and letras != 'N'):
                letras = input("La respuesta debe ser S o N, reingrese: ").upper()

            numeros = input("Incluye numeros (S/N): ").upper()
            while (numeros != 'S' and numeros != 'N'):
                numeros = input("La respuesta debe ser S o N, reingrese: ").upper()

            simbolos = input("Incluye simbolos (S/N): ").upper()
            while (simbolos != 'S' and simbolos != 'N'):
                simbolos = input("La respuesta debe ser S o N, reingrese: ").upper()

            if letras == 'N' and numeros == 'N' and simbolos == 'N':
                print("No hay caracteres, numeros o simbolos para generar la contraseña\nReintente:")
        
        
        contrasena = generar_contrasena(longitud, letras, numeros, simbolos)
        print("Contraseña generada:", contrasena)
    except ValueError:
        print("Ingrese una longitud válida.")


# Verificamos que contiene la clave
def verificar_letras(clave):
    return all(c in string.ascii_letters for c in clave)

def verificar_numeros(clave):
    return all(c in string.digits for c in clave)

def verificar_simbolos(clave):
    return any(c in string.punctuation for c in clave)

def calcular_longitud(clave):
    return len(clave)


# Chequeamos la clave asignandole un valor numerico como resultado
def chequear_cleve(clave):

    seguridad = 0
    
    longitud = calcular_longitud(clave)
    seguridad += longitud * 4


    if verificar_letras(clave):
        seguridad += longitud
    if verificar_numeros(clave):
        seguridad += longitud
    if verificar_simbolos(clave):
        seguridad += longitud * 2
    
    if verificar_letras(clave) and not verificar_numeros(clave) and not verificar_simbolos(clave):
        seguridad -= longitud
    elif not verificar_letras(clave) and verificar_numeros(clave) and not verificar_simbolos(clave):
        seguridad -= longitud
    elif not verificar_letras(clave) and not verificar_numeros(clave) and verificar_simbolos(clave):
        seguridad -= longitud
    
    return seguridad


# Funcion principal, menu e inicio
def main():
    print("Bienvenido al KeyGey")
    print("Este programa te permite chequear o crear contraseñas seguras")
    while True:
        print("\n*** Menu principal ***")
        print("1- Chequear contraseña")
        print("2- Crear contraseña")
        print("3- Salir")
        opcion = int(input("Ingrese una opcion: "))

    
        if opcion == 1:
            print("Ingrese la contraseña que quiere chequear")
            clave = input("Contraseña: ")
            seguridad = chequear_cleve(clave)
            print(seguridad)
            if seguridad < 30:
                print(f"La contraseña \033[91m{clave}\033[0m es muy debil, mejor genera una nueva")
            elif seguridad < 35:
                print(f"La contraseña \033[91m{clave}\033[0m es medianamente debil, mejor genera una nueva")
            elif seguridad < 50:
                print(f"La contraseña \033[91m{clave}\033[0m es debil, mejor genera una nueva")
            elif seguridad < 55:
                print(f"La contraseña \033[93m{clave}\033[0m es mediana, se puede mejorar generando una nueva")
            elif seguridad < 80:
                print(f"La contraseña \033[92m{clave}\033[0m es fuerte, se puede generar una nueva mas robusta")
            elif seguridad < 100:
                print(f"La contraseña \033[92m{clave}\033[0m es bastante fuerte, pero si quieres una mucho mas robusta y segura la puedes generar")
            else:
                print(f"La contraseña \033[92m{clave}\033[0m es muy fuerte, se tardaria demasiado en desifrar")

        elif opcion == 2:
            crear_clave()

        elif opcion == 3:
            print("\nMuchas gracias")
            break
        
        else:
            print("\033[91m\n**** Opcion incorrecta ****"+"\033[0m")
    
if __name__ == "__main__":
    main()


