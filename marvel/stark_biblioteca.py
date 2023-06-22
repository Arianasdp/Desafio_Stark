from funciones_stark import *
import os

def stark_normalizar_datos(lista: list) -> None:
    """Convierte los datos correspondientes en int o float

    Args:
        lista (list): lista a recorrer
    """

    datos_actualizados = False

    keys = ["altura", "peso", "fuerza"]

    if(len(lista) == 0):
        print("Error: Lista de héroes vacía")
    else:
        for key in keys:
            for heroe in lista:
                if(type(heroe[key]) == str):
                    if("." in heroe[key]):
                        heroe[key] = float(heroe[key])
                    else:
                        heroe[key] = int(heroe[key])
                    datos_actualizados = True
    
    if(datos_actualizados):
        print("Datos normalizados")

def obtener_nombre(heroe: dict) -> str:
    """Obtiene el nombre del héroe (de tipo diccionario) que se le pasa

    Args:
        heroe (dict): diccionario a recorrer
    returns:
        nombre (str): nombre del héroe
    """

    key = "nombre"
    nombre = ""

    if key in heroe:
        nombre = f"Nombre: {heroe[key]}"

    return nombre

def imprimir_dato(string: str) -> None:
    """Imprime la cadena que se le pasa

    Args:
        string (str): cadena a imprimir
    """

    print(string)

def stark_imprimir_nombre_heroes(lista: list) -> int:
    """Imprime por pantalla los nombres de los héroes de la lista y devuelve 0 si salió todo bien y -1 si no

    Args:
        lista (list): lista a recorrer
    returns:
        todoOk (int): -1 (no entró) o 0 (entró) dependiendo si entra en la validación
    """

    todoOk = -1

    if(len(lista) > 0):
        for heroe in lista:
            nombre = obtener_nombre(heroe)
            imprimir_dato(nombre)
        todoOk = 0

    return todoOk

def obtener_nombre_y_dato(heroe: dict, key: str) -> str:
    """Obtiene el nombre y dato que se le pida a través de la clave del héroe que se le pasa

    Args:
        heroe (dict): diccionario con el que se trabaja 
        key (str): clave a tomar en cuenta
    returns:
        datos (str): nombre y dato especificado por la clave del héroe
    """
    
    nombre = obtener_nombre(heroe)
    if(type(key) == float):
        datos = nombre + f" | {key}: {heroe[key]:.2f}" #solo va a entrar acá si normalizamos los datos
    else:
        datos = nombre + f" | {key}: {heroe[key]}"

    return datos

def stark_imprimir_nombres_alturas(lista: list) -> int:
    """Imprime por pantalla los nombres y alturas de los héroes de la lista y devuelve 0 si salió todo bien y -1 si no

    Args:
        lista (list): lista a recorrer
    returns:
        todoOk (int): -1 (no entró) o 0 (entró) dependiendo si entra en la validación
    """

    todoOk = -1

    if(len(lista) > 0):
        for heroe in lista:
            datos = obtener_nombre_y_dato(heroe, "altura")
            imprimir_dato(datos)
        todoOk = 0

    return todoOk

def calcular_max(lista: list, key: str) -> dict:
    """Recorre la lista y calcula el héroe con el valor máximo según la clave que se le pasa

    Args:
        lista (list): lista a recorrer
        key (str): la clave a tomar en cuenta
    returns:
        heroe (dict): el héroe con el valor máximo según la clave ingresada
    """

    heroe = lista[0]

    for personaje in lista:
        if(personaje[key]) >= (heroe[key]):
            heroe = personaje
    
    return heroe

def calcular_min(lista: list, key: str) -> dict:
    """Recorre la lista y calcula el héroe con el valor mínimo según la clave que se le pasa

    Args:
        lista (list): lista a recorrer
        key (str): la clave a tomar en cuenta
    returns:
        heroe (dict): el héroe con el valor mínimo según la clave ingresada
    """

    heroe = lista[0]

    for personaje in lista:
        if(personaje[key]) <= (heroe[key]):
            heroe = personaje
    
    return heroe

