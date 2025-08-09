# Imdb verileri hakkında sorular çözeceğiz #
# öncelikle ilgili dosyayı açalım
import pandas as pd
# imdb verilerini içeren csv dosyasını okuyalım
df = pd.read_csv("Imdb.csv")
# Dosya hakkında bilgileri görelim
#print(df.info()) # DataFrame'in yapısını gösterir
#result = df.columns
#print(result ) # DataFrame'in sütun isimlerini gösterir
# İlk 5 kaydı gösterelim
#result = df.head()
#print(result)
# ilk 10 kaydı gösterelim
#result = df.head(10)
#print(result) 
# Sadece "title" sütununu gösterelim
#result = df["Title"]
# sadece "title" ve "rated" sütunlarını içeren ilk 5 kaydı gösterelim
#result = df[["Title", "Rated"]].head()
#print(result) 
# Sadece "Title" ve "Rated" sütunlarını içeren son 7 kaydı alınız
#result = df[["Title","Rated"]].tail(7)
#print(result)
# Sadece "Title" ve "Rated" sütununu içeren ve imdb puanı 8 ve üstünde
# olan kayıtların ilk 50 tanesinin alınız
#result = df[df["Rated">=8.0]][["Title","Rated"]].head() 
# Yılları 2014-15 olan filmlerin isimlerini getiriniz
#result = df[(df["Year"] >=2014) & (df["Year"]<=2015)][["Title","Year"]]
#print(result)
