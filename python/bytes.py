cadena_bytes=b'\x02\x1f'
print(type(cadena_bytes))
print(bin(543))#->devulve string: 0b1000011111
print(hex(543))#->devuelve string: 0x21f
numero=int.from_bytes(cadena_bytes)
print(numero)
cadena_bytes2=bytes(3)
print(cadena_bytes2)
texto="hola yofre"
textO_bytes=b'hola yofre'
nombre=b'\x4A\x48\x49\x52\x4f'
print(nombre)
#PARA INDEXACIÓN LO DEVUELVE COMO INT, PERO PARA SLICING O STRIDE LO DEVUELVE COMO STRING(PERO EN BYTES)
cadena_bytes2=bytearray(b'\x02\x1f')#ahora si es mutable
print(ord('J'))#muestra al numero entero asociado segun ascii
#EJERCICIO
mensaje=b'Este es un mensaje secreto'
def crear_codigo_secreto(mensaje):
    repr_hex=mensaje[::2]
    repr_hex=repr_hex.hex()#esto es porque los bytes no pueden ser interpretados como int para la funcion
    repr_bin=mensaje[::2]
    repr_bin_primero, repr_bin_ultimo=bin(repr_bin[0]), bin(repr_bin[-1])
    repr_hex=str(repr_hex)
    repr_bin=str(repr_bin)
    repr_bin_primero=str(repr_bin_primero)
    repr_bin_ultimo=str(repr_bin_ultimo)
    conca=repr_hex+repr_bin+repr_bin_primero+repr_bin_ultimo
    return conca
print(f"Mensaje original: {mensaje}\nMensaje codificado: {crear_codigo_secreto(mensaje)}")