def calcular_max_min_dato(lista: list, key: str, criterio: str) -> dict:
    """Recorre la lista y calcula el héroe con el valor máximo o mínimo según la clave y el criterio que se le pasa

    Args:
        lista (list): lista a recorrer
        key (str): la clave a tomar en cuenta
        criterio (str): lo que determina si se calcula el valor máximo o mínimo
    returns:
        heroe (dict): el héroe con el valor máximo/mínimo según la clave y criterio ingresados
    """
    
    heroe = lista[0]

    if(criterio == "maximo"):
        heroe = calcular_max(lista, key)
    elif(criterio == "minimo"):
        heroe = calcular_min(lista, key)

    return heroe

def stark_calcular_imprimir_heroe(lista: list, criterio: str, key: str) -> int:
    """Recorre la lista y calcula el héroe con el valor máximo o mínimo según la clave y el criterio que se le pasa, 
    valida que la lista no esté vacía, caso en el que imprime el resultado, y en el caso contrario no imprime nada y devuelve -1

    Args:
        lista (list): lista a recorrer
        criterio (str): lo que determina si se calcula el valor máximo o mínimo
        key (str): la clave a tomar en cuenta
    returns:
        todoOk (int): -1 (no entró) o 0 (entró) dependiendo si entra en la validación
    """

    todoOk = -1

    if(len(lista) > 0):
        heroe = calcular_max_min_dato(lista, key, criterio)
        heroe = obtener_nombre_y_dato(heroe, key)
        if criterio == "maximo":
            imprimir_dato( f"Mayor {key}: " + heroe)
        elif criterio == "minimo":
            imprimir_dato( f"Menor {key}: " + heroe)
        todoOk = 0

    return todoOk

def sumar_dato_heroe(lista: list, key: str) -> int | float:
    """Recorre la lista y realiza una suma de lo que se le pase a través de la clave, 
    mientras dentro contenga un entero o un flotante

    Args:
        lista (list): lista a recorrer
        key (str): la clave a tomar en cuenta
    returns:
        suma (int | float): devuelve la suma de los enteros o flotantes que haya acumulado, dependiendo lo que
        se le pasó a través de la clave (o 0 si no entra en la validación)
    """

    suma = 0

    for heroe in lista:
        if type(heroe) == dict and len(heroe) > 0 and key in heroe and (type(heroe[key]) == int or type(heroe[key]) == float): 
            suma += heroe[key]

    return suma

def dividir(dividendo: int | float, divisor: int) -> float:
    """Realiza una división validando que el divisor no sea 0

    Args:
        dividendo (int): es dividido por el divisor
        divisor (int): divide al dividendo
    returns:
        resultado (float): el resultado de la división
    """

    if(divisor == 0):
        resultado = 0
    else:
        resultado = dividendo / divisor   
    
    return resultado

def calcular_promedio(lista: list, key: str) -> float:
    """Calcula el promedio de lo que se le pasa a través de las funciones sumar_dato_heroe y dividir

    Args:
        lista (list): lista con la que se trabaja
        key (str): la clave a tomar en cuenta
    returns:
        promedio (float): el resultado del cálculo
    """

    suma = sumar_dato_heroe(lista, key)
    promedio = dividir(suma, len(lista))

    return promedio

def stark_calcular_imprimir_promedio_altura(lista: list) -> int:
    """Calcula el promedio de las alturas de la lista y lo imprime por pantalla, habiendo previamente validado que
    la lista no estuviese vacía, caso contrario no hace nada y devuelve -1 

    Args:
        lista (list): lista a recorrer
    returns:
        todoOk (int): -1 (no entró) o 0 (entró) dependiendo si entra en la validación
    """

    todoOk = -1

    if(len(lista) > 0):
        promedio = calcular_promedio(lista, "altura")
        imprimir_dato((f"La altura promedio es de {promedio:.2f} centimetros"))
        todoOk = 0

    return todoOk

