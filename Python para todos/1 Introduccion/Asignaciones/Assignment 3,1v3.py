# 3.1 Escriba un programa para solicitar al usuario las horas y la tarifa por hora
# utilizando insumos para calcular el salario bruto. Paga la tarifa por hora por las horas
# a 40 y 1,5 veces la tarifa por hora para todas las horas trabajadas por encima de 40
# horas. Utilice 45 horas y una tasa de 10,50 por hora para probar el programa
# (la paga debe ser 498,75). Debes usar input para leer una cadena y
# float () para convertir la cadena en un número. No te preocupes por el error
# comprobar la entrada del usuario: suponga que el usuario escribe correctamente los números.

sh=input("Hours: ")
sr=input("Rate: ")
fh=float(sh)
fr=float(sr)
if fh>40:
    reg = fr*40
    otp=(fh-40.0)*(fr*1.5)
    xp1=otp+reg
    print(xp1)
else:
    xp1=fh*fr
    print(xp1)

# 3.1 Write a program to prompt the user for hours and rate per hour 
# using input to compute gross pay. Pay the hourly rate for the hours up 
# to 40 and 1.5 times the hourly rate for all hours worked above 40 
# hours. Use 45 hours and a rate of 10.50 per hour to test the program 
# (the pay should be 498.75). You should use input to read a string and 
# float() to convert the string to a number. Do not worry about error 
# checking the user input - assume the user types numbers properly.