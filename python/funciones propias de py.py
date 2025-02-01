#CASO PRÁCTICO
def cabecera():
    print("""
 ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗    ██╗███╗   ██╗███████╗
██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝    ██║████╗  ██║██╔════╝
██║     ███████║█████╗  ██║     █████╔╝     ██║██╔██╗ ██║█████╗  
██║     ██╔══██║██╔══╝  ██║     ██╔═██╗     ██║██║╚██╗██║██╔══╝  
╚██████╗██║  ██║███████╗╚██████╗██║  ██╗    ██║██║ ╚████║██║     
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝                                                                                                                                                                                                 
""")
print("Desarrollador: Jhiro Cisneros Sánchez")
cabecera()
def hash_text_e():
    textoe=input("Ingrese una cadena de texto que emitió: ")
    valore=hash(textoe)
    return valore
def hash_text_r():
    textor=input("Ingrese una cadena de texto que recibió: ")
    valorr=hash(textor)
    return valorr
valE=hash_text_e()
valR=hash_text_r()
if valE==valR:
    print("El mensaje se transmitió con éxito")
else:
    print("El mensaje ha sido modificado") 