def imprimir_menu() -> None:
    """Imprime por pantalla el menú de opciones
    """
    
    imprimir_dato("""*** Stark industries: Menú de Opciones ***
    ----------------------------------------------
    1- Lista de heroes
    2- Lista de heroes con su altura
    3- Heroe mas alto
    4- Heroe mas bajo
    5- Altura promedio
    6- Informar nombres asociados a la maxima y minima altura
    7- Informar heroe mas y menos pesado
    8- Listado de nombres de superheroes
    9- Listado de nombres de superheroinas
    10- Maximo o minimo de altura segun genero
    11- Altura promedio de superheroes
    12- Altura promedio de superheroinas
    13- Informar nombres asociados a la maxima y minima altura segun genero
    14- Conteo de heroes segun color de ojos
    15- Conteo de heroes segun color de pelo
    16- Conteo de heroes segun tipo de inteligencia
    17- Listado de heroes segun color de ojos
    18- Listado de heroes segun color de pelo
    19- Listado de heroes segun tipo de inteligencia
    20- Salir
    """)

def validar_entero(numeros: str) -> bool:
    """Recibe una cadena y valida si es de números enteros

    Args:
        numeros (str): cadena a validar
    returns:
        valido (bool): True si entra en la validación y False en el caso contrario
    """

    valido = False
    
    if numeros.isdigit():
        valido = True
    
    return valido 

def stark_menu_principal() -> int:
    """Imprime el menú de opciones, valida que la opción sea un entero y la devuelve de ser así, en el caso 
    contrario devuelve -1
    
    returns:
        opción (str): opción elegida si entra en la validación, -1 si no
    """

    imprimir_menu()

    opcion = (input("Ingrese opcion: "))
    if validar_entero(opcion):

        opcion = int(opcion)

    else:

        opcion = -1 

    return opcion

