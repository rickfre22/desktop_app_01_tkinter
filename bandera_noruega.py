
from tkinter import *
ventana_principal = Tk()
ventana_principal.title("bandera de francia")
ventana_principal.geometry("800x500")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="white")

#_-------------------------
# frame 1
#--------------------------
frame_1= Frame(ventana_principal)
frame_1.config(bg="darkred", width=780,height=480)
frame_1.place(x=10,y=10)
#_-------------------------
# frame 2
#--------------------------
frame_2= Frame(ventana_principal)
frame_2.config(bg="white", width=100,height=480)
frame_2.place(x=150,y=10)
# frame 3
#--------------------------
frame_3= Frame(ventana_principal)
frame_3.config(bg="white", width=780,height=100)
frame_3.place(x=10,y=200)
#_-------------------------
# frame 4
#--------------------------
frame_2= Frame(ventana_principal)
frame_2.config(bg="darkblue", width=40,height=480)
frame_2.place(x=180,y=10)
# frame 5
#--------------------------
frame_3= Frame(ventana_principal)
frame_3.config(bg="darkblue", width=780,height=40)
frame_3.place(x=10,y=230)
ventana_principal.mainloop()