import re
result = dir(re) # içindekiler hakkıdna bilgi almak için
print(result)
str = "Ferhat Gudek ile tam 45 saat python seruvenine hosgeldiniz"
result = re.findall("Ferhat",str) # virgül ile hangi str ifadesinde arama yapılacağı belirtilir
result = len(result) # hangi satırda olduğunu bulmamıza yarayan yöntem
result = re.split(" ",str) # str içindeki ifadeleri boşluktan itibaren böler
result = re.split("a",str) #aynısını "a" ile böler
result = re.sub(" ","-",str) # boşluk yerlerine çizgi ekledi
result = re.search("Ferhat",str) #aradığı aralığı ve eşleştirdiği yeri gösterir
result = result.span() # bu şekilde de direkt aralığı göstermiş olduk
#result.end() ve result.group() ile de sırasıyla son ve bulduğu ifadeyi gönderir
result = result.string #işlem yaptığımız str ifadadeyi gösterir
result = re.findall("[abc]",str) #abc olan ifadeleri liste şeklinde karşımıza çıkarır
result =re.findall("[saat]",str) # ilgili karakterlerin hepsini liste şeklinde gösterir
result = re.findall("[a-z]",str) # a dan z ye hepsini liste şekline karşıma çıkarır
result = re.findall("[0-5]",str) # sadece 4 ile 5 i gösterdi
result = re.findall("[^abc]",str) # carrot işareti ile abc dışındaki tüm karakterleri arar
result = re.findall("[^0-9]",str) # rakam olmayan karakterleri arar
result = re.findall("...",str) # üçlü gruplandıracak şekilde bize geri gönderir
result = re.findall("py..on",str) # python ifadesini bize döndürür
result = re.findall("^a",str) # a ile başlayan karakter araması yapar
result = re.findall("t$",str) # str ifadesi t ile bitiyor mu taraması yapar
result = re.findall("sa*t",str) #a nın sayısının önemi olmadan uygun ifade arar
result= re.findall("sa+t",str) # a karakterinden en az bir tane olacak demek ! sıfır ya da bir kere istiyorsak soru işareti kullanırız
result = re.findall("a{2}",str) # a dan iki tane olanları bana getir
result = re.findall("[0-9]{2}",str) # iki basamaklı sayıları getir
print(result)
