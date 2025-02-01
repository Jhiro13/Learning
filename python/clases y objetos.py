class Coche:
    def velocidad_maxima(self,velocidad): #a todos los métodos se le debe asignar el parámetro self (referencia a la clase)
        print(f"velocidad máxima: {velocidad}")
coche1=Coche()
coche1.velocidad_maxima(30)
class Carro:
    velocidad=150
    def velocidad_maxima(self):
        print(f"velocidad máxima: {self.velocidad}")
bmw=Carro()
bmw.velocidad_maxima()
#Metodo __init__() -> constructor: asigna valores específicos del objeto y se ejecuta automat al instanciar
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
    def actualizar_motor(self, motor_nuevo):
        self._motor=motor_nuevo
skyline=Carrito(260,"plateado",0.15)
skyline.presentar_coche()
skyline.actualizar_motor("rompeogts 2000")
skyline.presentar_coche()
#Getters y Setters: son para acceder y modificar atributos privados y se definen en la clase