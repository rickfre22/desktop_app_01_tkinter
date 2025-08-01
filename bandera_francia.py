
from tkinter import *
ventana_principal = Tk()
ventana_principal.title("bandera de francia")
ventana_principal.geometry("800x500")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="green")

#_-------------------------
# frame 1
#--------------------------
frame_1= Frame(ventana_principal)
frame_1.config(bg="blue", width=260,height=480)
frame_1.place(x=10,y=10)
#_-------------------------
# frame 2
#--------------------------
frame_2= Frame(ventana_principal)
frame_2.config(bg="white", width=260,height=480)
frame_2.place(x=270,y=10)
# frame 3
#--------------------------
frame_3= Frame(ventana_principal)
frame_3.config(bg="red", width=260,height=480)
frame_3.place(x=530,y=10)
ventana_principal.mainloop()