def stark_marvel_app(heroes: list) -> None:
    """Presenta un bucle con las opciones del menú principal de héroes y permite elegir la que se desee y devuelve
    la información correspondiente mediante la utilización de las funciones previamente creadas

    Args:
        lista (list): lista con la que se trabaja
    """

    heroes = cargar_lista(heroes)
    stark_normalizar_datos(heroes)

    heroe_alto = heroes[0]
    heroe_bajo = heroes[0]
    heroina_alta = heroes[0]
    heroina_baja = heroes[0]
    flag_alto = False
    flag_alta = False
    flag_bajo = False
    flag_baja = False

    while True:

        os.system("cls")

        match(stark_menu_principal()):

            case 1:

                stark_imprimir_nombre_heroes(heroes)

            case 2:
                    
                stark_imprimir_nombres_alturas(heroes)

            case 3:
                    
                stark_calcular_imprimir_heroe(heroes, "maximo", "altura")

            case 4:
                    
                stark_calcular_imprimir_heroe(heroes, "minimo", "altura")
                
            case 5:
                    
                stark_calcular_imprimir_promedio_altura(heroes)

            case 6:

                stark_calcular_imprimir_heroe(heroes, "maximo", "altura")
                stark_calcular_imprimir_heroe(heroes, "minimo", "altura")

            case 7:

                stark_calcular_imprimir_heroe(heroes, "maximo", "peso")
                stark_calcular_imprimir_heroe(heroes, "minimo", "peso")

            case 8:

                listar_heroes_genero(heroes, "M")
            
            case 9:

                listar_heroes_genero(heroes, "F")

            case 10:

                while True:

                    os.system("cls")

                    match(submenu()):
                        case 1:

                            heroe_alto = heroe_genero_maximo_minimo(heroes, "altura", True, "M")  
                            flag_alto = True
                            
                        case 2:

                            heroina_alta = heroe_genero_maximo_minimo(heroes, "altura", True, "F")
                            flag_alta = True
                            
                        case 3:

                            heroe_bajo = heroe_genero_maximo_minimo(heroes, "altura", False, "M")
                            flag_bajo = True
                            
                        case 4:

                            heroina_baja = heroe_genero_maximo_minimo(heroes, "altura", False, "F")
                            flag_baja = True
                            
                        case 5:

                            salida = salir()
                            if (salida == 's'):
                                break

                        case -1: 

                            print("Esa no es una opcion válida")

                        case _: 

                            print("Esa no es una opcion válida")
                            
                    os.system("pause")

            case 11:

                promedio = promedio_segun_genero(heroes, "altura", "M")
                print(f"La altura promedio de los heroes es de {promedio:.5} centimetros")

            case 12:

                promedio = promedio_segun_genero(heroes, "altura", "F")
                print(f"La altura promedio de los heroes es de {promedio:.5} centimetros")

            case 13:
                    if flag_alto and flag_alta and flag_baja and flag_bajo:
                        print(f"El heroe mas alto es {heroe_alto['nombre']}, con {heroe_alto['altura']:.5} centimetros")
                        print(f"El heroe mas bajo es {heroe_bajo['nombre']}, con {heroe_bajo['altura']:.5} centimetros")
                        print(f"La heroina mas alta es {heroina_alta['nombre']}, con {heroina_alta['altura']:.5} centimetros")
                        print(f"La heroina mas baja es {heroina_baja['nombre']}, con {heroina_baja['altura']:.5} centimetros")
                    else:
                        print("Ingrese a la opción 10 y calcule las alturas primero")

            case 14:

                listar_por_caracteristica(heroes, "color_ojos", "cantidad")

            case 15:  

                listar_por_caracteristica(heroes, "color_pelo", "cantidad")    

            case 16:

                listar_por_caracteristica(heroes, "inteligencia", "cantidad")

            case 17:

                listar_por_caracteristica(heroes, "color_ojos", "listar")

            case 18:

                listar_por_caracteristica(heroes, "color_pelo", "listar")

            case 19:

                listar_por_caracteristica(heroes, "inteligencia", "listar")

            case 20:

                salida = salir()
                if (salida == 's'):
                    break

            case -1: 

                print("Esa no es una opcion valida")
            
            case _: 

                print("Esa no es una opcion valida")

        os.system("pause")

def extraer_iniciales(nombre_heroe: str) -> str:
    """Recibe un nombre completo y extrae sus iniciales, validando que la cadena no esté vacía y que no se incluya
    la palabra "the" en las iniciales extraídas

    Args:
        nombre_heroe (str): cadena con la que se trabaja
    returns:
        iniciales (str): las iniciales extraídas
    """
    
    iniciales = ""

    nombre_heroe = nombre_heroe.replace("-"," ")
    nombres = nombre_heroe.split(" ")

    if nombre_heroe == "":
        iniciales = "N/A"

    for nombre in nombres:
        nombre = nombre.lower()
        if nombre != "the":
            for i in range(len(nombre)):
                if i == 0:
                    iniciales += nombre[i].upper() + "."

    return iniciales

def definir_iniciales_nombre(heroe: dict) -> bool:
    """Valida que lo que se le pasa sea un diccionario y agrega la clave iniciales al diccionario

    Args:
        heroe (dict): diccionario con el que se trabaja
    returns:
        todoOk (bool): True si entra en la validación y False en el caso contrario
    """

    todoOk = False

    if(type(heroe) == dict):

        if "nombre" in heroe:

            iniciales = extraer_iniciales(heroe['nombre'])
            heroe["iniciales"] = iniciales
            todoOk = True

    return todoOk

