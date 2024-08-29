import tkinter

def mostrar_mensaje(mensaje):
    print(mensaje)

#Creo el objeto ventana
ventana=tkinter.Tk()
ventana.title("Mi garage")
ventana.geometry("100x100")

#Creo el cuadro de texto
texto1=tkinter.Entry()
texto1.pack()


#Creo el objeto botón
boton1=tkinter.Button(ventana,text="Click aquí",bg="grey", command=mostrar_mensaje(texto1))
boton1.pack()



ventana.mainloop()