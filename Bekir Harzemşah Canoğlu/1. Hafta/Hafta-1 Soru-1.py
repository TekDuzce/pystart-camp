# Ekranı temizleme fonksiyonu
def ekranı_temizle():
    print("\033c", end="")

# Başlangıç ekranı
ekranı_temizle()
print("========================================")
print("     PyStart Katılımcı Kayıt Ekranı     ")
print("========================================")

# Kullanıcıdan ad, soyad ve bölüm bilgilerinin alındığı ekran
ad = input("Adınız: ") # while any kullanarak adın içinde rakam olup olmadığını kontrol ediyoruz diğerlerindede aynı şekilde
while any(char.isdigit() for char in ad):
    ekranı_temizle()
    print("Hatalı giriş! Adınızda rakam bulunamaz.")
    ad = input("Adınız: ")

soyad = input("Soyadınız: ")
while any(char.isdigit() for char in soyad):
    ekranı_temizle()
    print("Hatalı giriş! Soyadınızda rakam bulunamaz.")
    soyad = input("Soyadınız: ")

bolum = input("Bölümünüz: ")
while any(char.isdigit() for char in bolum):
    ekranı_temizle()
    print("Hatalı giriş! Bölümünüzde rakam bulunamaz.")
    bolum = input("Bölümünüz: ")

# Yıl ekranı
ekranı_temizle()
while True:
    yil_str = input("Doğum yılınız (Max 2026): ")
    if yil_str.isdigit():
        yil = int(yil_str)
        if 1900 <= yil <= 2026:
            break
    ekranı_temizle()
    print("Hatalı giriş! 1900 - 2026 arasında geçerli bir yıl girin.")

# Ay ekranı
ekranı_temizle()
while True:
    ay_str = input("Doğum ayınız (1-12): ")
    if ay_str.isdigit():
        ay = int(ay_str)
        if 1 <= ay <= 12:
            break #break direk while True döngüsünden çıkıyor ve bir sonraki adıma geçiyor
    ekranı_temizle()
    print("Hatalı giriş! 1 - 12 arasında geçerli bir ay girin.")

# Gün ekranı
ekranı_temizle()
while True:
    # Ayın gün sayısını hesaplayalım
    if ay in (1, 3, 5, 7, 8, 10, 12):
        max_gun = 31
    elif ay in (4, 6, 9, 11):
        max_gun = 30
    else:  # Şubat için artık yıl kontrolü 
           # bu kısım yapay zekayla yapıldı
        if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
            max_gun = 29
        else:
            max_gun = 28
            
    gun_str = input(f"Doğum gününüz (1-{max_gun}): ") #burada f string kullanarak bir stringin içerisine değişken gömebiliyoruz :D
    if gun_str.isdigit():
        gun = int(gun_str)
        if 1 <= gun <= max_gun:
            break
            
    ekranı_temizle()
    print(f"Hatalı giriş! Bu ay için 1 - {max_gun} arasında bir gün girin.")

# Doğum tarihini tuple'da tutalım ve yaş hesaplayalım
dogum_tarihi = (gun, ay, yil)
yas = 2026 - dogum_tarihi[2]

ad_soyad = f"{ad.title()} {soyad.title()}"
dogum_str = f"{dogum_tarihi[0]:02d}.{dogum_tarihi[1]:02d}.{dogum_tarihi[2]}"

# Sonuç kartı ekranı
ekranı_temizle()
print("========================================")
print("PyStart Katılımcı Kartı")
print("========================================")
print(f"Ad Soyad    : {ad_soyad}")
print(f"Bölüm       : {bolum}")
print(f"Doğum       : {dogum_str}")
print(f"Yaş         : {yas}")
print("========================================")