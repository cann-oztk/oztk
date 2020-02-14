sayı1 =int(input("1. Sayı =>"))
sayı2=int(input("2. Sayı =>"))
islem=input("İşlemi Giriniz(+,-,*,/)=> ")

if islem == "-":
  sonuc = sayı1 - sayı2

  print(sonuc)
elif islem == "+":

  sonuc = sayı1 + sayı2
  print(sonuc)

elif islem =="*":
  sonuc = sayı1 * sayı2

  print(sonuc)
elif islem == "/" and sayı2  != 0:

  sonuc = sayı1 / sayı2
  print(sonuc)

else:
  print("Hatalı Giriş Yaptınız..!")
