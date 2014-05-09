#!/src/bin/python
import sys
import modulo

def error(nro_intervalos, nro_test, umbral):
  recuento=0
  for i in (0,nro_test):
    valor=modulo.aproximacion(nro_intervalos)
    if(abs(valor-modulo.PI)>umbral):
      recuento=recuento+1
  porcentaje=(recuento/float(nro_test))*100
  return porcentaje
    

if __name__== "__main__":         #Establecemos un bloque dentro del modulo.

  if(len(sys.argv)==4):            #Si se especifican todos los argumentos.
    nro_intervalos = int(sys.argv[1])
    nro_test = int(sys.argv[2])
    umbral=float(sys.argv[3])
  else:                        # Si se especifican todos los argumentos.
    print 'No se han especificado los argumentos necesarios, la forma de uso es modulo nro_intervalos   nro_test  umbral.'
    nro_intervalos=5
    nro_test=5
    umbral=0.00001
    
  porcentaje=error(nro_intervalos, nro_test, umbral) 
  print "El porcentaje de error es de un %f" %porcentaje
