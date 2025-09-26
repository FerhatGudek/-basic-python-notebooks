import matplotlib.pyplot as plt
import numpy as np
'''
x = [1,2,3,4]
y = [1,4,9,14]     # eğer eklenti bir şey eklenirse plt.plot içinde de değişken eklenir
plt.plot(x,y,color="b",linewidth="5")    #renk ekleyip kalınlığını belirledik marker,stil,renk olarak da belirleniyor örneğin o--g
plt.axis([0,6,0,20]) # x min x max y min y max değeleridir
plt.title("Grafik başliği") # grafik başlığı için koyulur
plt.xlabel("xlabel") # xlabel ile x ekseninin ismini belirleyebiliriz
plt.ylabel("ylabel") # ylabel ile y ekseninin ismini belirleyebiliriz
plt.show() # yazdırmaya yarar ayrıca eklenen değişken grafik parantezine eklenir
'''
'''
x = np.linspace(0,2,100)
plt.plot(x,x,label="linear",color="yellow")
plt.plot(x,x**2,label="quadratic",color="blue")
plt.plot(x,x**3,label="cubic",color="green")
plt.xlabel("x grafiği")
plt.ylabel("y grafiği")
plt.title("Basit bir grafik çizimi")
plt.legend() # hangi çizginin hangi grafik olduğunu tanımlayan kutucuk koyar
plt.show() # bu yapılanlar sayesinde üç adet grafiği de çizmiş olduk
'''
'''
fig,axs = plt.subplots(3)#iki grafik çizeceğimiz için içini iki olarak belirldk
x = np.linspace(0,2,100)
axs[0].plot(x,x,color="yellow") #axs kullanarak üç ayrçizgiyi tanımladık
axs[0].set_title("linear")
axs[1].plot(x,x**2,color="blue")
axs[1].set_title("quadratic")
axs[2].plot(x,x**3,color="green")
axs[2].set_title("cubic")
plt.tight_layout() # yazıların üst üste gelmemesi için yapılır
plt.legend
plt.show()
'''  
x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,2)
fig.suptitle("Grafik Başlığı")
axs[0,0].plot(x,x,color="red")
axs[0,1].plot(x,x**2,color="green")
axs[1,0].plot(x,x**3,color="yellow")
axs[1,1].plot(x,x**4,color="pink")
plt.show()
