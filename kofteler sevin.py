# print('python ile ilk günüm')
# print('naberkofteli\nnaberkofteli\naberkofteli')
# print('merhaba' +' '+ 'koftepatates')
# print('merhaba' + ' '+ 'koftepatates')
# print (
#     input('merhaba, adın nedir')
# )
#print(len("Kofte"))
#print(len("Kofte"))

#print(len(input("merhaba,adın nedir ")))
#print(input("merhaba,adın nedir?"))

#isim = input("merhaba adın nedir")
#print(isim)
#print("merhaba "+isim)
#isim = "KoftePatates"
#print(isim)
# print(len(input("merhaba adın nedir?")))
# isim=input("merhaba adın nedir?")
#uzunluk=len(isim)
# print(uzunluk)
# ensongidilensehiradi = input("En son hangi şehire gittiniz?")
# evcilhayvanadı = input("Evcil hayvanınızın adı nedir?")
# print("grup adı: " + " " + ensongidilensehiradi + " "+evcilhayvanadı)
# sayi1 = input("1nci sayıyı giriniz: ")
# sayi2 = input("2nci sayıyı giriniz: ")
# toplam = int(sayi1) + int(sayi2)
# print("Toplam = " + str(toplam))
# kısakenar = input("kısa kenarı giriniz: ")
# uzunkenar = input("uzun kenarı getiriniz: ")
# cevre = (int(kısakenar) + int(uzunkenar)) * 2
# alan = int(kısakenar) * int(uzunkenar)
# print("Dikdörtgenin Çevresi: " + str(cevre))
# print("Dikdörtgenin Alanı: " + str(alan))
# yaricap = int(input("Yarıçapı giriniz: "))
# yukseklik = int(input("Yüksekliği giriniz: "))
# pisayisi = 3
# tabanAlani = pisayisi * yaricap * yaricap
# tabanCevresi = 2 * pisayisi * yaricap
# yanalAlan = yukseklik * tabanCevresi
# toplamAlan = yanalAlan + (2 * tabanAlani)
# hacim = tabanAlani * yukseklik
# print("Silindirin hacmi: " + str(hacim))
# print("Silindirin alanı: " + str(toplamAlan))
# yaricap = int(input("Yarıçapı giriniz: "))
# pisayisi = 3
# cevre = 2 * pisayisi * yaricap
# hacim = pisayisi * yaricap * yaricap
# print("Dairenin hacmi: " + str(hacim))
# print("Dairenin çevresi: " + str(cevre))
# print(len(str(1234567890)))
# print("Merhaba" [0])
# print(123 + 456)
# print(123_456_789)
# isimUzunluk = len(input("Merhaba, adın ne?: "))
# isimUzunluk_Str = str(isimUzunluk)
# print("İsminde " + isimUzunluk_Str + "karakter var.")
# fl = float(1.322)
# print(type(fl))
# intt = int(232)
# print(type(intt))
# st = str(123123)
# print(type(st))
# print(100 + float(15.23))
# print(str(122) + str(324))
# yas = input("Kaç yaşındasın?")
# yas_int = int(yas)
# ay = yas_int * 12
# hafta = yas_int * 52
# gun = yas_int * 365
# print(f"{ay} aylıksın")
# print(f"{hafta} haftalıksın")
# print(f"{gun} günlüksün")
# print("Lunaparka hoşgeldiniz!")
# print("Bilet fiyatı yetişkinler için 30 tl, 10 yaşından küçükler için 18 tl")
# boy = int(input("Lütfen boyunuzu giriniz: (cm)"))
# yas = int(input("Lütfen yaşınızı giriniz: "))
# biletfiyati = 0
# if boy > 100 :
#     if(yas<10):
#         biletfiyati = 18
#     else:
#         biletfiyati = 30
#     print(f"Crazy Dance'a binebilirsiniz! Fiyat {biletfiyati} TL") 
# elif boy > and boy < 100
#     if(yas < 10):
#         bilatfiyati = 18
#     else:,
#         biletfiyati = 30
#     print("Hız trenine binebilirsiniz! Fiyat {biletfiyati}  TL")
# elif boy > 100 and boy < 150:
#     if(yas < 10):
#         biletfiyati = 18
# else:
#     print("Lunaparktaki hic bir alete boyunuz yetmiyor")


# sayi = int(input("Lütfen tek mi çift mi olduğunu öğrenmek için bir sayı giriniz."))
# kalan = sayi % 2
# if kalan ==0:
#         print("Girdiğiniz sayı bir çift sayıdır!")
# else:
#         print("Girdiğiniz sayı bir tek sayıdır!")
# boy = float(input("Boyunuzu giriniz (m): "))
# kilo = float(input("Kilonuzu giriniz (kg): "))

