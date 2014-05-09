#!/src/bin/python
import sys
PI = 3.141592653589793115997963468544185
# Escribimos la funcion.
def aproximacion (n):
  n=int (n)
  if (n>0):
    suma=0
    for i in range(1, n+1):
      xi=(i-0.5)/float(n)
      f_xi= 4/(1+xi**2)
      b = i/float(n)
      a = b-(1/float(n))
      suma = suma + f_xi
    pi = suma/n
    return pi

if __name__== "__main__":         #Establecemos un bloque dentro del modulo. 

  if(len(sys.argv)==3):            #Si se especifican todos los argumentos.
    n = int(sys.argv[1])
    v = int(sys.argv[2])
  else:                        # Si se especifican todos los argumentos.
    print 'No se han especificado los argumentos necesarios, la forma de uso es modulo n v.'
    n=5
    v=5
    
  lista = [] 
  for j in range (1, v+1):
    if (v>0):
      pi2=aproximacion(j*n)
      lista = lista + [pi2]
  print lista

  print 'i   PI35DT   lista   i   PI35DT - lista i'
  for u in range (0, v):
    pi3= lista[u]
    diff= PI - pi3
  print '%d   %.10f   %.10f   %.10f' %(u, PI, pi3, abs(diff))
