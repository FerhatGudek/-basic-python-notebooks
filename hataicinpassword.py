import re

def checkPassword(psw):
    if len(psw) < 8:
        raise Exception("Parola en az 8 karakter olmalıdır kardesim.")
    elif not re.search("[a-z]", psw):
        raise Exception("Parola küçük harf içermelidir kardesim.")
    elif not re.search("[A-Z]", psw):
        raise Exception("Parola büyük harf içermelidir kardesim.")
    elif not re.search("[0-9]", psw):
        raise Exception("Parola rakam içermelidir kardesim.")
    elif not re.search("[_@$]", psw):
        raise Exception("Parola özel karakter (_@$) içermelidir kardesim.")
    elif re.search("\s", psw):
        raise Exception("Parola boşluk karakteri içermemelidir kardesim.")
    else:
        print("Parola başarılı şekilde oluşturuldu ✅")

# Test
password = "123456790"
try:
    checkPassword(password)
except Exception as ex:
    print(ex)

