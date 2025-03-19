from personel import personel_ekle, personel_listele, personel_guncelle, personel_sil
from vardiya import vardiya_ekle, vardiya_listele
from izin import izin_ekle, izin_listele
from veritabani import tablo_olustur, izin_tablosu_olustur

# Menü Sistemi
def menu():
    while True:
        print("\n1. Personel Ekle")
        print("2. Personel Listele")
        print("3. Personel Güncelle")
        print("4. Personel Sil")
        print("5. Vardiya Ekle")
        print("6. Personel Vardiya Listele")
        print("7. İzin Ekle")
        print("8. Personel İzin Listele")
        print("9. Çıkış")
        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            ad = input("Ad: ")
            soyad = input("Soyad: ")
            pozisyon = input("Pozisyon: ")
            maas = float(input("Maaş: "))
            personel_ekle(ad, soyad, pozisyon, maas)

        elif secim == "2":
            personel_listele()

        elif secim == "3":
            personel_id = int(input("Güncellenecek personelin ID'si: "))
            yeni_ad = input("Yeni Ad: ")
            yeni_soyad = input("Yeni Soyad: ")
            yeni_pozisyon = input("Yeni Pozisyon: ")
            yeni_maas = float(input("Yeni Maaş: "))
            personel_guncelle(personel_id, yeni_ad, yeni_soyad, yeni_pozisyon, yeni_maas)

        elif secim == "4":
            personel_id = int(input("Silinecek personelin ID'si: "))
            personel_sil(personel_id)

        elif secim == "5":
            personel_id = int(input("Vardiya eklenecek personelin ID'si: "))
            tarih = input("Vardiya Tarihi (YYYY-MM-DD): ")
            baslangic_saati = input("Başlangıç Saati (HH:MM): ")
            bitis_saati = input("Bitiş Saati (HH:MM): ")
            vardiya_ekle(personel_id, tarih, baslangic_saati, bitis_saati)

        elif secim == "6":
            personel_id = int(input("Vardiyaları görüntülemek için personel ID'si: "))
            vardiya_listele(personel_id)

        elif secim == "7":
            personel_id = int(input("İzin eklenecek personelin ID'si: "))
            tarih = input("İzin Tarihi (YYYY-MM-DD): ")
            izin_turu = input("İzin Türü: ")
            durum = input("İzin Durumu (Onaylı/Bekliyor/Reddedildi): ")
            izin_ekle(personel_id, tarih, izin_turu, durum)

        elif secim == "8":
            personel_id = int(input("İzinleri görüntülemek için personel ID'si: "))
            izin_listele(personel_id)

        elif secim == "9":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim! Tekrar deneyin.")

# Veritabanı tablosunu oluştur
tablo_olustur()
izin_tablosu_olustur()

# Menüyü başlat
menu()

