#def my_decorator(func):
#    def wrapper(name):
#        print("fonksiyondan önceki işlemler")
#        func(name)
#        print("fonksiyondan sonraki işlemler")
#    return wrapper
#@my_decorator
#def sayHello():
#    print("hello")
#def sayGreeting():
 #   print("greeting")
#sayHello = my_decorator(sayHello)
#sayGreeting = my_decorator(sayGreeting)
#sayHello()        
#sayGreeting()
# eşitlemeden direkt başına @my_decorator yaparak da eşitlemiş gibi işlem yapılabilir
# ek olarak başka parametre eklenirse örneğin sayHello'ya o zaman my_.. e de func
#kısmına ekleme yaparız ki ekleme çalışsın
#@my_decorator
#def sayHello(name):
#    print("hello", name)
#sayHello("Ferhat")        

import math
import time
def calculateTime(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print(f"Fonksiyon {func.__name__} str({finish - start}) saniye sürdü")
    return inner    
@calculateTime
def usAlma(a,b):
    #start = time.time()
    #time.sleep(1)
    print(math.pow(a,b))
    #finish = time.time()
    #print(f"fonksiyon str({finish - start}) saniye sürdü")
@calculateTime    
def faktoriyel(num):
    #start = time.time()
    #time.sleep(1)
    print(math.factorial(num))  
    #finish = time.time()
    #print(f"Fonksiyon str({finish - start}) saniye sürdü")
  # calculate için yapacağımız örnek sonradan  # yapılanlar ondan önce (factorial ve usalma içindeki timelardan bahsediyorum)
@calculateTime
def Toplama(a,b):
    print(a+b)
@calculateTime    
def Carpma(a,b):
    print(a*b)    
faktoriyel(4)
usAlma(2,3)
Toplama(2,3)
Carpma(3,6)    