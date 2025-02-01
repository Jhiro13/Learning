#NAMESPACE ES UN MAPEO DE NOMBRES A OBJETOS
dir(__builtins__)#por defecto
globals()#todo muestra
#namespace es local es para cada structura
locals()#cada una de las funciones
contador=0
def actualizar_cont():
    global contador#le indica que está en scope global
    contador+=1
actualizar_cont()
print(contador)
def act_cont():
    cont=1
    def func():
        nonlocal cont#le indica en el scope nolocal
        cont+=1
    func()
    print(cont)
act_cont()
#no es recomendado usar estas wbdas
recursos_ecosistema={
    "agua":1000,
    "alimento":800
}
def animal_interactua(tipo_animal, agua_consumir=None, alimento_consumir=None):
    global recursos_ecosistema
    if recursos_ecosistema["agua"]>0 and recursos_ecosistema["alimento"]>0:
        if tipo_animal=="herbivoro":
            recursos_ecosistema["agua"]-=agua_consumir
            recursos_ecosistema["alimento"]-=alimento_consumir
            print(f"Un herbivoro ha consumido {agua_consumir} unidades agua y {alimento_consumir} unidades de alimento")
            print(f"Estado actual del ecosistema: {recursos_ecosistema}")
        elif tipo_animal=="carnivoro":
            recursos_ecosistema["alimento"]-=alimento_consumir
            print(f"Un carnivoro ha consumido {alimento_consumir} unidades de alimento")
            print(f"Estado actual del ecosistema: {recursos_ecosistema}")
    else:
        print("Recursos insuficientes del ecosistema")
def lluvia(agua_llueve):
    global recursos_ecosistema
    recursos_ecosistema["agua"]+=agua_llueve
    print(f"¡Ha llovido! Se añadieron {agua_llueve} unidades de agua al ecosistema.")
print(f"Inicio del día en el ecosistema: {recursos_ecosistema}")
animal_interactua("herbivoro",200,100)
animal_interactua("carnivoro",alimento_consumir=50)
lluvia(200)
print(f"Fin del día en el ecosistema: {recursos_ecosistema}")