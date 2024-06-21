from tkinter import Label,Button,Tk
#subprocesos
import subprocess


#hacemos la ventana
ventana_principal = Tk()
#                                   Abrir ventanas
def abrir_calculadora_1():
    print("voy abrir calculadora_1")
    #abre el archivo que es un python y que se llama calculadora_1.pyw
    subprocess.Popen(['python','Calculadora_1.pyw'])
    #destruye la ventana principal
    ventana_principal.destroy()

#                                   Configuracion de la ventana
ventana_principal.title("Calculadoras de aprendisaje")
ventana_principal.geometry("+450+250")
ventana_principal.geometry("361x210")
ventana_principal.config(bg="grey")
#                                   ELEMENTOS DE LA VENTANA
lbl_titulo = Label(ventana_principal,text="Calculadoras",font="Arial 15",bg="grey")
btn_1 = Button(ventana_principal,font="Arial 10",bg="green",fg="white",width=10,text="1",command=abrir_calculadora_1)
btn_2 = Button(ventana_principal,font="Arial 10",bg="red",fg="white",width=10,text="2")
btn_3 = Button(ventana_principal,font="Arial 10",bg="red",fg="white",width=10,text="3")
btn_4 = Button(ventana_principal,font="Arial 10",bg="red",fg="white",width=10,text="4")
btn_5 = Button(ventana_principal,font="Arial 10",bg="red",fg="white",width=10,text="5")
btn_6 = Button(ventana_principal,font="Arial 10",bg="red",fg="white",width=10,text="6")
btn_7 = Button(ventana_principal,font="Arial 10",bg="red",fg="white",width=10,text="7")
btn_8 = Button(ventana_principal,font="Arial 10",bg="red",fg="white",width=10,text="8")

#                                   ESTRUCTURA DE LA VENTANA
lbl_titulo.grid(row=0,column=2,columnspan=2)
btn_1.grid(row=1,column=1)
btn_2.grid(row=1,column=2)
btn_3.grid(row=1,column=3)
btn_4.grid(row=1,column=4)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)
btn_7.grid(row=2,column=3)
btn_8.grid(row=2,column=4)
ventana_principal.mainloop()