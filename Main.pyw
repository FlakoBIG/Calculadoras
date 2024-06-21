#importamos Tkinter + sus clases
from tkinter import Tk,Label,Button,Entry,messagebox


#                                   Funciones

def Sumar(valor1,valor2):
    lbl_resultado.grid(row=4,column=0,columnspan=2)
    resultado = int(valor1) + int(valor2)
    lbl_resultado["text"] =(f"Resultado: {resultado}")

def Restar(valor1,valor2):
    lbl_resultado.grid(row=4,column=0,columnspan=2)
    resultado = int(valor1) - int(valor2)
    lbl_resultado["text"] =(f"Resultado: {resultado}")

def Dividir(valor1,valor2):
    lbl_resultado.grid(row=4,column=0,columnspan=2)
    resultado = int(valor1) / int(valor2)
    lbl_resultado["text"] =(f"Resultado: {resultado}")

def Multiplicar(valor1,valor2):
    lbl_resultado.grid(row=4,column=0,columnspan=2)
    resultado = int(valor1) * int(valor2)
    lbl_resultado["text"] =(f"Resultado: {resultado}")

def Validar(Operador):
    try :
        #se obtiene el valor que este dentro del input
        valor1 = input_1.get()
        valor2 = input_2.get()
        if valor1 == "" or valor2 == "":
            #print para ver en la consola
            print("No hay nada")
            #al lbl_resultado ingresale un txt y que diga .....
            lbl_resultado["text"] = "No se ingreso nada en uno de los dos valores"
            #abre una nueva ventana de error que tenga el titulo error y que diga falta....
            messagebox.showwarning("Error","Faltan valores para poder calcular")
        else:
            if Operador == "Sumar":
                Sumar(valor1,valor2)
            elif Operador == "Restar":
                Restar(valor1,valor2)
            elif Operador == "Dividir":
                Dividir(valor1,valor2)
            elif Operador == "Multiplicar":
                Multiplicar(valor1,valor2)
    except:
        lbl_resultado["text"] = "Solo Numeros porfavor"
        messagebox.showwarning("Error","No puedes ingresar letras , solo numeros")

def Limpiar():
    input_1.delete(0)
    input_2.delete(0)

#clase  para crear la ventana principal y donde se añaden los widgets
ventana = Tk()
#titulo que va arriba de la ventana
ventana.title("Calculetreitor 3000 sinto X")
#icono
#ventana.iconbitmap("\calculatoricon.ico")
#esto es para la posicionsa
ventana.geometry("+450+250")
#tamaño de la ventana
ventana.geometry("450x210")
#fondo de la ventana
ventana.config(bg="grey")
#esto sirve para que a medida que se mueva la ventana las columnas se van a adaptar
#columnas
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=1)
ventana.columnconfigure(3,weight=1)
#Filas
ventana.rowconfigure(0,weight=1)
ventana.rowconfigure(2,weight=1)
ventana.rowconfigure(3,weight=1)
ventana.rowconfigure(4,weight=1)
ventana.rowconfigure(5,weight=1)


#                                   ESTRUCTURA DE LA VENTANA
#titulo
lbl = Label(ventana,text="Calculetreitor 3000 sinto X",font="Arial 15",bg="grey")
#label del primer valor que se ingresara
lbl_valor_1 = Label(ventana,text="Primer numero",font="Arial 10",bg="grey")
#label del segundo valor que se ingresara
lbl_valor_2 = Label(ventana,text="Segundo numero",font="Arial 10",bg="grey")

#Primera entrada de valor
input_1 = Entry(ventana,font="Arial 10")
input_2 = Entry(ventana,font="Arial 10")

btn_suma = Button(ventana,text="Suma",font="Arial 10",bg="black",fg="white",width=10,command=lambda:Validar("Sumar"))
btn_resta = Button(ventana,text="Resta",font="Arial 10",bg="black",fg="white",width=10,command=lambda:Validar("Restar"))
btn_multiplicacion = Button(ventana,text="Multiplicacion",font="Arial 10",bg="black",fg="white",width=10,command=lambda:Validar("Multiplicar"))
btn_divicion = Button(ventana,text="Divicion",font="Arial 10",bg="black",fg="white",width=10,command=lambda:Validar("Dividir"))
btn_limpiar = Button(ventana,text="Borrar",font="Arial 10",bg="black",fg="white",width=10,command=Limpiar)

#Para organizar lo voy a usar el metodo grid , que es en base a cordenadas como tabla
#el lbl estara el fila 0 columna 0 y el columspan es para cunatas columnas ocupara
#texto
#cuantas columnas ocupara = columnspan
#espacio eje Y = pady
lbl.grid(row=0,column=1,columnspan=2,pady=10)
lbl_valor_1.grid(row=2,column=0,pady=5)
lbl_valor_2.grid(row=3,column=0,pady=5)
#inputs
input_1.grid(row=2,column=1,padx=10)
input_2.grid(row=3,column=1,padx=10)
#botones
btn_suma.grid(row=2,column=3,columnspan=2,pady=2)
btn_resta.grid(row=3,column=3,columnspan=2,pady=2)
btn_multiplicacion.grid(row=4,column=3,columnspan=2,pady=2)
btn_divicion.grid(row=5,column=3,columnspan=2,pady=2)
btn_limpiar.grid(row=6,column=3,columnspan=2,pady=2)

#resultado
lbl_resultado = Label(ventana,bg="grey")

#abre una ventana y es importante que este en el final
#es nesesario porque una ventana tiene que estar en loop para que este presente
ventana.mainloop()