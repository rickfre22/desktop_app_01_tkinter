#Se importa la libreria tkinter con todas las funciones 
from tkinter import *

# -----------------------------------------------------
#finciones de la aplicacion
#------------------------------------------------------


#------------------------------------------------------
# ventana principal
#------------------------------------------------------

# S e declara una variable llamada ventana_principal, que adquiere ls carcteristicas de un objeto de tipo TK()

ventana_principal = Tk()

#Titulo de la ventana
ventana_principal.title("Miguel Angel Galvis Quiñonez")
#Tamaño de laventana
ventana_principal.geometry("800x500")
#Metodo principal quedespiega la ventana en pantalla
ventana_principal.mainloop()