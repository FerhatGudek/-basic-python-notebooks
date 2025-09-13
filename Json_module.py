# dict için yaparsak
#person = {"name":"Ferhat", "languages":["python","C","JavaScript"]}
#result1 = person["name"]
#print(result1)
#result2 = person["languages"]
#print(result2)
#result3 = person["languages"][0]
#print(result3)
# buradaki gibi bir person ifadesini json yapmak için bunları tırnak içine yani
# string ifadeye çevirme işlemi yapıyoruz ve sonrasında json ifadesi elde edilmiş oluyor.
import json
person_string = '{"name":"Ferhat", "languages":["python","c","JavaScript"]}'
#result = json.loads(person_string) #dicte benzer şekilde json olarak stringi okur
#print(type(result))
#result = result["name"]
#print(type(result)) # bu sefer str tipinde olduğunu gördük
#print(result)
#with open("person.json") as f:
#    data = json.load(f)
    #print(data["name"]) # burada name bilgisini okudu
    #print(data["languages"]) # bu şekilde json dosyaasının içindeki bilgiler okunur

person_dict = {
    "name": "Ferhat",
    "languages": ["Python","C","JavaScript"]
}
#result = json.dumps(person_dict) # json.dumps kullanarak dict"i str'ye çevirdik
#print(result)
#print(type(result)) 
#with open("person.json","w") as f:
#    json.dump(person_dict,f) # dosyaya bu şekilde yazıdırıız
person_dict = json.loads(person_string)
result = json.dumps(person_dict,indent=4,sort_keys=True)
print(person_dict)
print(result) # ayrı şekilde istenildiği gibi yazdırılmış olur



