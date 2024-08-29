import tkinter

def mostrar_mensaje():
    #Muestra el texto
    print(texto1.get())
    #Limpia el cuadro de texto una vez que se muestra en pantalla
    texto1.delete(0, tkinter.END)

#Creo el objeto ventana
ventana=tkinter.Tk()
ventana.title("Mi garage")
ventana.geometry("100x100")

#Creo el cuadro de texto
titulo=tkinter.Label(text="Texto")
texto1=tkinter.Entry()
titulo.pack()
texto1.pack()

#Creo el objeto botón
boton1=tkinter.Button(ventana,text="Click aquí",bg="grey", command=mostrar_mensaje)
boton1.pack()

ventana.mainloop()