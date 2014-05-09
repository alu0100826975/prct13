import matplotlib.pylab as pl
import numpy as np
import time
import moduloerror
#----------------------Codigo para el primer grafico.--------------------------------

intervalos=[10, 50, 100, 150, 500, 550, 1000]
umbrales=[1e-4, 1e-5, 1e-6, 1e-7, 1e-8]
total=[]

for intervalo in intervalos:
  porcentajes = []
  for umbral in umbrales:
    p=moduloerror.error(intervalo, 100, umbral)
    porcentajes=porcentajes + [p]
  total=total+[porcentajes]
  
print total[0]
print total[1]
print total[2]
print total[3]
print total[4]

pl.subplot(2, 1, 1)

pl.plot(umbrales,total[0], color="blue", linewidth=2.5, linestyle="-", label="10 intervalos") 
pl.plot(umbrales,total[1], color="red", linewidth=2.5, linestyle="-", label="50 intervalos")   
pl.plot(umbrales,total[2], color="black", linewidth=2.5, linestyle="-", label="100 intervalos")
pl.plot(umbrales,total[3], color="yellow", linewidth=2.5, linestyle="-", label="150 intervalos")
pl.plot(umbrales,total[4], color="grey", linewidth=2.5, linestyle="-", label="500 intervalos")
pl.plot(umbrales,total[5], color="green", linewidth=2.5, linestyle="-", label="550 intervalos")
pl.plot(umbrales,total[6], color="violet", linewidth=2.5, linestyle="-", label="1000 intervalos")

pl.legend(loc='upper left')

#pl.xlim(1e-9,1e-3)
#pl.xticks([1e-4, 1e-5, 1e-6, 1e-7, 1e-8])

pl.ylim(-10, 10)

pl.title("Practica 13")



#-------------------Codigo para el segundo grafico.-----------------------------

tiempos=[]
for intervalo in intervalos:
  ci=time.clock()
  e=moduloerror.error(intervalo, 100, 1e-5)
  ct=time.clock()
  tp=ci-ct
  tiempos=tiempos+[tp]
  
pl.subplot(2, 1, 2) 
pl.plot(intervalos,tiempos, color="violet", linewidth=2.5, linestyle="-")
pl.xlim(-10.0,1100.0)
pl.xlabel("Intervalos")
pl.ylim(-0.001, 0.0015)
pl.ylabel("Tiempo en segundos")

pl.title("Practica 13")
pl.savefig("prct13.eps", dpi=72)
pl.show()