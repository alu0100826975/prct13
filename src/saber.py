import matplotlib.pylab as pl
import numpy as np

def f(x):
  return 4/(1+x*x)

pl.figure(figsize=(8,6), dpi=80)
X = np.linspace(0, 1, 256, endpoint=True)
Y = f(X)

pl.plot(X,Y, color="blue", linewidth=2.5, linestyle="-")
pl.xlim(-1.0,2.0)
pl.ylim(1.0,5.0)
pl.title("Para saber mas")
pl.savefig("saber.eps", dpi=72)
pl.show()