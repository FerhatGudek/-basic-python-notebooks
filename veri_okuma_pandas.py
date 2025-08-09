import pandas as pd
import numpy as np
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index= ["A", "B", "C"], columns= ["Column1", "Column2", "Column3"])
#print(df) istenilen şekilde ayarladıktan sonra rastgele değerli bir dataframe oluşturur.
#result = df["Column1"] # "Column1" sütununu seçer
#print(result)
#result = type(df["Column1"]) # "Column1" sütununun tipini döndürür
#print(result) #<class 'pandas.core.series.Series'> çıktısını verir.
#result = df[["Column1","Column2"]] # bu sefer iki sütunu seçtik 
#print(result)
#result = df.loc["A"] # "A" satırını seçer
#print(result)
#result = type(df.loc["A"])
#print(result) # <class 'pandas.core.series.Series'> çıktısını verir
#result = df.loc[:,"Column1"] # sadece bize column1 sütununun değerlerini verir
#print(result)
#result=  df.loc[:,["Column1","Column2"]] # bize sadece column1 ve column2 sütunlarını verir
#print(result)
#result = df.loc["A":"B",["Column2"]] # "A" ve "B" satırları arasındaki "Column2" sütununu seçer
#print(result)
#result = df.loc[2] # bu şekilde bir index numarası bizde yok ancak iloc kullanarak direkt satır numarası ile seçilebilir
#result = df.iloc[2] # c yani 3. satır bize döndürülmüş olur
#print(result)
#result = df.loc["A","Column3"] # "A" satırındaki "Column3" değerini seçer
#print(result)
#df["Column4"] = pd.Series(randn(3),index= ["A", "B", "C"]) # yeni bir sütun ekler
#print(df)
#df["Column5"] = df["Column1"]+ df["Column2"] # yeni bir sütun ekler ve bu sütun Column1 ve Column2'nin toplamı şeklinddir
#print(df)
##print(df.drop("Column5", axis=1)) # "Column5" sütununu siler
#.... DataFrame Filtreleme işlemleri.....#
data = np.random.randint(10, 100, 75).reshape(15,5) # 10 ile 100 arasında rastgele 75 sayı üretir ve 15x5 boyutunda bir matris oluşturur
df = pd.DataFrame(data, columns=["Column1", "Column2", "Column3", "Column4", "Column5"])
#result = df.columns # DataFrame'in sütun adlarını döndürür
#print(result)
#result = df.head() # DataFrame'in ilk 5 satırını döndüdür
#result = df.head(10) # DataFrame'in ilk 10 satırını döndürür
#result= df.tail() # DataFrame'in son 5 satırını döndürür
#result= df.tail(10) # DataFrame'in son 10 satırını döndürür
#result = df["Column1"].head() # "Column1" sütununun ilk 5 satırını döndürür
#result = df[["Column1", "Column2"]].head() # "Column1" ve "Column2" sütunlarının ilk 5 satırını döndüdrür
#result = df > 50 # DataFrame'deki tüm değerlerin 50'den büyük olup olmadığını kontrol eder ve boolean bir değer döndürür
#result = df[df > 50] # DataFrame'deki tüm değerlerin 50'den büyük olduğu satırları döndürür
#result = df[df%2 == 0] # DataFrame'deki tüm çift sayıları döndürür
#result = df[df["Column1"] > 50] # sadece column1 değerleri gelmez
#result = df[df["Column1"] > 50]["Column1"] # sadece " column1'in 50 den büyük değerleri döndürülür 
#result = df[(df["Column1"] > 50) & (df["Column2"] < 70)][["Column1","Column2"]]
# "Column1" değerleri 50'den büyük ve "Column2" değerleri 70'den küçük olan satırları döndürür
# & yerine | kullanarak ya da işlemi yapılabilir bu durumda iki durumdan birisi sağlanması yeterli olur
#print(result)
 


