from veritabani import baglanti_olustur

# Personel ekleme fonksiyonu
def personel_ekle(ad, soyad, pozisyon, maas):
    conn, cursor = baglanti_olustur()
    cursor.execute("""
        INSERT INTO personel (ad, soyad, pozisyon, maas)
        VALUES (?, ?, ?, ?)
    """, (ad, soyad, pozisyon, maas))
    conn.commit()
    print(f"{ad} {soyad} başarıyla eklendi!")
    conn.close()

# Personel listeleme fonksiyonu
def personel_listele():
    conn, cursor = baglanti_olustur()
    cursor.execute("SELECT * FROM personel")
    personeller = cursor.fetchall()
    print("\nPersonel Listesi:")
    for p in personeller:
        print(f"ID: {p[0]}, Ad: {p[1]}, Soyad: {p[2]}, Pozisyon: {p[3]}, Maaş: {p[4]}")
    conn.close()

# Personel güncelleme fonksiyonu
def personel_guncelle(personel_id, yeni_ad, yeni_soyad, yeni_pozisyon, yeni_maas):
    conn, cursor = baglanti_olustur()
    cursor.execute("""
        UPDATE personel
        SET ad = ?, soyad = ?, pozisyon = ?, maas = ?
        WHERE id = ?
    """, (yeni_ad, yeni_soyad, yeni_pozisyon, yeni_maas, personel_id))
    conn.commit()
    print(f"ID {personel_id} olan personel güncellendi.")
    conn.close()

# Personel silme fonksiyonu
def personel_sil(personel_id):
    conn, cursor = baglanti_olustur()
    cursor.execute("DELETE FROM personel WHERE id = ?", (personel_id,))
    conn.commit()
    print(f"ID {personel_id} olan personel silindi.")
    conn.close()
