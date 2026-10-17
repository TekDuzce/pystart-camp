# hobileri al ve kümeye koy
print("--- 1. Hobilerin Alınması ---")

while True:
    girdi1 = input("1. kişinin hobilerini virgülle ayırarak yaz (Örn: futbol,satranç,müzik): ").strip()
    if girdi1 == "":
        print("Hata: Bu alan boş bırakılamaz.")
        continue
    # Virgülle ayırıp boşlukları temizleyerek kümeye dönüştür
    hobi_kumesi1 = {hobi.strip() for hobi in girdi1.split(",") if hobi.strip() != ""}
    if len(hobi_kumesi1) == 0: # bu kısmı yapay zeka yaptı anlamadım ilk kez gördüm strip() i
        print("Hata: Geçerli en az bir hobi girmelisiniz.")
        continue
    break

while True:
    girdi2 = input("2. kişinin hobilerini virgülle ayırarak yaz (Örn: tenis,satranç,kitap): ").strip()
    if girdi2 == "":
        print("Hata: Bu alan boş bırakılamaz.")
        continue
    hobi_kumesi2 = {hobi.strip() for hobi in girdi2.split(",") if hobi.strip() != ""}
    if len(hobi_kumesi2) == 0:
        print("Hata: Geçerli en az bir hobi girmelisiniz.")
        continue
    break

print("\n--- 2. Küme İşlemleri ve Hobiler ---")

# Ortak hobiler
ortak_hobiler = hobi_kumesi1.intersection(hobi_kumesi2)
print(f"Ortak hobiler: {sorted(ortak_hobiler)}")

# Yalnızca birinci kişide olanlar
sadece_1de_olanlar = hobi_kumesi1.difference(hobi_kumesi2)
print(f"Yalnızca 1. kişide olanlar: {sorted(sadece_1de_olanlar)}")

# Yalnızca ikinci kişide olanlar
sadece_2de_olanlar = hobi_kumesi2.difference(hobi_kumesi1)
print(f"Yalnızca 2. kişide olanlar: {sorted(sadece_2de_olanlar)}")

# Tüm hobiler
tum_hobiler = hobi_kumesi1.union(hobi_kumesi2)
print(f"Tüm hobiler (Birleşim): {sorted(tum_hobiler)}")


print("\n--- 3. Mantıksal Sorular ---")

# Ortak Kesişim kümesi boş değilse True döner
ortak_var_mi = len(ortak_hobiler) > 0
print(f"Ortak hobiniz var mı?: {ortak_var_mi}")

# Hobi sayılarınız eşit mi?
sayilar_esit_mi = len(hobi_kumesi1) == len(hobi_kumesi2)
print(f"Hobi sayılarınız eşit mi?: {sayilar_esit_mi}")

# İkiniz de en az 3 hobi yazdınız mı?
en_az_uc_mu = len(hobi_kumesi1) >= 3 and len(hobi_kumesi2) >= 3
print(f"İkiniz de en az 3 hobi yazdınız mı?: {en_az_uc_mu}")

# "satranç" ikinizden birinin hobisi mi? (Tüm hobiler kümesinde 'satranç' var mı?)
satranc_var_mi = 'satranç' in tum_hobiler
print(f"'satranç' ikinizden birinin hobisi mi?: {satranc_var_mi}")