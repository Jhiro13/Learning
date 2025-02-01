dic={
    "Nombre":"Jhiro",
    "Apellido":"Cisneros",
    "Pais":"Peru",
    "Ciudad":"San Marcos"
}
print(dic)
dic2=dict(
    Nombre="Yofre",
    Apellido="Cisneros",
    Pais="Peru",
    Ciudad="Huari"
)
print(dic2["Apellido"])
#Ejercicio
perfil_laboral=dict(
    Nombre="Ana",
    Apellido="Pérez",
    Edad=30,
    Ciudad="Madrid",
    Experiencias=["Ingeniera de software en XYZ Corp", "Gerente de proyecto en ABC Inc"]
)
def agregar_experiencia(perfil_laboral, nueva_experiencia):
    perfil_laboral['Experiencias']=perfil_laboral['Experiencias']+[nueva_experiencia]
    return perfil_laboral
def generar_cv_reducido(perfil_laboral):
    print(f"CV de {perfil_laboral['Nombre']} {perfil_laboral['Apellido']}\nEdad: {perfil_laboral['Edad']}, Ciudad: {perfil_laboral['Ciudad']}\nExperiencia: {perfil_laboral['Experiencias']}")
n_experiencia="Jefe de proyecto en UNIMED"
cv_final=agregar_experiencia(perfil_laboral,n_experiencia)
generar_cv_reducido(cv_final)