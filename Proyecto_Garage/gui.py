from tkinter import *

color_fondo="#375362"

class GarageUI:
    def __init__(self,garage) -> None:
        self.garage=garage
        self.ventana=Tk()
        self.ventana.title("Mi garage")
        self.ventana.config(padx=20,pady=20,bg=color_fondo)

        self.titulo= Label(text="Seleccione una opción:", fg="white",bg=color_fondo)
        self.titulo.grid(row=0)

        self.boton_mostrar = Button(text="Mostrar vehículos", command=self.ventana_mostrar)
        self.boton_mostrar.grid(row=1,pady=10)

        self.boton_agregar = Button(text="Agregar vehículo")
        self.boton_agregar.grid(row=2,pady=10)

        self.boton_eliminar = Button(text="Quitar vehículo")
        self.boton_eliminar.grid(row=3,pady=10)


        

        self.ventana.mainloop()

    def ventana_mostrar(self):
        self.ventana2=Tk()
        self.ventana2.title("Listado de vehículos")
        
        #Crea el titulo
        self.titulo= Label(self.ventana2,text="Listado de vehículos:", fg="white",bg=color_fondo)
        self.titulo.grid(row=0)

        #Crea el espacio de texto
        self.panel=Canvas(self.ventana2,bg="white",width=600,height=600)
        self.tabla = self.panel.create_text(300,300,text=self.garage.mostrar_autos(),fill=color_fondo, font=("arial",20,"italic"))
        self.panel.grid(row=1)
        
        def cerrar_ventana():
            self.ventana2.destroy()


        self.boton_volver=Button(self.ventana2, text="Cerrar", command=cerrar_ventana)
        self.boton_volver.grid(row=2)
        self.ventana2.mainloop()

    
