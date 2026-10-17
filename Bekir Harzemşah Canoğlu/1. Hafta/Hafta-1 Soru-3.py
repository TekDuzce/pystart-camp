# Üç notu al
print("Lütfen aralarında boşluk bırakarak 3 adet not girin (Örn: 70 85 90):")
while True:
    girdi = input("3 not: ")
    parcalar = girdi.split()
    
    # Tam olarak 3 parça girilmiş mi kontrol
    if len(parcalar) != 3:
        print(f"Hata: 3 adet sayı girmelisiniz (Siz {len(parcalar)} tane girdiniz). Tekrar deneyin.")
        continue
        
    # Her bir parçanın tamamen rakamlardan oluşup oluşmadığını kontrol et
    gecerli_mi = True
    for p in parcalar:
        if not p.isdigit():
            gecerli_mi = False
            break
            
    if gecerli_mi:
        # Hepsi sayıysa listeye çevir
        notlar = [int(n) for n in parcalar]
        break
    else:
        print("Hata: Girdiğiniz değerler arasında harf veya geçersiz karakterler var. Tekrar deneyin.")

# tekrar not al ve ekle
while True:
    yeni_not_girdi = input("Bir not daha ekle: ")
    if yeni_not_girdi.isdigit():
        yeni_not = int(yeni_not_girdi)
        notlar.append(yeni_not)
        break
    else:
        print("Hatalı giriş! Lütfen sadece pozitif bir sayı giriniz.")

# küçükten büyüğe sırala ve yazdır
notlar.sort()
print(f"Notlar (sıralı): {notlar}")

# En düşük en yüksek ve ortalamayı yazdır
en_dusuk = notlar[0]
en_yuksek = notlar[-1]
ortalama = sum(notlar) / len(notlar)
print(f"En düşük: {en_dusuk} | En yüksek: {en_yuksek}")
print(f"Ortalama: {ortalama:.2f}")

# bu satır altı yapay zekayla yazıldı
# En düşük notu listeden çıkar ve yeni ortalamayı yazdır
notlar.pop(0)  # İlk eleman (en düşük not) listeden çıkarılır
yeni_ortalama = sum(notlar) / len(notlar)
print(f"En düşük not çıkarıldı: {notlar}")
print(f"Yeni ortalama: {yeni_ortalama:.2f}")