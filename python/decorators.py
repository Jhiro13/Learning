#un decorator permite modificar funciones sin alterar el codigo de la funcion original
#python trata como un objeto a las funciones
n=4
def funcion():
    print("holi brou")
def decorator(func):
    def wrapper():
        if n<=5:
            func()
        else:
            print("Me llega al webo")
    return wrapper        
new=decorator(funcion)
new()
#Syntactic sugar: realiza la asignación
def decorator1(func):
    def wrapper():
        if n<=5:
            func()
        else:
            print("Me llega al webo")
    return wrapper
@decorator1
def funcion1():
    print("Holi brooou")
funcion1()
#DECORATORS EN LAS CLASES
#@property: permite definir metodos en una clase para consultar y modificar atributos
class Carrito:
    """Esta clase representa un coche"""
    def __init__(self, velocidad, color, consumo):
        """Inicializa los atributos de instancia.
        
        Argumentos posicionales:
        velocidad -- int indica la velocidad máxima del coche
        color -- str indica el color del coche
        consumo -- float indica el consumo en litros por cada Km
        """
        self.velocidad=velocidad
        self.color=color
        self.consumo=consumo
        self.km_actuales=0#se puede tener atributos por defecto y modificarlos (mala practica) <obj>.<atrb>=nuevo_valor
        self._motor="terreneitor 3000"#el self._ hace que se vuelva privado, por defecto es publico
    def presentar_coche(self):
        """Muestra especificaciones del coche"""
        print(f"La velocidad máxima es: {self.velocidad}\nColor: {self.color}\nConsumo (L/Km): {self.consumo}\nMotor: {self._motor}")
    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self, motor_nuevo):
        self._motor=motor_nuevo
#PROBLEMA
def formato_notificacion(func):
    def wrapper(self, plataforma):#si te das cuenta recibe los mismo argumentos que notificar_evento
        print(f"***** NUEVO EVENTO en {plataforma} *****")
        func(self,plataforma)
        print(f"***** FIN DEL EVENTO EN {plataforma} *****")
    return wrapper
class NotificadorRedSocial:
    def __init__(self):
        self.evento="Lanzamiento de un nuevo libro"
    @formato_notificacion
    def notificar_evento(self, plataforma):
        if plataforma=="Twitter":
            print(f"Twett: {self.evento}")
        elif plataforma=="Instagram":
            print(f"Story: {self.evento}")
        elif plataforma=="Facebook":
            print(f"Post en Facebook:{self.evento}")
        else:
            print("Plataforma no soportada")
notificador=NotificadorRedSocial()
notificador.notificar_evento("Twitter")#lo puedes hacer con un for pendejo
notificador.notificar_evento("Instagram")
notificador.notificar_evento("Facebook")
notificador.notificar_evento("LinkedIn")