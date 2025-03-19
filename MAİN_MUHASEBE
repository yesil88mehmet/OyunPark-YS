from muhasebe import Muhasebe
from rapor import Rapor

def main():
    muhasebe = Muhasebe()

    # Örnek gider ekleme
    muhasebe.gider_ekle("Elektrik faturası", 1500)
    muhasebe.personel_maasi_ekle("Ahmet", 5000)
    muhasebe.gelir_ekle("Giriş ücreti", 20000)
    muhasebe.gelir_ekle("Yiyecek satışları", 3000)

    rapor = Rapor()
    rapor.kar_zarar_raporu()

if _name_ == "_main_":
    main()
