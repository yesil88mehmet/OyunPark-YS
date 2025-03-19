from muhasebe import Muhasebe

class Rapor:
    def _init_(self):
        self.muhasebe = Muhasebe()

    def kar_zarar_raporu(self):
        toplam_gelir = self.muhasebe.toplam_gelir()
        toplam_gider = self.muhasebe.toplam_gider()
        net_kar = toplam_gelir - toplam_gider

        print("\n===== Kâr-Zarar Raporu =====")
        print(f"Toplam Gelir: {toplam_gelir:.2f} TL")
        print(f"Toplam Gider: {toplam_gider:.2f} TL")
        print(f"Net Kâr/Zarar: {net_kar:.2f} TL")

        if net_kar > 0:
            print("Sonuç: Kârda ✅")
        elif net_kar < 0:
            print("Sonuç: Zararda ❌")
        else:
            print("Sonuç: Başabaş ➖")
