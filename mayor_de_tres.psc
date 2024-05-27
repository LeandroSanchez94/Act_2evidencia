Algoritmo sin_titulo
	Escribir "por favor, ingresa el primer  numero: "
	Leer numero1
	Escribir "por favor, ingresa el segundo  numero: "
	Leer numero2
	Escribir "por favor, ingresa el tercer  numero: "
	Leer numero3
	Si numero1 > numero2 Entonces
		Si numero1 > numero3 Entonces
			mas_grande = numero1
		SiNo
			mas_grande = numero3
		Fin Si
	SiNo
		Si numero2 > numero3 Entonces
			mas_grande = numero2
		SiNo
			mas_grande = numero3
		Fin Si
	Fin Si
	Escribir "el mayor es: ", mas_grande
FinAlgoritmo
