import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(h, w, max_iters=20):
    y, x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x + y * 1j
    z = c
    divtime = max_iters + np.zeros(z.shape, dtype=int)

    for i in range(max_iters):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2            
        div_now = diverge & (divtime==max_iters)  
        divtime[div_now] = i                     
        z[diverge] = 2                           

    return divtime

plt.imshow(mandelbrot(400, 400))
plt.show()