# vki = int(kilo/boy**2)
# if vki < 18.5:
#     print(f"Vücut kütle indeksiniz: {vki} , Zayıfsınız!")
# elif vki > 18.5 and vki < 25:
#     print(f"Vücut kütle indeksiniz: {vki} , Kilonuz Normal!")
# elif vki > 25 and vki < 30:
#     print(f"Vücut kütle indeksiniz: {vki} , Kilolusunuz!")
# elif vki > 30 and vki < 35:
#     print(f"Vücut kütle indeksiniz: {vki} , Obezsiniz!")
# elif vki > 35:
#     print(f"Vücut kütle indeksiniz: {vki} , Aşırı Obezsiniz!")

# yil = int(input("Hangi yılı kontrol etmek istiyorsunuz?"))
# if yil % 4 == 0:
#     if yil % 100 == 0:
#         if yil % 400 == 0:
#             print(f"{yil} bir artık yıldır!")
#         else:
#             print(f"{yil} bir artık yıl değildir!.")
#     else:
#          print(f"{yil} bir artık yıl değildir!.")
# else:
#     print(f"{yil} bir artık yıl değildir!.")
# boy = input("Mezitli Pizzaya hoşgeldiniz! Hangi Boy pizza istersiniz? K veya O veya B =>")

# ekstraSos = input("Ekstra sos ister misiniz? E veya H =>")
# ekstraPeynir = input("Ekstra peynir ister misiniz? E veya H =>")
# toplam = 0 
# if boy == "K":
#     toplam += 15
# elif boy == "O":
#     toplam += 20 
# elif boy == "B":
#     toplam += 25

# if ekstraSos == "E":
#     if boy == "K":
#         toplam += 2
#     else:
#         toplam += 5
# if ekstraPeynir == "E":
#     toplam += 3

# print(f"Toplam Ödeme = {toplam}")

# print("Sevgi Hesaplayıcıya hoşgeldiniz!")
# isim1 = input("Adınız nedir?")
# isim2 = input("Onun adı nedir?")

# isimler = ( isim1 + isim2 ).lower()

# g = isimler.count("g")
# e = isimler.count("e")
# r = isimler.count("r")
# ç = isimler.count("ç")
# e = isimler.count("e")
# k = isimler.count("k")
# a = isimler.count("a")
# ş = isimler.count("ş")
# k = isimler.count("k")

# toplam = g + e + r + ç + e + k + a + ş + k

# if( toplam < 10 ):
#     print(f"Sevgi puaınınız: {toplam}, kane ve aj lee  gibisiniz!")
# elif( toplam > 10):
#     print(f"Sevgi puanınız: {toplam}, seth ve becky  gibisiniz!")
# else:
#     print(f"Sevgi puanınız: {toplam}")
#     print('''
# ___________                        _________                      __  .__    .__                 
# \__    ___/__.__.______   ____    /   _____/ ____   _____   _____/  |_|  |__ |__| ____    ____   
#   |    | <   |  |\____ \_/ __ \   \_____  \ /  _ \ /     \_/ __ \   __\  |  \|  |/    \  / ___\  
#   |    |  \___  ||  |_> >  ___/   /        (  <_> )  Y Y  \  ___/|  | |   Y  \  |   |  \/ /_/  > 
#   |____|  / ____||   __/ \___  > /_______  /\____/|__|_|  /\___  >__| |___|  /__|___|  /\___  /  
#           \/     |__|        \/          \/             \/     \/          \/        \//_____/   
# ''')
# yas = int(input("Kaç yaşındasınız"))
# if yas >= 18:
#     saglık = input("Sağlıklı mısın? e veya h =>")
#     if saglık == "e":
#         print("Ehliyet alabilirin")
#     else:
#         print("Üzgünüm, ehliyet alamzsın")
# else:
#     print("Üzgünüm, ehliyet alamzsın")
# sifre = "005162"
# print("Mezitli Bankasına Hoşgeldiniz!")
# sifreGirilen = input("Lütfen şifrenizi giriniz!")
# print(sifreGirilen)
# if len(sifreGirilen) != 6:
#     print("Eksik ya da fazla tuşladınız!")
# elif sifre == sifreGirilen:
#     print("Hoşgeldiniz!")
# else:
#     print("Yanlış tuşladınız!")
# import math
# boy = float(input("Boyunuzu metre cinsinden giriniz!"))
# kilo = int(input("Kilonuzu kilogram cinsinden giriniz!"))

