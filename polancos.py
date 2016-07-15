
mensaje = "ingrese  arreglo"
print mensaje

t = raw_input()
arreglos = []
for var1 in range(0, int(t)):
	lista.append(raw_input("Ingrese elemento "))

print "A^0 = E"


a1 = "{"
for var1 in range(0, len(arreglos)):
	a1 = a1 + arreglos[var1]+","
a1 = a1 + "}"



a2 = "{"
for var1 in range(0, len(arreglos)):
	for var2 in range(0, len(arreglos)):	
		a2 = a2 + arreglos[var1]+arreglos[var2]+","
a2 = a2 + "}"




a3 = "{"
for i in range(0, len(arreglos)):
	for var2 in range(0, len(arreglos)):	
		for var3 in range(0, len(arreglos)):
			a3 = a3 + arreglos[var1]+arreglos[var2]+arreglos[var3]+","
a3 = a3 + "}"


a4 = "{"
for var1 in range(0, len(arreglos)):
	for var2 in range(0, len(arreglos)):	
		for var3 in range(0, len(arreglos)):
			for var4 in range(0, len(arreglos)):
				a4 = a4 + arreglos[var1]+arreglos[var2]+arreglos[var3]+arreglos[var4]+","
print "A^1 = "+a1
print "A^2 = "+a2
print "A^3 = "+a3
print "A^4 = "+a4


