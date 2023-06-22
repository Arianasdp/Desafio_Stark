
def menu() -> str:
    """menú de opciones
    
    returns:
        opción elegida (str)
    """
     
    print("""
    *** Menu de Opciones ***
    ----------------------------------------------
    1- Lista de héroes
    2- Lista de héroes con su altura
    3- Héroe más alto
    4- Héroe más bajo
    5- Altura promedio
    6- Informar nombres asociados a la máxima y mínima altura
    7- Informar héroe más y menos pesado
    8- Listado de nombres de superhéroes
    9- Listado de nombres de superheroínas
    10- Maximo o minimo de altura segun género
    11- Altura promedio de superheroes
    12- Altura promedio de superheroinas
    13- Informar nombres asociados a la máxima y mínima altura segun género
    14- Conteo de héroes según color de ojos
    15- Conteo de héroes según color de pelo
    16- Conteo de héroes según tipo de inteligencia
    17- Listado de héroes según color de ojos
    18- Listado de héroes según color de pelo
    19- Listado de héroes según tipo de inteligencia
    20- Salir
    """)

    opcion = (input("Ingrese opcion: ")) 

    return opcion  
  
def salir() -> str:
    """Confirmación de salida

    returns:
        opción elegida (str)
    """
    salir = input("Confirma salida? s/n: ")
    salir = salir.lower()
    while(salir != 's' and salir != 'n'):
        salir = input("Error. Confirma salida? s/n: ")
        salir = salir.lower()
    return salir

def submenu() -> int:
    """submenú de opciones
    
    returns:
        opción elegida (int)
    """

    print("""
    1- Superheroe mas alto
    2- Superheroina mas alta
    3- Superheroe mas bajo
    4- superheroina mas baja
    5- Salir
    """)
    opcion = (input("Ingrese opcion: ")) 
    if opcion.isdigit():

        opcion = int(opcion)

    else:

        opcion = -1 

    return opcion 

def esta_presente_en(lista: list, item: dict) -> bool:
    esta = False
    for elemento in lista:
        if(elemento == item):
            esta = True
            break
    return esta

def cargar_lista(lista_origen: list) -> list:
    """Carga la lista

    Args:
        lista_origen (list): lista a cargar

    returns:
        lista (list): lista cargada
    """
    lista = []
    for item in lista_origen:
        if(not esta_presente_en(lista, item)):
            lista.append(item)
    return lista
                  
def listar_heroes_general(lista: list) -> None:
    for personaje in lista:
        print(f"nombre: {personaje['nombre']}") 

def listar_heroes_genero(lista: list, genero: str) -> None:
    for personaje in lista:
        if(personaje["genero"] == genero):
            print(f"nombre: {personaje['nombre']}")

def listar_alturas(lista):
    """recorre la lista e imprime por pantalla las alturas de los héroes

    Args:
        lista (list): lista de héroes
    """
    for personaje in lista:
        print(f"nombre: {personaje['nombre']}, altura: {personaje['altura']:.5}")

def heroe_maximo_minimo(lista: list, key: str, criterio: bool) -> dict:
    """Recorre la lista y determina el héroe máximo o mínimo según la clave y el criterio que se le pasan

    Args:
        lista (list): lista a recorrer
        key (str): la clave del diccionario
        criterio (bool): determina si se busca el máximo o mínimo del héroe
    returns:
        heroe (dict): el héroe encontrado que compla con la clave y el criterio
    """
    heroe = lista[0]
    for personaje in lista:
        if((float(personaje[key]) >= float(heroe[key]) and criterio == True)
           or (float(personaje[key]) <= float(heroe[key]) and criterio == False)):
                    heroe = personaje

    return heroe

def heroe_genero_maximo_minimo(lista: list, key: str, criterio: bool, genero: str) -> dict:
    """Recorre la lista y determina el héroe máximo o mínimo según el género, la clave y el criterio que se le pasan,
        lo devuelve e imprime por consola el resultado
    Args:
        lista (list): lista a recorrer
        key (str): la clave del diccionario
        criterio (bool): determina si se busca el máximo o mínimo del héroe
        genero (str): determina los héroes a tomar en cuenta
    returns:
        heroe (dict): el héroe encontrado que compla con el género, la clave y el criterio
    """

    heroe = None

    for personaje in lista:
         if(personaje["genero"] == genero):
            heroe = personaje
            break
         
    if(heroe is None):
        heroe = {}
        return heroe 
    
    for personaje in lista:
        if((float(personaje[key]) >= float(heroe[key]) and criterio == True and personaje["genero"] == genero)
           or (float(personaje[key]) <= float(heroe[key]) and criterio == False and personaje["genero"] == genero)):
            heroe = personaje
    
    if criterio == True:
        if genero == "M":
            print(f"El heroe más alto es: {heroe['nombre']}")
        else:
            print(f"La heroína más alta es: {heroe['nombre']}")
    else:
        if genero == "M":
            print(f"El heroe más bajo es: {heroe['nombre']}")
        else:
            print(f"La heroína más baja es: {heroe['nombre']}")
    return heroe

