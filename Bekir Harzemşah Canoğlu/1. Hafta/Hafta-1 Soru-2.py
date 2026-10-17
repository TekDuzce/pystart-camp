# Kullanıcıdan bir cümle alıyoruz
cumle = input("Lütfen bir cümle girin: ")

# 1. Karakter sayısı ve boşluklar hariç karakter sayısı
toplam_karakter = len(cumle)
bosluksuz_karakter = len(cumle.replace(" ", ""))

# 2. Kelime sayısı, ilk kelime ve son kelime
kelimeler = cumle.split()
kelime_sayisi = len(kelimeler)

if kelime_sayisi > 0:
    ilk_kelime = kelimeler[0]
    son_kelime = kelimeler[-1]
else:
    ilk_kelime = ""
    son_kelime = ""

# 3. Cümlenin tamamen büyük harfli hali ve tersten yazılışı
# Gözlem: Türkçe karakterlerde 'i' harfi büyük harfe dönüştüğünde 'İ' olur. 
# Ancak standart upper() fonksiyonu Türkçe'ye tam uyum sağlamayabilir (örneğin İngilizce karakter setine göre davranabilir).
# Python'da i -> İ dönüşümünde 'I' ile 'İ' ayrımına dikkat edilmelidir.
# BU KISIM YAPAY ZEKAYLA YAPILDI
buyuk_harfli = cumle.upper()
tersten_yazilis = cumle[::-1]

# 4. Cümlede kaç tane 'a' harfi olduğu anlar (büyük-küçük fark etmeden)
a_sayisi = cumle.lower().count('a')

# 5. Cümlede 'python' kelimesinin geçip geçmediği (True ya da False)
python_geciyor_mu = 'python' in cumle.lower()

print("-" * 30)
print(f"1. Karakter sayısı: {toplam_karakter}, Boşluksuz karakter sayısı: {bosluksuz_karakter}")
print(f"2. Kelime sayısı: {kelime_sayisi}, İlk kelime: '{ilk_kelime}', Son kelime: '{son_kelime}'")
print(f"3. Büyük harfli hali: {buyuk_harfli}")
print(f"   Tersten yazılışı: {tersten_yazilis}")
print(f"4. 'a' harfi sayısı: {a_sayisi}")
print(f"5. 'python' kelimesi geçiyor mu?: {python_geciyor_mu}")