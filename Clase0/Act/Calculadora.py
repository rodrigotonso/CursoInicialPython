'''
La computadora no puede trabajar con las cosas en el aire, 
le tenemos que decir que guarde en algun lugar de la memoria lo que necesitamos
por lo que usaremos variables, constantes, etc. para que la computadora sepa donde ir a buscar 
'''

'''
Python está pensado como un lenguaje simple por lo que no exige que crees las variables antes de usarlas
Es importante aclarar que muchos otros lenguajes si lo exigen y además exigen que digas el tipo (int, float, string, etc)
https://j2logo.com/python/tutorial/tipos-de-datos-basicos-de-python/
'''

# Aclarado lo anterior empezamos a realizar la calculadora

# Pido los números con los que se va a operar

'''
Le digo a Python que intente hacer un input (entrada) de lo que el usuario escribe en el teclado
Ese input lo guarda como tipo float (forma en la que en computación se representan los decimales +info buscar coma flotante en wiki)
¿Pero qué pasa si el usuario escribe letras o nada? se rompería la ejecución del programa.
para que eso no pase le digo que si hay una excepción (un error), le avise al usuario.
'''
try:
    n1 = float(input("Introduce el primer número: ") )
    n2 = float(input("Introduce el segundo número: ") )
except ValueError as err:
    print('format errado') # Mensaje de error


while True:
    print("""
    ------------------------------
    ¿Qué operación desea realizar?
    
    1) Suma
    2) Resta
    3) Multiplicación
    4) División
    5) Cambiar los números elegidos
    6) Salir
    """)
    opcion = int(input("Elige una opción: ") )

    if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de",n1,"+",n2,"es igual a",n1+n2)
    elif opcion == 2:
        print(" ")
        #ToDo: Hacer esto
    elif opcion == 3:
        print(" ")
        #ToDo: Hacer esto
    elif opcion == 4:
        print(" ")
        #ToDo: Hacer esto
    elif opcion == 5:
        print(" ")
        #ToDo: Hacer esto
    elif opcion == 6:
        break
    else:
        print("Opción incorrecta")