def promedio(lista: list, key: str) -> float:  
    """Saca el promedio de lo que se le pase

    Args:
        lista (list): lista a recorrer
        key (str): la clave del diccionario a tomar en cuenta
    returns:
        promedio (float): el promedio
    """              
    acum = 0
    cont = 0
    promedio = 0
    for personaje in lista:
                acum += float(personaje[key])
                cont += 1

    promedio = acum / cont
    return promedio 

def promedio_segun_genero(lista: list, key: str, genero: str) -> float:   
    """Saca el promedio de lo que se le pase según el género

    Args:
        lista (list): lista a recorrer
        key (str): la clave del diccionario a tomar en cuenta
        genero (str): determina los héroes a tomar en cuenta
    returns:
        promedio (float): el promedio
    """               
    acum = 0
    cont = 0
    promedio = 0
    for personaje in lista:
                if(personaje["genero"] == genero):
                    acum += float(personaje[key])
                    cont += 1

    promedio = acum / cont
    return promedio 

def listar_por_caracteristica(lista: list, key: str, condicion: str) -> None:
    """Según la característica (la clave) y la condición divide a los héroes y devuelve el conteo o el listado

    Args:
        lista (list): lista a recorrer
        key (str): la clave del diccionario a tomar en cuenta
        condicion (str): determina si se devuelve la cantidad o la lista de héroes
        """

    caracteristicas = cargar_caracteristica(lista, key)
    key_titulo = key.upper()

    if condicion == "cantidad":
        
        print(" _________________________________________")
        print(f"|       {key_titulo:12}         |  CANTIDAD  |")
        print("|____________________________|____________|") 
        for carac in caracteristicas:
            contador = 0
            for heroe in lista:
                if heroe[key] == carac:
                    contador += 1
            print(f"| {carac:23}    |     {contador:2}     |")
            print("|____________________________|____________|")
    
    elif condicion == "listar":
         
         for carac in caracteristicas:
            print(f"{key_titulo}: {carac}")
            print(" ____________________________________________________________________________________________________________________________________________________________________")
            print("|            NOMBRE            |            IDENTIDAD            |    EMPRESA    | ALTURA |  PESO  | GE |        OJOS             |     PELO     |  FUERZA |    IQ   |")
            print("|______________________________|_________________________________|_______________|________|________|____|_________________________|______________|_________|_________|")
            for heroe in lista:
                if(heroe[key] == carac):
                    
                    print(f"| {heroe['nombre']:25}    | {heroe['identidad']:31} | {heroe['empresa']:13} | {float(heroe['altura']):6.2f} | {float(heroe['peso']):6.2f} | {heroe['genero']}  | {heroe['color_ojos']:23} | {heroe['color_pelo']:13}|  {float(heroe['fuerza']):6.2f} | {heroe['inteligencia']:7} |")
                    print("|______________________________|_________________________________|_______________|________|________|____|_________________________|______________|_________|_________|")
            print("")  


def cargar_caracteristica(lista: list, key: str) -> list:
    """Carga la lista de características

    Args:
        lista (list): lista a recorrer
        key (str): la clave del diccionario a tomar en cuenta
    returns:
        caracteristicas (list): lista cargada
    """
    caracteristicas = []
    for item in lista:
         item[key] = item[key].capitalize()
         if not esta_en_lista(caracteristicas, item[key]):
            if item[key] == "":
                item[key] = "None"
            caracteristicas.append(item[key])
                   
    return caracteristicas

def esta_en_lista(lista: list, item: str) -> bool:
    """Determina si el item pasado por parámetro está en la lista

    Args:
        lista (list): lista 
        item (str): item a confirmar

    returns:
        esta (bool): True o False dependiendo si el item existe o no en la lista
    """
    esta = False
    for elemento in lista:
        if(elemento == item):
            esta = True
            break
    return esta