def agregar_iniciales_nombre(heroes: list) -> bool:
    """Valida que lo que se le pasa sea de tipo lista y que la misma no esté vacía, y agrega la clave iniciales a
    todos los diccionarios de la lista

    Args:
        heroes (list): lista a recorrer
    returns:
        todoOk (bool): True si entra en la validación y False en el caso contrario
    """
    
    todoOk = False

    if type(heroes) == list and len(heroes) > 0:

        for heroe in heroes:

            iniciales_definidas = definir_iniciales_nombre(heroe)

            if not iniciales_definidas:
                print("El origen de datos no contiene el formato correcto")
                break
            else:
                todoOk = True
                
    return todoOk

def stark_imprimir_nombres_con_iniciales(heroes: list) -> None:
    """Imprime por pantalla los nombres de los héroes de la lista junto con sus iniciales

    Args:
        heroes (list): lista a recorrer
    """

    if type(heroes) == list and len(heroes) > 0:

        agregar_iniciales_nombre(heroes)
        
        for heroe in heroes:
            print(f"* {heroe['nombre']} ({heroe['iniciales']})")

def generar_codigo_heroe(id_heroe: int, genero_heroe: str) -> str:
    """Genera un código en base al id y el género del héroe que se le pasa si los datos son válidos, en el caso
    contrario devuelve en string "N/A"

    Args:
        id_heroe (int): el id del héroe
        genero_heroe (str): el género del héroe
    returns:
        codigo (str): el código generado
    """

    codigo = ""

    genero_heroe = genero_heroe.upper()

    if type(id_heroe) == int and genero_heroe != None and (genero_heroe == 'M' or genero_heroe == 'F' or genero_heroe == 'NB'):
        
        cadena_id = str(id_heroe)

        len_id = len(cadena_id) + len(genero_heroe) + 1

        if len_id < 10:

            resto = 10 - len_id
            cadena_id = '0' * resto + cadena_id 

        codigo = f"{genero_heroe}-{cadena_id}"

    else:

        codigo = "N/A"

    return codigo

def agregar_codigo_heroe(heroe: dict, id_heroe: int) -> bool:
    """Agrega el código generado a través de generar_codigo_heroe al diccioanario que se le pasa y retorna si
    todo salió bien o no

    Args:
        heroe (dict): diccionario con el que se trabaja
        id_heroe (int): el id del héroe
    returns:
        todoOk (bool): True si entra en la validación y False en el caso contrario
    """

    todoOk = False
    
    if len(heroe) > 0: 
        codigo = generar_codigo_heroe(id_heroe,heroe["genero"])
        if len(codigo) == 10:
            heroe["codigo_heroe"] = codigo
            todoOk = True

    return todoOk

def stark_generar_codigos_heroes(lista_heroes: list) -> None:
    """Genera el código de todos los héroes de la lista mientras que la lista sea mayor a 0, caso contrario
    imprime un mensaje de error

    Args:
        lista_heroes (list): lista a recorrer
    """

    if len(lista_heroes) > 0:
        i = 1
        for heroe in lista_heroes:
            if(type(heroe) == dict and "genero" in heroe):
                agregar_codigo_heroe(heroe, i)
                i += 1
            else:
                print("El orige de datos no contiene el formato correcto")

def sanitizar_entero(numero_str: str) -> int:
    """Convierte la cadena de números positivos que se le pasa a entero y lo devuelve, si es que es válida, 
    caso contrario devuelve -1 si ocurre un ValueError, -2 si los números son menores a 0 y -3 si ocurre otro error

    Args:
        numero_str (str): cadena con la que se trabaja
    returns:
        numero_retornado (int): el número convertido a entero, -1 (ValueError), -2 (si es un número negativo) 
        o -3 (si ocurre otro error)
    """

    try:
        numero_str = numero_str.strip()
        numero = int(numero_str)
        if numero < 0:
            numero_retornado = -2
        else:
            numero_retornado = numero
    except ValueError:
        numero_retornado = -1
    except:
        numero_retornado = -3

    return numero_retornado

