saat = int(input ("lütfen saati giriniz"))

if 8 <= saat< 12:
    print("günaydın")
elif 12 <= saat < 16:

    print("iyi günler")
elif 16 < saat < 24:
    print("iyi aksamlar")
elif 1 <= saat < 8:
    print("iyi geceler")

else :
    print("hatalı saat girdiniz:")
