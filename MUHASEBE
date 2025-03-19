import csv
import os

class Muhasebe:
    def _init_(self):
        self.giderler = self.dosya_yukle('../data/giderler.csv')
        self.gelirler = self.dosya_yukle('../data/gelirler.csv')
        self.personel_maaslari = self.dosya_yukle('../data/personel.csv')

    def dosya_yukle(self, dosya):
        if os.path.exists(dosya):
            with open(dosya, mode='r') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        return []

    def gider_ekle(self, aciklama, tutar):
        self.giderler.append({'aciklama': aciklama, 'tutar': float(tutar)})
        self.dosya_kaydet('../data/giderler.csv', self.giderler)

    def gelir_ekle(self, aciklama, tutar):
        self.gelirler.append({'aciklama': aciklama, 'tutar': float(tutar)})
        self.dosya_kaydet('../data/gelirler.csv', self.gelirler)

    def personel_maasi_ekle(self, isim, maas):
        self.personel_maaslari.append({'isim': isim, 'maas': float(maas)})
        self.dosya_kaydet('../data/personel.csv', self.personel_maaslari)

    def toplam_gider(self):
        toplam_gider = sum(float(g['tutar']) for g in self.giderler)
        toplam_maas = sum(float(p['maas']) for p in self.personel_maaslari)
        return toplam_gider + toplam_maas

    def toplam_gelir(self):
        return sum(float(g['tutar']) for g in self.gelirler)

    def dosya_kaydet(self, dosya, veri):
        with open(dosya, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=veri[0].keys())
            writer.writeheader()
            writer.writerows(veri)
