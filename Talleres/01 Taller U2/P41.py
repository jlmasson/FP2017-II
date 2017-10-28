# Ejercicio 1
cadena = input("Ingrese cadena de 6 caracteres: ").upper()
print("{}\t{}\t{}\t{}\t{}\t{}".format(cadena[0]*2, cadena[1]*2, cadena[2]*2, cadena[3]*2, cadena[4]*2, cadena[5]*2))

# Otra forma de realizarlo - válido para cualquier longitud (Nivel más avanzado).
nuevaCadena = ""
for letra in cadena:
	nuevaCadena += "{}\t".format(letra*2)
nuevaCadena = nuevaCadena.rstrip("\t");
print(nuevaCadena)

# Ejercicio 2
cadena = input("Ingrese una cadena de caracteres: ").lower()
totalA = cadena.count("a")
totalE = cadena.count("e")
totalI = cadena.count("i")
totalO = cadena.count("o")
totalU = cadena.count("u")

nuevaCadena = cadena.replace("a", "")
nuevaCadena = nuevaCadena.replace("e", "")
nuevaCadena = nuevaCadena.replace("i", "")
nuevaCadena = nuevaCadena.replace("o", "")
nuevaCadena = nuevaCadena.replace("u", "")

totalVocales = totalA + totalE + totalI + totalO + totalU
nuevaCadena = "*" * totalVocales + nuevaCadena
print(nuevaCadena)

# Otra forma de realizarlo (Nivel más avanzado)
vocales = list("aeiou")
totalVocales = 0
nuevaCadena = cadena
for vocal in vocales:
	totalVocales += cadena.count(vocal)
	nuevaCadena = nuevaCadena.replace(vocal, "")
nuevaCadena = "*" * totalVocales + nuevaCadena
print(nuevaCadena)

# Ejercicio 3
materia = input("Ingrese una materia: ").upper()
adjetivo = input("Ingrese un adjetivo: ").upper()
actividad = input("Ingrese una actividad: ").upper()
print("\tLa clase de {} fue muy {} hoy".format(materia, adjetivo))
print("\t\tHemos aprendido como {} hoy en clases".format(actividad))
print("\t\t\tNo puedo esperar a la clase del Lunes")

# Ejercicio 4
tiempo = input("Ingrese la hora en formato [hh:mm:ss]: ")
h, m, s = tiempo.split(":")
h = int(h)
m = int(m)
s = int(s)
totalSegundos = h * 3600 + m * 60 + s
print("Total en segundos:", totalSegundos)

# Otra forma de realizarlo (Nivel más avanzado)
tiempo = input("Ingrese la hora en formato [hh:mm:ss]: ")
campos = [int(valor) for valor in tiempo.split(":")]
maximoExponente = len(campos) - 1
totalSegundos = 0
for i in range(len(campos)):
	valor = campos[i]
	totalSegundos += valor * (60 ** (maximoExponente - i))
print("Total en segundos:", totalSegundos)

# Ejercicio 5
segundos = int(input("Ingrese el tiempo en segundos: "))
h = segundos // 3600
residuo = segundos % 3600
m = residuo // 60
s = residuo % 60
print("La hora en formato hh:mm:ss es {:02d}:{:02d}:{:02d}".format(h, m, s))

# Ejercicio 6
exponente = int(input("Ingrese exponente de la ecuación x^n: "))
derivada = exponente - 1
print("La derivada es: {}x^{}".format(exponente, derivada))

