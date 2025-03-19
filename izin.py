from veritabani import baglanti_olustur

# İzin ekleme fonksiyonu
def izin_ekle(personel_id, tarih, izin_turu, durum):
    conn, cursor = baglanti_olustur()
    cursor.execute("""
        INSERT INTO izin (personel_id, tarih, izin_turu, durum)
        VALUES (?, ?, ?, ?)
    """, (personel_id, tarih, izin_turu, durum))
    conn.commit()
    print(f"ID {personel_id} olan personelin {tarih} tarihli izni başarıyla eklendi!")
    conn.close()

# İzin listeleme fonksiyonu
def izin_listele(personel_id):
    conn, cursor = baglanti_olustur()
    cursor.execute("""
        SELECT * FROM izin WHERE personel_id = ?
    """, (personel_id,))
    izinler = cursor.fetchall()
    print(f"\nID {personel_id} olan personelin izinleri:")
    for i in izinler:
        print(f"Tarih: {i[2]}, İzin Türü: {i[3]}, Durum: {i[4]}")
    print("-------------------------")
    conn.close()
