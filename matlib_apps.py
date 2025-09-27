import matplotlib.pyplot as plt

yil = [2008,2012,2022,2025]
AlexDeSouza = [24,18,8,6]
MousaSow = [8,30,9,3]
EnnerValencia = [4,12,25,14]
EnNesryi = [2,6,10,18]
plt.plot([],[],color="b",label="AlexDeSouza")
plt.plot([],[],color="y",label="MousaSow")
plt.plot([],[],color="g",label="EnnerValencia")
plt.plot([],[],color="r",label="EnNesryi")
plt.stackplot(yil,AlexDeSouza,MousaSow,EnnerValencia,EnNesryi,colors=["b","y","g","r"])
plt.title("Yıllara Göre FB'li oyuncuların attıkları goller")
plt.xlabel("Yıl")
plt.ylabel("Gol sayısı")
plt.legend()
plt.show()
"""

"""
goal_types = "Atak Golü", "Serbest Vuruş", "Penaltı"
goals = [60,8,14]
colors = ["y","b","g"]
plt.pie(goals,labels=goal_types,colors=colors,shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%")
plt.legend()
plt.show()
"""
"""

plt.bar([0.25,1.50,2.75,3.45,4.20],[10,50,40,30,80],label="AlexDeSouza",width=.5)
plt.bar([0.30,1.40,2.55,3.95,4.70],[20,50,80,10,50],label="MousaSow",width=.5)
plt.bar([0.20,1.90,2.25,3.55,4.90],[60,20,90,90,50],label="EnnerValencia",width=.5)
plt.bar([0.80,1.70,2.15,3.45,4.60],[45,50,40,20,90],label="EnNesri",width=.5)
plt.legend()
plt.xlabel("Sezon")
plt.ylabel("Performans")
plt.title("Fenerbahçe Oyuncularının Performans Grafiği")
plt.show()
"""
"""
ulasilanGolSayisi = [21,18,28,17,32,13,21,34,45,23,12,45,32,18,32,13]
formaNumaralari = [7,8,9,10,11]
plt.hist(ulasilanGolSayisi,formaNumaralari,histtype="bar",rwidth=0.8)
plt.xlabel("Forma Numaraları")
plt.ylabel("Ulaşılan Gol Sayıları")
plt.title("Fenerbahçe Oyuncularının Formalara göre attıkları gol sayısı")
plt.show()
"""