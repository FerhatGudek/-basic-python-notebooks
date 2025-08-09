#import pandas as pd
#import numpy as np
#data = {
#    "timestamp": ["2025-01-01 12:00", "2025-01-01 12:01", "2025-01-01 12:02"],
#    "value":[10,12,14]
#}
#df = pd.DataFrame(data)
#df["timestamp"]= pd.to_datetime(df["timestamp"]) # bu sayede pandas bu sütunu zaman gibi algılar
#df.set_index("timestamp", inplace= True) 
#print(df)
#pd.to_datetime() fonksiyonu, bu string ifadeleri datetime64[ns] tipine çevirir.
#df.set_index(".....") ilgili sütunu indeks haline getirir inplace true kalıcılık sağlar.Artık timestamp satırların kimliğiidir
#df.resample("min").mean() → dakikalık ortalama
#df.between_time("12:00", "12:02") → zaman aralığı seçimi
#df.rolling(window=2).mean() → kayan ortalama artık bu işlemler yapılabilir

#....pd.date_range kullanımı....#
#minutes = pd.date_range(start= "2025-01-01", periods =10, freq="min")
#print(minutes) # 10 defa iki dk arayla zaman verileri üretir



#df = pd.DataFrame({
#    "timestamp": pd.date_range("2025-01-01 12:00", periods=5, freq="min"),
#    "value": [10, np.nan, np.nan, 13, 14]
#})
#df.set_index("timestamp", inplace=True)

#print("Eksik değerli veri:")
#print(df)

#df_filled = df.ffill() # NaN değerleri bir önceki değerler ile dolduruyor
#print("\nForward fill uygulanmış hali:")
#print(df_filled)
#import pandas as pd

#df = pd.DataFrame({
#    "timestamp": pd.date_range("2025-01-01", periods=5, freq="D")
#})
#df["hour"] = df["timestamp"].dt.hour
#df["day"] = df["timestamp"].dt.day
#df["month"] = df["timestamp"].dt.month

#print(df)
#df.groupby(df["timestamp"].dt.dayofweek)["value"].mean()
import pandas as pd

#df = pd.DataFrame({
#    "timestamp": pd.date_range("2025-01-01", periods=1440, freq="min"),
#    "value": range(1440)
#})
#df.set_index("timestamp", inplace=True)

#daily_mean = df.resample("D").mean()
#print(daily_mean)
#.... basit bir argparse uygulaması....#
import argparse
if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sayi1", help="sayi1 değeri", required=True)
    parser.add_argument("--sayi2", help = "sayi2 değeri", required=True)
    parser.add_argument("--operator", help ="operatör işlemleri", choices=["toplama","çıkarma","çarpma"])
    args = parser.parse_args()

    sayi1 = int(args.sayi1)
    sayi2 = int(args.sayi2)
    operator = str(args.operator)

    sonuc = None
    if operator == "toplama":
        sonuc = sayi1 + sayi2
    elif operator == "çıkarma":
        sonuc = sayi1 - sayi2
    elif operator == "çarpma":
        sonuc = sayi1 * sayi2
    else:
        print("Lütfen geçerli bir işlem yapınız")
         
    print(f"İşlem sonucunuz:{sonuc}")

          

   



