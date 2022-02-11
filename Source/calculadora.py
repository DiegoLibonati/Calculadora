from tkinter import *
from PIL import ImageTk, Image

raiz=Tk()
raiz.title("Calculadora")
raiz.geometry("200x300")
raiz.iconbitmap("D:\Diego\Programacion\Python\Proyectos\Calculadora")

miFrame=Frame(raiz)
miFrame.pack()


# Variables
operacion=""
resultado=0
reset_pantalla=False
Volver=0



# PANTALLA
numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=20, columnspan="5", sticky="EW", ipady=3) # Columnspan para ocupar 4 columnas el entry.
pantalla.config(background="black", fg="#03f943", justify="right")

numeroPantalla.set(0)

# Pulsaciones Teclado

def numeroPulsado(num):

	global operacion
	global reset_pantalla

	if reset_pantalla==True:

		numeroPantalla.set(numeroPantalla.get() + num) # Lo que haya en pantalla contadenado mas el num. Es lo que permite get.

	else:

		numeroPantalla.set(num)
		reset_pantalla=True

# Operaciones

# Funcion Suma

cont_suma=0

def suma(num):

	global operacion

	global resultado

	global reset_pantalla

	global num1

	global cont_suma

	print("hola")

	if cont_suma==0:
		num1=float(num)
		resultado=num1

		if cont_suma==1:
			resultado=resultado+float(num) # resultado=resultado+int(num) - float(resultado)+=float(num)

	cont_suma+=1

	if cont_suma>=1:
		cont_suma=0

	operacion="suma"

	reset_pantalla=False

	botonComa.config(state="active")
	botonCe.config(state="active")

	numeroPantalla.set(resultado)


# Funcion Resta
num1=0

cont_rest=0

def resta(num):

	global operacion

	global resultado

	global num1

	global cont_rest

	global reset_pantalla

	if cont_rest==0:

		num1=float(num)

		resultado=float(num1)

	else:

		if cont_rest==1:

			resultado=float(num1)-float(num)

		else:

			resultado=float(resultado)-float(num)

		numeroPantalla.set(resultado)

		resultado=numeroPantalla.get()


	cont_rest=cont_rest+1
	operacion="resta"
	botonComa.config(state="active")
	botonCe.config(state="active")
	reset_pantalla=False

# Funcion multiplicar
cont_mult=0

def Multiplicar(num):
	global operacion
	global resultado
	global num1
	global cont_mult
	global reset_pantalla

	if cont_mult==0:

		num1=float(num)

		resultado=num1

	else:

		if cont_mult==1:

			resultado=num1*float(num)

		else:

			resultado=float(resultado)*float(num)

		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()

	cont_mult+=1
	operacion="mult"
	botonComa.config(state="active")
	botonCe.config(state="active")
	reset_pantalla=False

# Funcion Dividir

cont_div=0

def div(num):

	global resultado

	global cont_div

	global operacion

	global resultado

	global num1

	global reset_pantalla

	if cont_div==0:
		num1=float(num)
		resultado=num1

	else:

		if cont_div==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)

		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()

	cont_div+=1

	if cont_div>=1:
		cont_div=0

	operacion="division"
	botonComa.config(state="active")
	botonCe.config(state="active")
	reset_pantalla=False

	
# Operacion Porcentaje
operacion2=""

def opPorcentaje(num):
	global operacion
	global num1
	global resultado
	global operacion2


	num1=float(num)
	resultado=num1

	if operacion=="suma":
		porcentajesuma=num1*float(num)/100
		resultado=resultado+porcentajesuma
		resultado=resultado-float(num)

	elif operacion=="resta":
		porcentajeresta=num1*float(num)/100
		
		resultado=float(resultado)-porcentajeresta
	
		resultado=resultado+float(num)
		
	elif operacion=="mult":
		porcentajemult=num1*float(num)/100
		
		resultado=float(resultado)*porcentajemult
		
		resultado=resultado/float(num)

	elif operacion=="division":
		porcentajediv=num1*float(num)/100
		
		resultado=float(resultado)/porcentajediv
		
		resultado=resultado*float(num)

# Funcion Igual

i=0

def resul3():

	global resultado

	global cont_rest

	global cont_mult

	global operacion

	global reset_pantalla

	global i

	if operacion=="resta":

		numeroPantalla.set(float(resultado)-float(numeroPantalla.get()))

		resultado=0

		cont_rest=0

		reset_pantalla=False

	elif operacion=="mult":

		numeroPantalla.set(float(resultado)*float(numeroPantalla.get()))

		resultado=0

		cont_mult=0

		reset_pantalla=False
	
	elif operacion=="suma":

		numeroPantalla.set(float(resultado)+float(numeroPantalla.get())) 

		resultado=0

	elif operacion=="division":

		numeroPantalla.set(float(resultado)/float(numeroPantalla.get())) 

		resultado=0

		reset_pantalla=False

	i=i+1

	if i>=1:
		botonCe.config(state="disabled")

# Funcion C -> Volver a 0.
cont_c=1

