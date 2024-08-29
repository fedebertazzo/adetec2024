from autos_model import Auto
from autos_data import lista_autos
from garage_model import Garage

lista_garage=[]
#Armar la lista según el diccionario en autos_data.py
for auto in lista_autos:
    auto_dominio = auto["dominio"]
    auto_marca = auto["marca"]
    auto_modelo = auto["modelo"]
    auto_color = auto["color"]
    nuevo_auto = Auto(auto_dominio,auto_marca,auto_modelo,auto_color)
    lista_garage.append(nuevo_auto)

#Crea el objeto garage
garage = Garage(lista_garage)

#Parámetro de salida del menú
salir= False

while salir==False:
    print("Seleccione una opción:")
    print("1 - Mostrar autos")
    print("2 - Agregar auto")
    print("3 - Eliminar auto")
    print("4 - Salir")
    opcion=int(input("Opción: "))
    if opcion==1:
        print("Tabla de autos:\n")
        garage.mostrar_autos()
    elif opcion == 2:
        print("Agregar auto:")
        nuevo_dominio=input("Indique el dominio del auto: ")
        nuevo_marca=input("Indique la marca: ")
        nuevo_modelo=input("Indique el modelo:")
        nuevo_color=input("Indique el color: ")
        print(f"El auto {nuevo_dominio}: {nuevo_marca} {nuevo_modelo} color {nuevo_color} será agregado...")
        while True:
            nuevo_pos= int(input("Indique la posición: "))
            try:
                garage.agregar_auto(Auto(nuevo_dominio, nuevo_marca, nuevo_modelo,nuevo_color),nuevo_pos)
                break
            except:
                print("No se pudo agregar el auto.")
    elif opcion == 3:
            garage.eliminar_auto()
    else:
        print("Adios!\n")
        salir=True
        # # break