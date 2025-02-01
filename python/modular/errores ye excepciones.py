#excepciones gestionan los errores que surgen en el codigo(para controlar errores que emergentes)
#errores de sintaxis: cuando la sentencia no es sintácticamente válida y no se pueden controlar
#las excepciones si pueden ser gestionados o ignorados
"""Listado de excepciones en Python
A continuación se muestra una lista de las excepciones más relevantes en Python 3 y una breve descripción en inglés:

Exception

Base class for all exceptions

StopIteration

Raised when the next() method of an iterator does not point to any object.

SystemExit

Raised by the sys.exit() function.

StandardError

Base class for all built-in exceptions except StopIteration and SystemExit.

ArithmeticError

Base class for all errors that occur for numeric calculation.

OverflowError

Raised when a calculation exceeds maximum limit for a numeric type.

FloatingPointError

Raised when a floating point calculation fails.

ZeroDivisonError

Raised when division or modulo by zero takes place for all numeric types.

AssertionError

Raised in case of failure of the Assert statement.

AttributeError

Raised in case of failure of attribute reference or assignment.

EOFError

Raised when there is no input from either the raw_input() or input() function and the end of file is reached.

ImportError

Raised when an import statement fails.

KeyboardInterrupt

Raised when the user interrupts program execution, usually by pressing Ctrl+c.

LookupError

Base class for all lookup errors.

IndexError

Raised when an index is not found in a sequence.

KeyError

Raised when the specified key is not found in the dictionary.

NameError

Raised when an identifier is not found in the local or global namespace.

UnboundLocalError

Raised when trying to access a local variable in a function or method but no value has been assigned to it.

EnvironmentError

Base class for all exceptions that occur outside the Python environment.

IOError

Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist.

OSError

Raised for operating system-related errors.

IndentationError

Raised when indentation is not specified properly.

SystemError

Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit.

SystemExit

Raised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit.

TypeError

Raised when an operation or function is attempted that is invalid for the specified data type.

ValueError

Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified.

RuntimeError

Raised when a generated error does not fall into any category.

NotImplementedError

Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented."""
try:
    print(x)
except NameError:
    x="chanchito feliz"
lista_colores=("rojo", "verde", "azul")
color="amarillo"
#if color not in lista_colores:
    #raise Exception(f"El color {color} no se encuentra en la lista")
#PRACTICA
menu={
    "Pizza Margarita":8.99, 
    "Hamburguesa Clásica":5.99, 
    "Ensalada César": 7.5, 
    "Agua mineral": 1.5
}
def realizar_pedido(alimento_seleccionado, dinero):
    for alimento, precio in menu.items():
        print(f"{alimento} ${precio}")
    try:
        if alimento_seleccionado not in menu:
            raise Exception("El alimento seleccionado no está en el menú")
        if dinero<menu[alimento_seleccionado]:
            raise Exception("No se disponen de suficientes fondos para realizar el pedido")
        coste_total=menu[alimento_seleccionado]
        print(f"Pedido realizado con éxito. Alimento seleccionado: {alimento_seleccionado}, Total a pagar: ${coste_total}")
    except ValueError as e:
        print(f"Error en el pedido: {e}")
realizar_pedido("Pizza Margarita", 10)
realizar_pedido("Pizza Margarita", 2)
realizar_pedido("Sandwich Mixto", 10)