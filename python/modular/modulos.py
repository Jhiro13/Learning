import mimodulo
#importar objetos nada mas
from mimodulo import funcion, coche
from mimodulo import *
#ahora con alias o AKA
import mimodulo as mm
from mimodulo import funcion as fuc
#paquete
from paquete.paquetes import func
if __name__=='__main__': #-> esta wbda permite ejecutar solo el script donde se encuentra lo importado, más no desde donde se encuentra (evita duplicar)
    print(mimodulo.texto)
    funcion("chanchito contento")
    coche1=coche()
    print(mm.lista)
    fuc("chanchito triste")
    func()