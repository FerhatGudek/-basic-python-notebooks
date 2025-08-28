#x = int(input("x değeri giriniz: "))
#y = int(input("y değeri giriniz: "))
#print(x/y) # eger sıfıra bölersek ZeroDivisionError hatası alırız
# o yüzden try expected blokları içine sokarak bilinçli bir şekilde yapalım
#try:
#    x = int(input("x değeri giriniz: "))
#    y = int(input("y değeri giriniz: "))
#    print(x/y)
#except ZeroDivisionError:
#    print("y değeri için sıfır girilmez")    
# bu şekilde istediğimiz hatayı vermiş olduk ekleme yapalım
#except ValueError:
#    print("Gardas lütfen istenilen şekilde değerler gir!")

#try:
#    x = int(input("x değeri giriniz: "))
#    y = int(input("y değeri giriniz: "))
#    print(x/y)
#except (ZeroDivisionError,ValueError) as e:
#    print("Yanlış bilgi girdin gardas")
#    print(e) 
#try:
#    x = int(input("Lütfen bir x değeri giriniz: "))
#    y = int(input("Lütfen bir y değeri giriniz: "))
#    print(x/y)
#except (ValueError,ZeroDivisionError):
#    print("Hata yaptın la bebe")
#else:
#    print("Hersey yolunda gardas")        
while True:
    try:
        x = int(input("Lütfen bir x değeri giriniz: "))
        y = int(input("Lütfen bir y değeri giriniz: "))
        print(x/y)
    except Exception as ex: #Exception ise tanımlı bir hatalar kümesidir genel koyulabilir
        print("Hata yaptın la bebe",ex)
    else:
        break
    finally:
        print("try except sonlandı")  # bu örnek while döngüsü ile birleşimi
