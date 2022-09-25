#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define las variables a utilizar.
counter = 0
accepted = False

# Función principal.
def Main(testString):
	# Se hace referencia a las variables de inicio para evitar errores.
	global counter
	global accepted

	# Se llama al estado inicial, q1.
	q1(testString)

	# Al terminar de recorrer los estados, se determina y la cadena fue aceptada o rechazada.
	if accepted:
		print("The string has been accepted.")
	else:
		print("The string has been rejected.")

def q1(testString):
	global counter
	global accepted

	# Si la letra es una a, se pasa al siguiente caracter y se va a q2.
	if counter < len(testString):
		if testString[counter] == "a":
			counter += 1
			q2(testString)

def q2(testString):
	global counter
	global accepted

	# Si la letra es una t, se pasa al siguiente caracter y se va a q3.
	if counter < len(testString):
		if testString[counter] == "t":
			counter += 1
			q3(testString)

def q3(testString):
	global counter
	global accepted

	# Si la letra es una a, se pasa al siguiente caracter y se va a q4.
	if counter < len(testString):
		if testString[counter] == "a":
			counter += 1
			q4(testString)

def q4(testString):
	global counter
	global accepted

	# Si la letra es una c, se pasa al siguiente caracter y se va a q5.
	if counter < len(testString):
		if testString[counter] == "c":
			counter += 1
			q5(testString)

def q5(testString):
	global counter
	global accepted

	# Si la letra es una a, se pasa al siguiente caracter y se va a q6.
	if counter < len(testString):
		if testString[counter] == "a":
			counter += 1
			q6(testString)

def q6(testString):
	global counter
	global accepted

	# Si la letra es una r, se pasa al siguiente caracter y se va a q7.
	if counter < len(testString):
		if testString[counter] == "r":
			counter += 1
			q7(testString)

def q7(testString):
	global counter
	global accepted

	# Si la letra es una e, se pasa al siguiente caracter y se va a q8. En caso de que sea una a, entonces se va a q10.
	if counter < len(testString):
		if testString[counter] == "e":
			counter += 1
			q8(testString)
		elif testString[counter] == "a":
			counter += 1
			q10(testString)

def q8(testString):
	global counter
	global accepted

	# Al ser un doble círculo o estado de aceptación, hay que cambiar accepted por True.
	accepted = True

	# Si la letra es una m, se pasa al siguiente caracter y se va a q9. En caso de que sea una i, entonces se va a q10.
	if counter < len(testString):
		if testString[counter] == "m":
			counter += 1
			q9(testString)
		elif testString[counter] == "i":
			counter += 1
			q10(testString)

def q9(testString):
	global counter
	global accepted

	# Llegamos a este estado desde un estado de aceptación, así que hay que reiniciar el valor de accepted a False porque este estado no es de aceptación.
	accepted = False

	# Si la letra es una o, se pasa al siguiente caracter y se va a q10.
	if counter < len(testString):
		if testString[counter] == "o":
			q10(testString)

def q10(testString):
	global counter
	global accepted

	# Al ser un doble círculo o estado de aceptación, hay que cambiar accepted por True.
	accepted = True

	# Si la letra es una s o una m, se pasa al siguiente caracter y se va a q11.
	if counter < len(testString):
		if testString[counter] == "s" or testString[counter] == "n":
			q11(testString)

def q11(testString):
	global counter
	global accepted

	# Al ser un doble círculo o estado de aceptación, hay que cambiar accepted por True.
	accepted = True
	# Aquí no se va a ninguna otra función, pues este estado no lleva a ningún otro.

# Desde aquí se llama a la función principal.
if __name__ == "__main__":
	# Se lee la cadena a evaluar.
	stringToTest = input("Enter a string to test it: ")

	# Se llama a la función principal con la cadena leída.
	Main(stringToTest)