# idealKilo = math.floor(22*boy*boy)
# fark = abs(idealKilo - kilo)
# if idealKilo > kilo:
#     print(f"{fark} kilo almalısınız!")
# else:
#     print(f"{fark} kilo vermelisiniz!")
# sayi1 = int(input("1nci Sayıyı Giriniz!"))
# sayi2 = int(input("2nci Sayıyı Giriniz!"))
# sayi3 = int(input("3nci Sayıyı Giriniz!"))
# sayi4 = int(input("4nci Sayıyı Giriniz!"))
# sayi5 = int(input("5nci Sayıyı Giriniz!"))
# enBuyuk = sayi1

# if enBuyuk < sayi2:
#     enBuyuk  = sayi2
# if enBuyuk < sayi3:
#     enBuyuk  = sayi3
# if enBuyuk < sayi4:
#     enBuyuk  = sayi4
# if enBuyuk < sayi5:
#     enBuyuk  = sayi5 

# print(f"Girilen Sayılardan En Büyüğü = {enBuyuk}")
# import random

# randomSayi = random.randint(1,3)
# cevap = int(input("Taş (1), Kağıt (2)  Makas (3) Seçiniz"))
sehirler = ["Adana","Adıyaman","Afyonkarahisar","Ağrı","Aksaray","Amasya","Ankara","Antalya","Ardahan","Artvin","Aydın","Balıkesir","Bartın","Batman",
"Bayburt","Bilecik","Bingöl","Bitlis","Bolu","Burdur","Bursa","Çanakkale","Çankırı","Çorum","Denizli","Diyarbakır","Düzce","Edirne","Elazığ",
"Erzincan","Erzurum","Eskişehir","Gaziantep","Giresun","Gümüşhane","Hakkari","Hatay","Iğdır","Isparta","İstanbul","İzmir","Kahramanmaraş","Karabük",
"Karaman","Kars","Kastamonu","Kayseri","Kilis","Kırıkkale","Kırklareli","Kırşehir","Kocaeli","Konya","Kütahya",
"Malatya","Manisa","Mardin","Mersin","Muğla","Muş","Nevşehir","Niğde","Ordu","Osmaniye","Rize","Sakarya","Samsun","Şanlıurfa",
"Siirt","Sinop","Şırnak","Sivas","Tekirdağ","Tokat","Trabzon","Tunceli","Uşak","Van","Yalova","Yozgat","Zonguldak"]
# print(sehirler[0])
# print(sehirler.index("Adana"))
# print(sehirler[12])
# print(sehirler[80])
# print(sehirler[-1]) 
# print(sehirler[-2]) 
# sehirler[33] = "İçel"
# print(sehirler[33])

# sehirler.append("Tarsus")
# print(sehirler[81])
# print(len(sehirler))
# sehirler.remove("Tarsus")
# print(len(sehirler))
# sehirler.pop()
# print(len(sehirler))
# import random
# isimler = "Gekkoberk, Met, Sedo, Halinur, Xagan, Cemokero"
# isimDizisi = isimler.split(", ")
# index = random.randint(0, len(isimDizisi) - 1 )
# print(f"Hesabı {isimDizisi[index]} ödeyecek!")
# row1 = ['⬜️', '⬜️', '⬜️']
# row2 = ['⬜️', '⬜️', '⬜️']
# row3 = ['⬜️', '⬜️', '⬜️']
# harita = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}\n")

# pozisyon = input("Hazineyi nereye koymak istersin?\n")

# yatay = int(pozisyon[0]) -1
# dikey = int(pozisyon[1]) - 1 
# harita[dikey][yatay] = "X"
# print(f"{row1}\n{row2}\n{row3}\n")
# import random
# taş = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# kağıt = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# makas = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# while True:
#     kullaniciSecimi = int(input("Taş(0), Kağıt(1), Makas(2) seç!"))
#     bilgisayarSecimi = random.randint(0,2)

#     print("Senin Seçimin")
#     if kullaniciSecimi == 0:
#         print(taş)
#     elif kullaniciSecimi == 1:
#         print(kağıt)
#     elif kullaniciSecimi == 2:
#         print(makas)


#         if kullaniciSecimi >=3 or kullaniciSecimi < 0:
#             print("0 , 1 ,veya 2 giriniz!")
#     elif kullaniciSecimi == 0 and bilgisayarSecimi == 2:
#         print("Yendin!")
#     elif bilgisayarSecimi == 0 and kullaniciSecimi == 2:
#         print("Kaybettin!")
#     elif kullaniciSecimi > bilgisayarSecimi:
#         print("Yendin!")
#     elif bilgisayarSecimi > kullaniciSecimi:
#         print("Kaybettin!")
#     else:
#         print("Berabere!")
# def fonksiyonum():
#     print("Merhaba")
#     print("Dünya")
# fonksiyonum()
# meyveler = ["Elma", "Armut", "Şeftali"]
# for meyve in meyveler:
#     print(meyve)
_abs_(-7)
