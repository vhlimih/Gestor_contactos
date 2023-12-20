from tkinter import ttk
import tkinter

contactos=[]

#agregamos contactos con dos variables: nombre y telefono,que va a estar adentro de la funcion

def agregar_contacto():
    nombre= caja_nombre.get()
    telefono= caja_telefono.get()
    contacto={"Nombre":nombre,"Telefono":telefono}
    contactos.append(contacto)
    treeview.insert("", tkinter.END, text=nombre, values=(telefono))


#borrar contacto,esto nos ayuda a eliminar con facilidad
 
def borrar():
    selec = treeview.selection()
    if selec:
        for i in selec:
            treeview.delete(i)


#crear una ventana

ventana = tkinter.Tk()
ventana.geometry("500x500")
ventana.title("gestor de contactos")


etiquetaNombre = tkinter.Label(ventana, text="Nombre:")
etiquetaNombre.pack() 
caja_nombre = tkinter.Entry(ventana)
caja_nombre.pack()


etiquetaTelefono= tkinter.Label(ventana, text="Telefono:")
etiquetaTelefono.pack()
caja_telefono = tkinter.Entry(ventana)
caja_telefono.pack()

#empezamos a agregar nuestros botones en estas columnas

boton_agrega = tkinter.Button(ventana, bg= "orange", text="agregar_contacto", command = agregar_contacto)
boton_borrar = tkinter.Button(ventana, bg= "red", text="borrar", command = borrar)
texto = tkinter.Entry(ventana)

boton_agrega.pack()
boton_borrar.pack()


treeview = ttk.Treeview(ventana, columns=('tel'))
treeview.heading("#0", text="nombre")
treeview.heading("tel", text="telefono")
treeview.pack()


ventana.mainloop()