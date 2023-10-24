import random
#kullanıcıdan girmesini ve varsa her kolona eklenecek şanslı sayı girmesini istiyoruz
print()
print()
kolon_sayisi = int(input("kolon sayısını girin: "))
print("Şanslı sayı her kolonda olmasını istediğiniz sayıdır")
sansli_sayi_var = input("Şanslı sayı eklemek istiyorsanız lütfen 1'e basın basın: ")
eleman_sayisi = 6
#eğer şanslı sayı varsa 6 tane random sayı alacak yoksa 5 random sayı alacak
if sansli_sayi_var == "1":
    sansli_sayi = int(input("Şanslı sayınızı girin: "))
    eleman_sayisi = 5
#tüm kolonların kaydedileceği kupon listesi
kupon = []

for kol in range(kolon_sayisi):
    
    for i in range(kolon_sayisi):
        kolon = []  
        # şanslı sayı varsa kolona ekleme
        if sansli_sayi_var == "1": 
            kolon.append(sansli_sayi)
        #kolonun geriye kalan elemanlarını ekleme 
        for j in range(eleman_sayisi):
            sayi = random.randint(1, 90)
            #sayıların birbirinden farklı olmasını istiyoruz
            if (sayi not in kolon):
                kolon.append(sayi)
            else: 
                sayi = random.randint(1, 90)
                kolon.append(sayi)
    # kolonu kupona ekledik
    kupon.append(kolon)
#kuponu ekrana yazdırma
for item in kupon:
    print(f"{kupon.index(item) + 1}.kolon = ", item)
print()
print()