def sanitizar_flotante(numero_str: str) -> int | float:
    """Convierte la cadena de números positivos que se le pasa a flotante y lo devuelve, si es que es válida, 
    caso contrario devuelve -1 si ocurre un ValueError, -2 si los números son menores a 0 y -3 si ocurre otro error

    Args:
        numero_str (str): cadena con la que se trabaja
    returns:
        numero_retornado (int | float): el número convertido a flotante, -1 (ValueError), 
        -2 (si es un número negativo) o -3 (si ocurre otro error)
    """
    
    try:
        numero_str = numero_str.strip()
        numero = float(numero_str)
        if numero < 0:
            numero_retornado = -2
        else:
            numero_retornado = numero
    except ValueError:
        numero_retornado = -1
    except:
        numero_retornado = -3

    return numero_retornado

def sanitizar_string(valor_str: str, valor_por_defecto: str = "-") -> str:
    """Se asegura que la cadena que recibe no tenga números y la devuelve habiendo reemplazado la barra, si es que
    tiene alguna, por un espacio, si contiene números retorna "N/A" y si está vacía retorna el valor_por_defecto

    Args:
        valor_str (str): cadena con la que se trabaja
        valor_por_defecto (str): valor ya seteado en "-"
    returns:
        retorno (str): la cadena si es válida, "N/A" si no, y el valor_por_defecto si está vacía
    """

    retorno = " "
    contiene_numero = False
    
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()

    for caracter in valor_str:

        if caracter.isnumeric():
                
            contiene_numero = True
            break
                
        else:
            
            if "/" in valor_str:
                
                valor_str = valor_str.replace("/", " ")    

            retorno = valor_str.lower()

    if not valor_str:

        retorno = valor_por_defecto.lower()

    if contiene_numero:

        retorno = "N/A"

    return retorno

def sanitizar_dato(heroe: dict, clave: str, tipo_dato: str) -> bool:
    """Dependiendo el tipo de dato que reciba, lo conviete a entero, flotante, o chequea que sea un string válido.
    Valida que los datos sean los correspondientes, d elo contrario imprime mensajes de error y no realiza la sanitización
    del dato

    Args:
        heroe (dict): diccionario con el que se trabaja 
        clave (str): clave a tomar en cuenta
        tipo_dato (str): si el dato es string, entero o flotante
    returns:
        todoOk (bool): True si entra en la validación y False en el caso contrario
    """

    tipo_dato = tipo_dato.lower()
    tipos_validos = ["string", "entero", "flotante"]
    todoOk = False

    if tipo_dato not in tipos_validos:

        print("Tipo de dato no reconocido")
    
    elif clave not in heroe:

        print("La clave especificada no existe en el héroe")
    
    else:
        if tipo_dato == "entero":
            heroe[clave] = sanitizar_entero(heroe[clave])
        elif tipo_dato == "flotante":
            heroe[clave] = sanitizar_flotante(heroe[clave])
        else:
            heroe[clave] = sanitizar_string(heroe[clave])
        todoOk = True

    return todoOk

def stark_normalizar_datos_2(lista_heroes: list) -> None:
    """Convierte los datos correspondientes en int o float, valida los strings e imprime un mensaje avisando que
    todo salió bien, habiendo validado que la lista no esté vacía. Caso contrario imprime un mensaje de error y
    no sanitiza los datos

    Args:
        lista_heroes (list): lista a recorrer
    """

    claves_str = ["color_ojos", "color_pelo", "inteligencia"]
    claves_float = ["altura", "peso"]
    claves_int = ["fuerza"]

    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            for clave in heroe:
                if clave in claves_str:
                    sanitizar_dato(heroe, clave, "string")
                elif clave in claves_float:
                    sanitizar_dato(heroe, clave, "flotante")
                elif clave in claves_int:
                    sanitizar_dato(heroe, clave, "entero")
        print("Datos normalizados")
    else:
        print("error: Lista de héroes vacía")

