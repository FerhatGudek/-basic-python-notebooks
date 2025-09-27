import matplotlib.pyplot as plt
import numpy as np
'''
x = np.linspace(-9,10,20)
y = x**3
z = x**2
figure = plt.figure()
axes_cube = figure.add_axes([0.1,0.1,0.9,0.9]) #fig üzerine eklenecek olan axisin konumu
axes_cube.plot(x,y,"b")
axes_cube.set_xlabel("X ekseni")
axes_cube.set_ylabel("Y ekseni")
axes_cube.set_title("Cube")
axes_square = figure.add_axes([0.15,0.6,0.25,0.3])
axes_square.plot(x,y,"r") # r çizgi p parçalı böyle modlara sahiptir
axes_square.set_xlabel("X ekseni")
axes_square.set_ylabel("Y ekseni")
axes_square.set_title("Square")
plt.legend()
plt.show()
'''
""""
figure = plt.figure()
x = np.linspace(-9,10,20)
y = x**3
z = x**2
axes = figure.add_axes([0,0,1,1])
axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
plt.legend(loc=3) # 3 yapınca sol alt köşeye geldi
plt.show()
"""
fig,axes= plt.subplots(nrows=2,ncols=1,figsize=(4,4)) #gelen sayfanın boyutu
x = np.linspace(-9,10,20)
y = x**3
z = x**2
axes[0].plot(x,y)
axes[0].set_title("Square")
axes[1].plot(x,z)
axes[1].set_title("Cube")
plt.legend()
plt.tight_layout()
plt.show()
#fig.savefig("figure2.pdf") olarak da figürü pdf olarak kaydedebiliriz