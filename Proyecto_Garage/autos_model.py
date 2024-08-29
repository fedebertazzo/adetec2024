class Auto:
    '''Crea el objeto auto con su marca, modelo y color''' 
    def __init__(self,auto_dominio:str,auto_marca,auto_modelo,auto_color="Blanco"):
        self.id=str(auto_dominio)
        self.marca = auto_marca
        self.modelo = auto_modelo
        self.color = auto_color
        self.tiene_luces= True
        self.esta_encendido =False

    def info(self):
        print(f"Dominio: {self.id}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")

    def arrancar(self):
        '''Cambia el estado del auto a encendido'''
        if self.esta_encendido == False:
            self.esta_encendido = True
            print("Auto arrancó")
        else:
            print("El auto ya esta encendido")
        

    def apagar(self):
        '''Cambia el estado del auto a apagado'''
        if self.esta_encendido == True:
            self.esta_encendido=False
            print("Auto se apagó")
        else:
            print("El auto no esta encendido")

    def get_color(self):
        '''Obtiene el color del auto'''
        print(f"El auto es de color {self.color}")
        return self.color
    
    def set_color(self,nuevo_color):
        '''Cambia el color del auto'''
        self.color = nuevo_color
        print(f"El nuevo color es {self.color}")


class Moto:
    pass