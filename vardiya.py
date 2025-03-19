from veritabani import baglanti_olustur

# Vardiya ekleme fonksiyonu
def vardiya_ekle(personel_id, tarih, baslangic_saati, bitis_saati):
    conn, cursor = baglanti_olustur()
    cursor.execute("""
        INSERT INTO vardiya (personel_id, tarih, baslangic_saati, bitis_saati)
        VALUES (?, ?, ?, ?)
    """, (personel_id, tarih, baslangic_saati, bitis_saati))
    conn.commit()
    print(f"ID {personel_id} olan personelin {tarih} tarihli vardiyası eklendi.")
    conn.close()

# Vardiya listeleme fonksiyonu
def vardiya_listele(personel_id):
    conn, cursor = baglanti_olustur()
    cursor.execute("""
        SELECT * FROM vardiya WHERE personel_id = ?
    """, (personel_id,))
    vardiyalar = cursor.fetchall()
    print(f"\nID {personel_id} olan personelin vardiyaları:")
    for v in vardiyalar:
        print(f"Tarih: {v[2]}, Başlangıç Saati: {v[3]}, Bitiş Saati: {v[4]}")
    conn.close()
