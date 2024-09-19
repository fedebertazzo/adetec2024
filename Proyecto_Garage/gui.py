from tkinter import *
import tkinter.ttk as ttk
import autos_model


color_fondo="#375362"

class GarageUI:
    def __init__(self,garage) -> None:
        self.garage=garage
        self.ventana=Tk()
        self.ventana.title("Mi garage")
        self.ventana.config(padx=20,pady=20,bg=color_fondo)

        self.titulo= Label(text="Seleccione una opción:", fg="white",bg=color_fondo)
        self.titulo.pack(pady=5)

        self.boton_mostrar = Button(text="Mostrar vehículos", command=self.ventana_mostrar)
        self.boton_mostrar.pack(pady=5)

        self.boton_agregar = Button(text="Agregar vehículo", command=self.ventana_agregar)
        self.boton_agregar.pack(pady=5)

        self.boton_eliminar = Button(text="Quitar vehículo", command=self.ventana_quitar)
        self.boton_eliminar.pack(pady=5)

        self.ventana.mainloop()

    def ventana_mostrar(self):
        self.ventana2=Tk()
        self.ventana2.title("Listado de vehículos")
        # self.ventana2.geometry("600x600")
        
        #Crea el titulo
        self.titulo= Label(self.ventana2,text="Listado de vehículos:", fg="white",bg=color_fondo)
        self.titulo.pack()      

        lista_autos= Variable(self.ventana2)
        lista_autos.set(self.garage.mostrar_autos())
        lista_mostrar=Listbox(self.ventana2,listvariable=lista_autos,width=50)
        lista_mostrar.pack(pady=5)
        
        def cerrar_ventana():
            self.ventana2.destroy()

        self.boton_volver=Button(self.ventana2, text="Cerrar", command=cerrar_ventana)
        self.boton_volver.pack()
        self.ventana2.mainloop()
    
    def ventana_agregar(self):
        self.ventana3=Tk()
        self.ventana3.title("Agregar vehículo")
              
        #Crea el titulo
        self.titulo= Label(self.ventana3,text="Agregar vehículo:", fg="white",bg=color_fondo)
        self.titulo.grid(row=0, column=0)

        texto_patente = Label(self.ventana3, text="Dominio:")
        texto_patente.grid(row=1,column=0)
        input_dominio=Entry(self.ventana3,background="white", fg=color_fondo)
        input_dominio.grid(row=1,column=1)

        texto_marca = Label(self.ventana3, text="Marca:")
        texto_marca.grid(row=2,column=0)
        input_marca=Entry(self.ventana3,background="white", fg=color_fondo)
        input_marca.grid(row=2,column=1)
        
        texto_modelo = Label(self.ventana3, text="Modelo:")
        texto_modelo.grid(row=3,column=0)
        input_modelo=Entry(self.ventana3,background="white", fg=color_fondo)
        input_modelo.grid(row=3,column=1)

        texto_color = Label(self.ventana3, text="Color")
        texto_color.grid(row=4,column=0)
        input_color=Entry(self.ventana3,background="white", fg=color_fondo)
        input_color.grid(row=4,column=1)

        texto_pos = Label(self.ventana3, text="Ubicación: ")
        texto_pos.grid(row=5,column=0)
        lista_libres=self.garage.mostrar_libres()
        print(lista_libres)

        pos_libres = ttk.Combobox(self.ventana3, values=lista_libres,state="readonly")
        pos_libres.grid(row=5,column=1)

        def cerrar_ventana():
            self.ventana3.destroy()
        self.boton_cerrar=Button(self.ventana3,text="Cerrar",command=cerrar_ventana)
        self.boton_cerrar.grid(row=16, column=0)
        
        def guardar_vehiculo():
            nuevo_auto=[input_dominio.get(),input_marca.get(),input_modelo.get(), input_color.get()]
            self.garage.agregar_auto(autos_model.Auto(input_dominio.get(),input_marca.get(),input_modelo.get(), input_color.get()),pos_libres.get())
            pos_libres["values"]=[]
            pos_libres.set("")
            pos_libres["values"]=self.garage.mostrar_libres()
            #Limpiar el formulario
            input_dominio.delete(0,END)
            input_marca.delete(0,END)
            input_modelo.delete(0,END)
            input_color.delete(0,END)
            nuevo_auto.clear()
            

        self.boton_guardar=Button(self.ventana3,text="Guardar",command=guardar_vehiculo)
        self.boton_guardar.grid(row=15, column=0)

        self.ventana3.mainloop()

    def ventana_quitar(self):
        self.ventana4=Tk()
        self.ventana4.title("Quitar vehículo")
        self.ventana4.geometry("600x600")        
        #Crea el titulo
        self.titulo= Label(self.ventana4,text="Quitar vehículo:", fg="white",bg=color_fondo)
        self.titulo.pack()
        
        lista_autos= Variable(self.ventana4)
        lista_autos.set(self.garage.mostrar_autos())
        lista_mostrar=Listbox(self.ventana4,listvariable=lista_autos,width=50,selectmode=BROWSE)
        lista_mostrar.pack(pady=5)

        def quitar_seleccionado():
            seleccionado = lista_mostrar.curselection()
            print(seleccionado[0])
            self.garage.eliminar_auto(str(seleccionado[0]))
            lista_autos.set(self.garage.mostrar_autos())


        boton_quitar = Button(self.ventana4, text="Quitar vehículo", command=quitar_seleccionado)
        boton_quitar.pack(pady=5)

        self.ventana4.mainloop()
