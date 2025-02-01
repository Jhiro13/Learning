def escribir_agenda(nombre_agenda, agenda_digital):
    agenda_fichero=open(nombre_agenda,'w')
    agenda_fichero.write(str(agenda_digital))
    agenda_fichero.close()
def leer_agenda(nombre_agenda):
    agenda_digital_lectura=open(nombre_agenda)
    agenda_digital=agenda_digital_lectura.readlines()
    agenda_digital_lectura.close()
    return eval(agenda_digital[0])#esa wbda de eval es para devolver un str a dict
def solicitar_contacto_nuevo():
    nombre=input("Introduce el nombre completo del contacto: ")
    direccion=input("Introduce la direcciond el contacto: ")
    email=input("Ingrese email del contacto: ")
    telefono=input("Ingrese telefono del contacto: ")
    contacto=dict(
        Nombre=nombre,
        Direccion=direccion,
        Email=email,
        Telefono=telefono
    )
    return contacto
def crear_contacto(agenda_digital, nuevo_contacto):
    agenda_digital[nuevo_contacto["Nombre"]]=dict(
        direccion=nuevo_contacto["Direccion"],
        email=nuevo_contacto["Email"],
        telefono=nuevo_contacto["Telefono"]
    )
    return agenda_digital
def consultar_contacto(agenda_digital):
    buscar=input("Introduce el nombre completo del contacto a buscar: ")
    print(f"---{buscar}---\nDirección: {agenda_digital[buscar]["direccion"]}\nEmail: {agenda_digital[buscar]["email"]}\nTeléfono: {agenda_digital[buscar]["telefono"]}")
agenda_digital=leer_agenda("agenda.txt")
nuevo_contacto=solicitar_contacto_nuevo()
agenda_digital=crear_contacto(agenda_digital, nuevo_contacto)
escribir_agenda("agenda.txt", agenda_digital)
consultar_contacto(agenda_digital)
#DETALLANDO LA FUNCION OPEN()