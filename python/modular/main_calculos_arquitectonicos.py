from calculos_arquitectonicos import area_rectangulo, volumen_cilindro, area_circulo
def planificar_proyecto(largoA, anchoA, radioB, alturaB, radioC):
    print(f"Área de la sala principal: {area_rectangulo(largoA, anchoA)} metros cuadrados.")
    print(f"Volúmen de la piscina: {volumen_cilindro(radioB, alturaB)} metros cúbicos.")
    print(f"Área del jardín circular: {area_circulo(radioC)} metros cuadrados.")
print("---------- Informe proyecto ----------")
planificar_proyecto(20, 15, 5, 2, 10)
print("--------------------------------------")