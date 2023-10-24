# taş-kağıt-makas
import random
print()
print()

bitis = int(input("Kaç olan kazansın: "))
hamleler = [ "Taş", "Kağıt", "Makas" ]
bilgisayar_puan = 0
kullanıcı_puan = 0

for hamle in hamleler:
    print(f"{hamleler.index(hamle) }",hamle)
while True:  

    # kullanıcı seçim yapar
    kullanıcı_secim = hamleler[int(input("Ne yapmak istersiniz: "))]
    print()
    print(f"Siz {kullanıcı_secim} yaptınız")

    # makine hamleler dizisinden random seçim yapar
    bilgisayar_secim = random.choice(hamleler)
    print(f"Bilgisayar {bilgisayar_secim} yaptı")

    # kullanıcı ve bilgisayar aynı işareti yapars apuan aynı kalır
    if kullanıcı_secim == bilgisayar_secim:
        print(f"Siz: {kullanıcı_puan} - {bilgisayar_puan}: Bilgisayar")
        continue

    # kullanıcının kazanma ihtimalleri kazanınca puanı 1 artar
    elif (kullanıcı_secim == "Taş" and bilgisayar_secim == "Makas") or (kullanıcı_secim == "Makas" and bilgisayar_secim == "Kağıt") or (kullanıcı_secim == "Kağıt" and bilgisayar_secim == "Taş"):
        print("Bu eli kazandınız")
        kullanıcı_puan +=1
        print(f"Siz: {kullanıcı_puan} - {bilgisayar_puan}: Bilgisayar")
        print()

    # Bilgisayarın kazanma ihtimalleri kazanınca puanı 1 artar
    else:
        print("Bu eli kaybettiniz")
        bilgisayar_puan +=1
        print(f"Siz: {kullanıcı_puan} - {bilgisayar_puan}: Bilgisayar")
        print()

    # bitiş
    if kullanıcı_puan == bitis or bilgisayar_puan == bitis:
        if kullanıcı_puan < bilgisayar_puan:
            print(f"Oyun bitti Siz: {kullanıcı_puan} Bilgisayar: {bilgisayar_puan}")
            print()
        else:
            print(f"Oyun bitti Siz: {kullanıcı_puan} Bilgisayar: {bilgisayar_puan}")
            print()
        break
    print("----------------------------------------------------")

    
    