def generar_indice_nombres(lista_heroes: list) -> list:
    """Genera un índice de todos los nombres de los héroes separados por un guión, habiendo validado que la lista
    que recibe no esté vacía

    Args:
        lista_heroes (list): lista a recorrer
    returns:
        nombres (list): la lista de nombres de los héroes
    """

    nombres = []

    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            if type(heroe) == dict and "nombre" in heroe:
                nombres_heroe = heroe["nombre"].replace("-"," ").split(" ")
                nombres += nombres_heroe
            else:
                print("El origen de datos no contiene el formato correcto")
    else:
        print("El origen de datos no contiene el formato correcto")
    
    return nombres 

def stark_imprimir_indice_nombre(lista_heroes: list) -> None:
    """Imprime el índice de todos los nombres de los héroes separados por un guión

    Args:
        lista_heroes (list): lista con la que se trabaja
    """

    nombres = generar_indice_nombres(lista_heroes)
    nombres = " ".join(nombres).replace(" ", "-")
    print(nombres)

def convertir_cm_a_mtrs(valor_cm: float) -> int | float:
    """Convierte el flotante en cm que recibe a mtrs, retornándolo si pasa la validación, caso contrario retorna
    -1 si el número es menor a 0 o si ocurre un TypeError 

    Args:
        valor_cm (float): flotante en centímetros a convertir en metros
    returns:
        numero_a_retornar (int | float): el flotante en mtrs correspondiente, o -1 si es un número negativo o 
        ocurre un TypeError
    """

    try:
        numero_a_retornar = float(valor_cm)
        if valor_cm > 0:
            numero_a_retornar /= 100  
        else:
            numero_a_retornar = -1
    except TypeError:
        numero_a_retornar = -1
    
    return numero_a_retornar

def generar_separador(patron: str, largo: int, imprimir: bool = True) -> str:
    """Genera un separador en base al patrón que recibe, el largo que se le da, y se lo imprime automáticamente,
    a menos que la variable imprimir se cambie a False, validando que el patrón tenga un largo mayor a 0 y menor a 3, 
    y el largo que determina el tamaño del separador no sea mayor a 236 ni menor a 1

    Args:
        patron (str): patrón base del separador a ser generado
        largo (int): el largo del separador
        imprimir (bool): ya seteado en True para imprimir el separador por pantalla
    returns:
        string (str): el separador generado, o "N/A" de no ser válido
    """

    string = ""
    
    if (len(patron) > 0 and len(patron) < 3) and (largo > 0 and largo < 236):
    
        string = patron * largo
    
    else:

        string = "N/A"

    if imprimir:
        print(string)
        
    return string

def generar_encabezado(titulo: str) -> str:
    """Genera un encabezado en base al título que reciba

    Args:
        titulo (str): cadena con la que se trata
    returns:
        encabezado (list): título + separador
    """

    encabezado = generar_separador("*", 140, False) + "\n" + titulo.upper() + "\n" + generar_separador("*", 140, False)

    return encabezado

def imprimir_ficha_heroe(heroe: dict) -> None:
    """Recibe el héroe con el que va a trabajar y le genera su ficha en base a sus datos y la muestra por pantalla

    Args:
        heroe (dict): diccionario con el que se trabaja
    """

    string = generar_encabezado("principal") + "\n"
    string += f"NOMBRE DEL HÉROE: {heroe.get('nombre')} ({heroe.get('iniciales')})\n"
    string += f"IDENTIDAD SECRETA: {heroe.get('identidad')}\n"
    string += f"CONSULTORA: {heroe.get('empresa')}\n"
    string += f"CÓDIGO DE HÉROE: {heroe.get('codigo_heroe')}\n"
    string += generar_encabezado("físico") + "\n"
    altura_str = str(convertir_cm_a_mtrs(heroe.get('altura', 0)))
    if altura_str != '-1' and altura_str != '0':
        altura_entera, altura_decimal = altura_str.split(".")
        altura_decimal = altura_decimal[:2]
        altura = f"{altura_entera},{altura_decimal}"
        string += f"ALTURA: {altura} Mtrs.\n"
    else:
        string += f"ALTURA: {heroe.get('altura')} Cm.\n"
    peso_entero, peso_decimal = str((heroe.get('peso', 0))).split(".")
    peso_decimal = peso_decimal[:2]
    peso = f"{peso_entero},{peso_decimal}"
    string += f"PESO: {peso} Kg.\n"
    string += f"FUERZA: {heroe.get('fuerza')} N \n"
    string += generar_encabezado("señas particulares") + "\n"
    string += f"COLOR DE OJOS: {heroe.get('color_ojos')}\n"
    string += f"COLOR DE PELO: {heroe.get('color_pelo')}\n"
    string += f"INTELIGENCIA: {heroe.get('inteligencia')}\n"

    imprimir_dato(string)

