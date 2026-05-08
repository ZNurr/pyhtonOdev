import random

# ============================================================
# ÖDEV 1 - Sayı Tahmin Oyunu
# ============================================================
def odev1():
    print("\n--- ÖDEV 1: Sayı Tahmin Oyunu ---")
    gizli_sayi = random.randint(1, 10)

    while True:
        tahmin = int(input("1 ile 10 arasında bir sayı tahmin et: "))
        if tahmin == gizli_sayi:
            print("Bildiniz!")
            break
        else:
            print("Yanlış! Tekrar deneyin.")


# ============================================================
# ÖDEV 2 - Liste İçinde En Büyük Sayıyı Bul (max() YASAK)
# ============================================================
def odev2():
    print("\n--- ÖDEV 2: En Büyük Sayıyı Bul ---")
    sayilar = [43, 7, 91, 25, 68, 12, 55]
    print(f"Liste: {sayilar}")

    en_buyuk = sayilar[0]
    for sayi in sayilar:
        if sayi > en_buyuk:
            en_buyuk = sayi

    print(f"En büyük sayı: {en_buyuk}")


# ============================================================
# ÖDEV 3 - Tek ve Çift Sayıları Ayır
# ============================================================
def odev3():
    print("\n--- ÖDEV 3: Tek ve Çift Sayıları Ayır ---")
    tekSayilar = []
    ciftSayilar = []

    for i in range(1, 6):
        sayi = int(input(f"{i}. sayıyı girin: "))
        if sayi % 2 == 0:
            ciftSayilar.append(sayi)
        else:
            tekSayilar.append(sayi)

    print(f"Tek Sayılar : {tekSayilar}")
    print(f"Çift Sayılar: {ciftSayilar}")


# ============================================================
# ÖDEV 4 - Şifre Güç Kontrolü
# ============================================================
def odev4():
    print("\n--- ÖDEV 4: Şifre Güç Kontrolü ---")
    sifre = input("Bir şifre girin: ")
    uzunluk = len(sifre)

    if uzunluk < 6:
        print("Zayıf şifre")
    elif uzunluk <= 10:
        print("Orta şifre")
    else:
        print("Güçlü şifre")


# ============================================================
# ÖDEV 5 - İsmi Tersten Yazdır
# ============================================================
def odev5():
    print("\n--- ÖDEV 5: İsmi Tersten Yazdır ---")
    isim = input("Bir isim girin: ")
    ters_isim = isim[::-1]
    print(f"Ters hali: {ters_isim}")


# ============================================================
# ÖDEV 6 - Listeyi Filtreleme (10'dan büyükler)
# ============================================================
def odev6():
    print("\n--- ÖDEV 6: Listeyi Filtreleme ---")
    sayilar = [3, 15, 8, 22, 5, 11, 1, 30, 9, 17]
    print(f"Orijinal liste: {sayilar}")

    buyuk_sayilar = []
    for sayi in sayilar:
        if sayi > 10:
            buyuk_sayilar.append(sayi)

    print(f"10'dan büyük olanlar: {buyuk_sayilar}")


# ============================================================
# ÖDEV 7 - Kullanıcıdan Sürekli Veri Alma
# ============================================================
def odev7():
    print("\n--- ÖDEV 7: Sürekli İsim Al (çıkmak için 'q') ---")
    isimler = []

    while True:
        isim = input("İsim girin (çıkmak için 'q'): ")
        if isim.lower() == "q":
            break
        isimler.append(isim)

    print(f"Girilen isimler: {isimler}")


# ============================================================
# ÖDEV 8 - Ortalama Hesapla ve Geçti/Kaldı
# ============================================================
def odev8():
    print("\n--- ÖDEV 8: 5 Not Ortalaması ---")
    notlar = []

    for i in range(1, 6):
        while True:
            not_ = float(input(f"{i}. notu girin (0-100): "))
            if 0 <= not_ <= 100:
                notlar.append(not_)
                break
            else:
                print("Geçersiz not! Lütfen 0 ile 100 arasında bir değer girin.")

    ortalama = sum(notlar) / len(notlar)
    print(f"Ortalama: {ortalama:.2f}")

    if ortalama >= 50:
        print("Sonuç: Geçti ✓")
    else:
        print("Sonuç: Kaldı ✗")


# ============================================================
# ÖDEV 9 - İki Listede Ortak Elemanları Bul
# ============================================================
def odev9():
    print("\n--- ÖDEV 9: Ortak Elemanları Bul ---")
    liste1 = [1, 2, 3, 4, 5, 6]
    liste2 = [4, 5, 6, 7, 8, 9]
    print(f"Liste 1: {liste1}")
    print(f"Liste 2: {liste2}")

    ortak = []
    for eleman in liste1:
        if eleman in liste2:
            ortak.append(eleman)

    print(f"Ortak elemanlar: {ortak}")


# ============================================================
# ÖDEV 10 - Menülü Program
# ============================================================
def odev10():
    print("\n--- ÖDEV 10: Menülü Program ---")
    sayilar = []

    while True:
        print("\n1- Sayı Ekle")
        print("2- Listeyi Göster")
        print("3- Çıkış")
        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            sayi = int(input("Eklenecek sayıyı girin: "))
            sayilar.append(sayi)
            print(f"{sayi} listeye eklendi.")
        elif secim == "2":
            print(f"Liste: {sayilar}")
        elif secim == "3":
            print("Çıkılıyor...")
            break


# ============================================================
# ANA MENÜ - Hangi ödevi çalıştırmak istediğinizi seçin
# ============================================================
if __name__ == "__main__":
    odevler = {
        "1": odev1,
        "2": odev2,
        "3": odev3,
        "4": odev4,
        "5": odev5,
        "6": odev6,
        "7": odev7,
        "8": odev8,
        "9": odev9,
        "10": odev10,
    }

    print("=" * 40)
    print("   PYTHON ÖDEVLER - ANA MENÜ")
    print("=" * 40)
    for numara in odevler:
        print(f"  {numara}. Ödev {numara}")
    print("  0. Çıkış")
    print("=" * 40)

    while True:
        secim = input("\nHangi ödevi çalıştırmak istiyorsunuz? (0 = Çıkış): ")
        if secim == "0":
            print("Çıkılıyor...")
            break
        elif secim in odevler:
            odevler[secim]()
        else:
            print("Geçersiz seçim! Lütfen 1-10 arası bir sayı girin.")
