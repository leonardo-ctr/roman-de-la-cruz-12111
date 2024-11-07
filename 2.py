print(" ")
print("Roman De la cruz leonardo antonio,3-w.1211")
print(" ")
#solicita la nota
nota = float(input("Introduce tu nota: "))

#compara e imprime los valores dependiendo del dato ingreasdo
if 0 <= nota < 5:
    print("reprobado")
elif 5 <= nota < 6:
    print("pasate")
elif 6 <= nota < 7:
    print("bien")
elif 7 <= nota < 9:
    print("muy bien")
elif 9 <= nota <= 10:
    print("demasiado bien ")
else:
    print("no valido")