def stark_navegar_fichas(lista_heroes: list) -> None:
    """Navega a través de las fichas de los héroes, mostrándolas según la opción que elija el usuario

    Args:
        lista_heroes (dict): lista de héroes con la que se trabaja
    """

    i = 0
    total = len(lista_heroes)
    agregar_iniciales_nombre(lista_heroes)

    while True:

        os.system("cls")

        imprimir_ficha_heroe(lista_heroes[0])

        opcion = submenu_fichas()

        if opcion == '1':
                
            i -= 1
            if i < 0:
                i = total - 1
            imprimir_ficha_heroe(lista_heroes[i])    

        elif opcion == '2':
                
            i += 1
            if i > total - 1:
                i = 0
            imprimir_ficha_heroe(lista_heroes[i])

        elif opcion.upper() == 'S':

            salida = salir()
            if (salida == 's'):
                break
            
        else:

            print("Esa no es una opcion válida")

        os.system("pause")

def submenu_fichas() -> str:
    """menú de opciones
    
    returns:
        opción elegida (str)
    """

    imprimir_dato(""" Menú de fichas de los héroes
    [ 1 ] Ir a la izquierda
    [ 2 ] Ir a la derecha
    [ S ] Salir """)

    opcion = (input("Ingrese opcion: "))

    return opcion

def imprimir_menu_2() -> None:
    """muestra por pantalla el menú de opciones
    """

    imprimir_dato("""   Menú de opciones - Stark Industries
1 - Imprimir la lista de nombres junto con sus iniciales
2 - Generar códigos de héroes
3 - Normalizar datos
4 - Imprimir índice de nombres
5 - Navegar fichas
S - Salir
____________________________________________________________
    """)

def stark_menu_principal_2() -> str: 
    """menú de opciones
    
    returns:
        opción elegida (str)
    """

    imprimir_menu_2()

    opcion = (input("Ingrese opcion: "))

    return opcion

def stark_marvel_app_3(lista_heroes: list) -> None:
    """Presenta un bucle con las opciones del menú principal de héroes y permite elegir la que se desee y devuelve
    la información correspondiente mediante la utilización de las funciones previamente creadas

    Args:
        lista_heroes (list): lista con la que se trabaja
    """

    heroes = cargar_lista(lista_heroes)
    
    flag_codigos = False
    flag_datos = False


    while True:

        os.system("cls")

        match(stark_menu_principal_2().upper()):

            case '1':

                stark_imprimir_nombres_con_iniciales(heroes)

            case '2':

                stark_generar_codigos_heroes(heroes)
                print(f"Los códigos fueron correctamente generados, el primer código es: {heroes[0]['codigo_heroe']}")
                flag_codigos = True

            case '3':

                stark_normalizar_datos_2(heroes)
                flag_datos = True

            case '4':

                stark_imprimir_indice_nombre(heroes)

            case '5':

                if not flag_datos and not flag_codigos:
                    print("Se mostrará una versión desactualizada de las fichas, para actualizarla ingrese las opciones 2 y 3")
                    os.system("pause")
                stark_navegar_fichas(heroes)

            case 'S':

                salida = salir()
                if (salida == 's'):
                    break

            case _:

                print("Esa no es una opcion válida")

        os.system("pause")
