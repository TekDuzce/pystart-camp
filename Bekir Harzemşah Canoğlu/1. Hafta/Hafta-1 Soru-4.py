rehber = {'Ali': '0555 111 22 33', 'Ayşe': '0532 444 55 66'}

print("--- 1. Yeni Kişi Ekleme ---")
# Kullanıcıdan isim ve numara alıp rehbere ekle
while True:
    yeni_isim = input("Eklenecek kişinin adı: ").strip()
    # İsime boş bırakmak ve numarayı engelleme
    if yeni_isim == "" or yeni_isim.isdigit():
        print("Hata: Geçerli bir isim girmelisiniz (Boş bırakılamaz ve sadece sayı olamaz).")
        continue
    break

while True:
    yeni_no = input("Eklenecek kişinin numarası (Örn: 05551112233): ").strip()
    # Numaranın boş olmadığını ve sadece rakamlardan olup olmadığını kontrol 
    # Boşlukları temizleyip rakam kontrolü
    temiz_no = yeni_no.replace(" ", "")
    if temiz_no.isdigit() and len(temiz_no) >= 10:
        break
    else:
        print("Hata: Geçerli bir telefon numarası giriniz (Sadece rakam içermelidir ve en az 10 haneli olmalıdır).")

rehber[yeni_isim] = yeni_no
print(f"'{yeni_isim}' başarıyla rehbere eklendi.\n")


# Alinin numarasını güncelle
print("--- 2. Numara Güncelleme ---")
rehber['Ali'] = '0555 999 88 77'
print(f"Ali'nin yeni numarası güncellendi: {rehber['Ali']}\n")


# Ayşeyi rehberden sil ve silinen numarayı ekle
print("--- 3. Kişi Silme ---")
silinen_no = rehber.pop('Ayşe', 'Kayıt bulunamadı')
print(f"Ayşe rehberden silindi. Silinen Numara: {silinen_no}\n")


# Kullanıcıdan bir isim al ve numarasını yazdır
print("--- 4. Numara Sorgulama ---")
while True:
    aranan_isim = input("Numarasını öğrenmek istediğiniz kişinin adı: ").strip()
    if aranan_isim == "":
        print("Hata: İsim alanı boş bırakılamaz.")
        continue
    break

# get() metodu ile güvenli sorgulama
numara = rehber.get(aranan_isim, 'Kayıt bulunamadı')
print(f"Sonuç: {numara}\n")


# Rehberdeki kişi sayısını ve isimleri alfabetik sırayla yazdır
print("--- 5. Rehber Özeti ---")
kisi_sayisi = len(rehber)
alfabetik_isimler = sorted(rehber.keys())

print(f"Toplam kişi sayısı: {kisi_sayisi}")
print(f"Alfabetik sıralı isimler: {alfabetik_isimler}")
print(f"Güncel Rehber: {rehber}")