def c(num):

	global cont_c
	global Volver
	global reset_pantalla
	global cont_div
	global cont_mult
	global cont_suma
	global cont_rest


	if cont_c>=1:

		numeroPantalla.set(Volver)
		botonComa.config(state="active")
		
	cont_c+=1
	cont_div=0
	cont_mult=0
	cont_suma=0
	cont_rest=0
	reset_pantalla=False

# Limitar la Coma a 1 sola vez.
cont_coma=1

def coma(): 

	global cont_coma

	while cont_coma==1:
		botonComa.config(state="disabled")
		break

# Importando icono al boton borrar

foto=ImageTk.PhotoImage(Image.open("D:\Diego\Programacion\Python\Proyectos\Calculadora\del.jpg"))

# Boton borrar ultimo digito

def borrarDigito():

	global pantalla

	pantalla.delete(len(numeroPantalla.get())-1, END)

# Operacion CE, borra luego de una operacion

def operacionCE():

	pantalla.delete(0, END)

hola2=0
def onex(num):
	global hola2

	hola2=1/float(num)
	numeroPantalla.set(hola2)

import math
hola3=0
def cuadrada(num):
	hola3=math.sqrt(float(num))
	numeroPantalla.set(hola3)

def potencia(num):
	global resultado

	resultado=float(num)*float(num)

	numeroPantalla.set(resultado)
	

# 1RA FILA


# 2DA FILA

botonBorrar=Button(miFrame, width=25, height=36, text="", image=foto, command=borrarDigito, padx=3, pady=3)
botonBorrar.grid(row=3, column=1)

botonCe=Button(miFrame, text="Ce", width=3, height=2,bg="red", command=operacionCE)
botonCe.grid(row=3, column=2)
botonCe.config(state="disabled")

botonC=Button(miFrame, text="C", width=3, height=2,bg="red", command=lambda:c(numeroPantalla.get()))
botonC.grid(row=3, column=3)

botonPotencia=Button(miFrame, text="x2", width=3, height=2,bg="#00aae4", command=lambda:potencia(numeroPantalla.get()))
botonPotencia.grid(row=3, column=4)

botonCuad=Button(miFrame, width=6, height=2, text="R",bg="#00aae4", command=lambda:cuadrada(numeroPantalla.get()))
botonCuad.grid(row=3, column=5)


# 3RA FILA

boton7=Button(miFrame, text="7", width=3, height=2, command=lambda:numeroPulsado("7"))
boton7.grid(row=4, column=1)

boton8=Button(miFrame, text="8", width=3, height=2, command=lambda:numeroPulsado("8"))
boton8.grid(row=4, column=2)

boton9=Button(miFrame, text="9", width=3, height=2, command=lambda:numeroPulsado("9"))
boton9.grid(row=4, column=3)

botonDiv=Button(miFrame, text="/", width=3, height=2, bg="#00aae4", command=lambda:div(numeroPantalla.get()))
botonDiv.grid(row=4, column=4)

botonPorc=Button(miFrame, text="%", width=6, height=2, bg="#00aae4", command=lambda:opPorcentaje(numeroPantalla.get()))
botonPorc.grid(row=4, column=5)

# 4TA FILA

boton4=Button(miFrame, text="4", width=3, height=2, command=lambda:numeroPulsado("4"))
boton4.grid(row=5, column=1)

boton5=Button(miFrame, text="5", width=3, height=2, command=lambda:numeroPulsado("5"))
boton5.grid(row=5, column=2)

boton6=Button(miFrame, text="6", width=3, height=2, command=lambda:numeroPulsado("6"))
boton6.grid(row=5, column=3)

botonMult=Button(miFrame, text="x", width=3, height=2, bg="#00aae4", command=lambda:Multiplicar(numeroPantalla.get()))
botonMult.grid(row=5, column=4)

boton1x=Button(miFrame, text="1/x", width=6, height=2, bg="#00aae4", command=lambda:onex(numeroPantalla.get()))
boton1x.grid(row=5, column=5)

# 5TA FILA

boton1=Button(miFrame, text="1", width=3, height=2, command=lambda:numeroPulsado("1"))
boton1.grid(row=6, column=1)

boton2=Button(miFrame, text="2", width=3, height=2, command=lambda:numeroPulsado("2"))
boton2.grid(row=6, column=2)

boton3=Button(miFrame, text="3", width=3, height=2, command=lambda:numeroPulsado("3"))
boton3.grid(row=6, column=3)

botonRest=Button(miFrame, text="-", width=3, height=2, bg="#00aae4", command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=6, column=4)

# 6TA FILA

boton0=Button(miFrame, text="0", width=3, height=2, command=lambda:numeroPulsado("0"))
boton0.grid(row=7, column=1, columnspan=2, sticky="EW")

botonComa=Button(miFrame, text=",", width=3, height=2, command=lambda:[numeroPulsado("."),coma()])
botonComa.grid(row=7, column=3)

botonSuma=Button(miFrame, text="+", width=3, height=2,bg="#00aae4", command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=7, column=4)

botonIgual=Button(miFrame, text="=", width=6, height=2, bg="red", command=lambda:resul3())
botonIgual.grid(row=6, column=5, rowspan=2, sticky="NS")




raiz.mainloop()