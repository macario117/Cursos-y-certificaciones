# If the code in the try works - the except is skipped
# If the code in the try fails - it jumps to the except section

# Si el código en el intento funciona, se omite la excepción
# Si el código en el intento falla, salta a la sección excepto

rawstr = input('Enter a number:')
try: 
    ival = int(rawstr)  # Verifica que sea un número entero 
except: 
    ival = -1           # Si NO es un número haz que la variable "ival" sea un -1

if ival > 0 :  #Así seguramos que cuando el programa llegue aqui ival es un numero entero
    print('Nice work')
else:  
    print('Not a number')


