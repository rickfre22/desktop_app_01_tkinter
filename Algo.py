#Se importa la libreria tkinter con todas las funciones 
from tkinter import *

# -----------------------------------------------------
#funciones de la app
#------------------------------------------------------


#------------------------------------------------------
# ventana principal
#------------------------------------------------------

# Se declara una variable llamada ventana_principal, que adquiere ls carcteristicas de un objeto de tipo TK()
ventana_principal = Tk()

#Titulo de la ventana
ventana_principal.title("bandera de alemania")

#Tamaño de laventana
ventana_principal.geometry("800x500")

#desavilitar boton maximizar
ventana_principal.resizable(0,0)

#color de fondo de la ventana
ventana_principal.config(bg="green")

#_-------------------------
# frame 1
#--------------------------
frame_1= Frame(ventana_principal)
frame_1.config(bg="black", width=780,height=160)
frame_1.place(x=10,y=10)
#_-------------------------
# frame 2
#--------------------------
frame_2= Frame(ventana_principal)
frame_2.config(bg="red", width=780,height=160)
frame_2.place(x=10,y=170)
# frame 3
#--------------------------
frame_3= Frame(ventana_principal)
frame_3.config(bg="yellow", width=780,height=160)
frame_3.place(x=10,y=330)
#Metodo principal quedespiega la ventana en pantalla
ventana_principal.mainloop()