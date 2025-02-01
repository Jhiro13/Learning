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
#generamos una clase herencia de carrito, hereda atributos y metodos
class CarritoElectrico(Carrito):
    def __init__(self, velocidad, color, consumo, combustible):
        super().__init__(velocidad, color, consumo)#super() hace referencia a la clase padre
        self.combustible=combustible
tesla=CarritoElectrico(200, "negro", 15, "0.17 Kwh/100km")
tesla.presentar_coche()
#ALGO ASI ES LA IDEA, SE ENTIENDE
"DEFINICION DE ATRIBUTOS Y METODOS DE LA CLASE HIJA"
class Animal:
    def __init__(self, nombre, especie, edad, Habitat):
        self.nombre=nombre
        self.especie=especie
        self.edad=edad
        self.Habitat=Habitat
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nEspecie: {self.especie}\nEdad: {self.edad}\nHabitad: {self.Habitat.tipo_habitad}\nTemperatura: {self.Habitat.temperatura}")
class Habitat:
    def __init__(self, tipo_habitad, temperatura):        
        self.tipo_habitad=tipo_habitad
        self.temperatura=temperatura
class Mamifero(Animal):
    def __init__(self, nombre, especie, edad, habitat, tipo_pelaje):
        super().__init__(nombre, especie, edad, habitat)
        self.tipo_pelaje=tipo_pelaje
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de pelaje: {self.tipo_pelaje}")
class Ave(Animal):
    def __init__(self, nombre, especie, edad, habitat, tipo_plumaje):
        super().__init__(nombre, especie, edad, habitat)
        self.tipo_plumaje=tipo_plumaje
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de plumaje: {self.tipo_plumaje}")
class Zoologico:
    def __init__(self, nombre):
        self.nombre=nombre
        self.animales=[]
    def añadir_animal(self, Animal):
        self.animales.append(Animal)
    def mostrar_animales(self):
        print(f"Animales en {self.animales}")
        for i in self.animales:
            Animal.mostrar_info(self)
# Ejemplo de uso
zoologico = Zoologico("ZooFantástico")
 
# Definición de dos habitats
habitat1 = Habitat("Sabana", "Cálido")
habitat2 = Habitat("Bosque", "Templado")
 
# Definición de dos animales
leon = Mamifero("Simba", "León", 5, habitat1, "Corto")
canario = Ave("Piolín", "Canario", 2, habitat2, "Suave")
 
zoologico.añadir_animal(leon)
zoologico.añadir_animal(canario)
zoologico.mostrar_animales()
#LO DE ARRIBA ES INTENTO MIO
class Animal:
    """ Representa un animal genérico.
    """
    def __init__(self, nombre, especie, edad, habitat):
        """
        Inicializa un objeto Animal con nombre, especie, edad y hábitat.
 
        Args:
            nombre (str): El nombre del animal.
            especie (str): La especie del animal.
            edad (int): La edad del animal en años.
            habitat (Habitat): El hábitat del animal.
        """
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.habitat = habitat
 
    def mostrar_info(self):
        """Imprime la información del animal."""
        print(f"--> Nombre: {self.nombre}\nEspecie: {self.especie}\nEdad: {self.edad}\nHábitat: {self.habitat.tipo_habitat}, {self.habitat.temperatura}")
 
class Habitat:
    """ Representa el hábitat de un animal.
    """
    def __init__(self, tipo, temperatura):
        """
        Inicializa un objeto Habitat con tipo y temperatura.
 
        Args:
            tipo (str): El tipo de hábitat.
            temperatura (str): La temperatura del hábitat.
        """
        self.tipo_habitat = tipo
        self.temperatura = temperatura
 
class Mamifero(Animal):
    """ Representa un mamífero, subclase de Animal.
    """
    def __init__(self, nombre, especie, edad, habitat, tipo_pelaje):
        """
        Inicializa un objeto Mamifero con nombre, especie, edad, hábitat y tipo de pelaje.
 
        Args:
            nombre (str): El nombre del mamífero.
            especie (str): La especie del mamífero.
            edad (int): La edad del mamífero en años.
            habitat (Habitat): El hábitat del mamífero.
            tipo_pelaje (str): El tipo de pelaje del mamífero.
        """
        super().__init__(nombre, especie, edad, habitat)
        self.tipo_pelaje = tipo_pelaje
 
    def mostrar_info(self):
        """Imprime la información del mamífero, incluido el tipo de pelaje."""
        super().mostrar_info()
        print(f"Tipo de pelaje: {self.tipo_pelaje}")
 
class Ave(Animal):
    """ Representa un ave, subclase de Animal.
    """
    def __init__(self, nombre, especie, edad, habitat, tipo_plumaje):
        """
        Inicializa un objeto Ave con nombre, especie, edad, hábitat y tipo de plumaje.
 
        Args:
            nombre (str): El nombre del ave.
            especie (str): La especie del ave.
            edad (int): La edad del ave en años.
            habitat (Habitat): El hábitat del ave.
            tipo_plumaje (str): El tipo de plumaje del ave.
        """
        super().__init__(nombre, especie, edad, habitat)
        self.tipo_plumaje = tipo_plumaje
    
    def mostrar_info(self):
        """Imprime la información del ave, incluido el tipo de plumaje."""
        super().mostrar_info()
        print(f"Tipo de plumaje: {self.tipo_plumaje}")
 
class Zoologico:
    """ Representa un zoológico.
    """
    def __init__(self, nombre):
        """
        Inicializa un objeto Zoologico con nombre.
 
        Args:
            nombre (str): El nombre del zoológico.
        """
        self.nombre = nombre
        self.animales = []
 
    def añadir_animal(self, animal):
        """
        Añade un animal al zoológico.
 
        Args:
            animal (Animal): El animal a añadir.
        """
        self.animales.append(animal)
 
    def mostrar_animales(self):
        """Imprime la información de todos los animales en el zoológico."""
        print(f"Animales en {self.nombre}:")
        for animal in self.animales:
            animal.mostrar_info()
 
 
# Ejemplo de uso
zoologico = Zoologico("ZooFantástico")
 
# Definición de dos habitats
habitat1 = Habitat("Sabana", "Cálido")
habitat2 = Habitat("Bosque", "Templado")
 
# Definición de dos animales
leon = Mamifero("Simba", "León", 5, habitat1, "Corto")
canario = Ave("Piolín", "Canario", 2, habitat2, "Suave")
 
zoologico.añadir_animal(leon)
zoologico.añadir_animal(canario)
zoologico.mostrar_animales()