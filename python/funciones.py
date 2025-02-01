name="cisneros sanchez"
n=len(name)#contador de caracteres de string
nombre_planeta="Saturno"
distancia=65
#FUNCIONES PERSONALIZADAS
def distancia_planeta(v1 ,v2):
    print(f"Nombre del planeta: {nombre_planeta}\nDistancia al planeta: {distancia} millones de km")
distancia_planeta(nombre_planeta, distancia)
#TIPOS DE ARGUMENTOS
#---ARGUMENTOS PALABRAS CLAVE: mas que todo sirve para no fijarse tanto en el orden de la funcion
a="hola kbro"
b="adios kbro"
def myfunction(x1,x2):
    print(x1)
    print(x2)
myfunction(x1=b, x2=a)
#ARGUMENTO por defecto
def myfunction(x1,x2="hola mundo"):#le puedes poner solo un argumento y por defecto ya se queda con el segundo arg
    print(x1)
    print(x2)
#si le pones return, te devuelvo tanto el valor y hace que continue el código desde la parte en la que se invocó
#los docstrings se usan para documentar dentro de funciones, usualmente usando """texto"""
#Es una buena practica definir una funcion
def docs():
    """"Te devuelve una cadena cualquiera"""
    print("Lily and Yofre")
docs()
def generar_mensaje(nombre, mensaje="Bienvenido al curso de Python"):
    """
    Genera un mensaje personalizado combinando el nombre del destinatario y un mensaje opcional.
 
    Args:
        nombre (str): El nombre de la persona a la que se dirigirá el mensaje.
        mensaje (str, opcional): El contenido del mensaje que se quiere enviar. Por defecto es "Bienvenido a Python".
 
    Returns:
        str: Un mensaje personalizado que incluye el nombre y el mensaje proporcionado.
    """
    mensaje_completo = f"¡Hola, {nombre}! {mensaje}"
    return mensaje_completo
#Esta es la estructura de un docstring
# Llamada a la función con un nombre específico
nombre_ejemplo = "Jhiro"
resultado = generar_mensaje(nombre_ejemplo)
 
# Mostrar el resultado
#------------------------------------------------------------------------------------------------------------
#help(int)--> brinda información de un objeto
type(nombre_ejemplo)#--> indica el tipo de objeto
id(nombre_ejemplo)#--> brinda el identificador
def contar_caracteres(str1):
    cont=len(str1)
    print(f"La frase {str1} tiene {cont} caracteres")
def convertir_numero(int1):
    cadena=str(int1)
    flotante=float(int1)
    print(f"Entero: {int1}, Tipo: {type(int1)}")
    print(f"Cadena: {cadena}, Tipo: {type(cadena)}")
    print(f"Flotante: {flotante}, Tipo: {type(flotante)}")
contar_caracteres("'Tres tristes tigres comen trigo en un trigal'")
convertir_numero(10)