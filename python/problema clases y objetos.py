class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo=titulo
        self.autor=autor
        self.isbn=isbn
        self.disponible=True
    def informacion(self):
        print(f"Titulo: {self.titulo}\nAutor: {self.autor}\nISBN: {self.isbn}\nDisponible: {self.disponible}")
    def prestar_libro(self):
        if self.disponible==True:
            self.disponible=False
            print(f"El libro {self.titulo} ha sido prestado\n")
            Libro.informacion(self)
        else:
            print("Este libro ya está prestado")
    def devolver_libro(self):
        if self.disponible==False:
            self.disponible=True
            print(f"El libro {self.titulo} ha sido devuelto a la biblioteca\n")
            Libro.informacion(self)
        else:
            print("Este libro ya está en la biblioteca")
libro1=Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", "978-0747532743")
libro2=Libro("1984", "George Orwell", "978-0451524935")
libro1.prestar_libro()
libro1.informacion()
libro1.devolver_libro()
libro1.informacion()
libro2.prestar_libro()
libro2.informacion()
libro2.prestar_libro()