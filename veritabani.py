import sqlite3

# Veritabanı bağlantısı oluşturma
def baglanti_olustur():
    conn = sqlite3.connect('oyunparkı.db')
    cursor = conn.cursor()
    return conn, cursor

# Personel tablosunu oluşturma
def tablo_olustur():
    conn, cursor = baglanti_olustur()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS personel (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ad TEXT,
        soyad TEXT,
        pozisyon TEXT,
        maas REAL
    )
    """)
    conn.commit()
    conn.close()

# İzin tablosunu oluşturma
def izin_tablosu_olustur():
    conn, cursor = baglanti_olustur()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS izin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        personel_id INTEGER,
        tarih TEXT NOT NULL,
        izin_turu TEXT NOT NULL,
        durum TEXT NOT NULL,
        FOREIGN KEY (personel_id) REFERENCES personel(id)
    )
    """)
    conn.commit()
    conn.close()
