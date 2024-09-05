from prettytable import PrettyTable

class ErrorEspacioGarage(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class Garage:
    def __init__(self,lista_garage,capacidad=6) -> None:
        self.capacidad=capacidad
        if self.condicion(lista_garage):
            self.garage_lista = lista_garage
            self.garage_dic={}
            for i in range(self.capacidad):
                try:
                    self.garage_dic[str(i)]=self.garage_lista[i]
                except:
                    self.garage_dic[str(i)]=False
        else:
            raise ErrorEspacioGarage("La lista de autos es mayor a la capacidad del garage!")
        
    def condicion(self,l):
        return len(l) <= self.capacidad

    def mostrar_autos(self):
        '''Muestra una tabla con los autos en el garage'''
        tabla = PrettyTable()
        tabla.field_names = ["Ubicacion","Dominio","Marca","Modelo","Color"]
        for pos in self.garage_dic:
            if self.garage_dic[pos] == False:
                tabla.add_row([pos,"-","-","-","-"])
            else:
                tabla.add_row([pos,self.garage_dic[pos].id,self.garage_dic[pos].marca,self.garage_dic[pos].modelo,self.garage_dic[pos].color])
        print(tabla)


        lista_valores_auto=[]
        for obj_auto in self.garage_lista:
            lista_valores_auto.append([obj_auto.id,",", obj_auto.marca,"," ,obj_auto.modelo,",", obj_auto.color])
        # print(lista_valores_auto)
        return lista_valores_auto

    def eliminar_auto(self):
        '''Elimina un auto del garage'''
        self.mostrar_autos()
        pos=input("Ingrese la ubicación del auto a eliminar: ")
        try:
            if pos in self.garage_dic:
                if self.garage_dic[pos]==False:
                    print("Aqui no hay ningun auto!")
                else:
                    self.garage_dic[str(pos)]=False
                    self.mostrar_autos()
            else:
                print("La ubicación no existe!")
        except:
            print("ERROR! La ubicación no existe")
    
    
    
    def agregar_auto(self,auto,pos):
        '''Agrega un auto en una posición'''
        if self.garage_dic[str(pos)] == False:
            self.garage_dic[str(pos)]=auto
            self.mostrar_autos()
        else:
            print("No se pudo agregar auto, la ubicación esta ocupada.")
            raise ValueError