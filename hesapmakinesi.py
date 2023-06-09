print("lütfen yapmak istediğiniz işlemi şeçin")
print("1. toplama")
print("2. çıkarma")
print("3. çarpma")
print("4. bölme")

secim = input("seçiminizi yapınız (1/2/3/4)")

sayi1 = float(input("İlk sayıyı giriniz : "))
sayi2 = float(input("İkinci sayıyı giriniz :"))

def topla(x,y):
    return x+y

def cikar(x,y):
    return x-y

def carp(x,y):
    return x*y

def bol(x,y):
    return x/y

if secim == "1":
    print("Toplama işlemi sonucu : ", topla(sayi1, sayi2))
elif secim == "2":
    print("Çıkarma işlemi sonucu : ", cikar(sayi1, sayi2))
elif secim == "3":
    print("Çarpma işlemi sonucu : ", carp(sayi1, sayi2))
elif secim == "4":
    print(" Bölme işlemi sonucu : ", bol(sayi1, sayi2))
if sayi2 == 0:
    print("infinity, bir sayı 0'a bölünemez.")
else:
    print(" Bölme işlemi sonucu : ", bol(sayi1, sayi2))

else:
    print("geçersiz")