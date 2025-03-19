

import qrcode
import random

def generate_qr(data):
    qr = qrcode.make(data)
    qr.show()

def abonman_giris():
    print("Abonman karti dogrulandi, giris yapabilirsiniz.")

def nakit_odeme():
    print("Nakit odeme alindi, giris yapabilirsiniz.")

def gunubirlik_kart():
    print("Gunubirlik kart dogrulandi, giris yapabilirsiniz.")

def qr_dogrulama():
    qr_data = str(random.randint(1000, 9999))
    print(f"QR Kodunuz: {qr_data}")
    generate_qr(qr_data)
    user_input = input("QR kodu giriniz: ")
    if user_input == qr_data:
        print("QR dogrulandi, giris yapabilirsiniz.")
    else:
        print("QR dogrulama basarisiz.")

def sms_hatirlatma():
    print("Kart sureniz bitmek uzere! Lutfen yenileyiniz.")

def giris_sistemi():
    while True:
        print("\n--- Oyun Parki Giris Sistemi ---")
        print("1. Abonman Girisi")
        print("2. Nakit odeme")
        print("3. Kart ile Gunubirlik Giris")
        print("4. QR Kart Dogrulama")
        print("5. Kart Suresi Hatirlatma")
        print("6. cikis")
        
        secim = input("Seciminizi yapin: ")
        
        if secim == "1":
            abonman_giris()
        elif secim == "2":
            nakit_odeme()
        elif secim == "3":
            gunubirlik_kart()
        elif secim == "4":
            qr_dogrulama()
        elif secim == "5":
            sms_hatirlatma()
        elif secim == "6":
            print("cikis yapiliyor...")
            break
        else:
            print("Gecersiz secim, tekrar deneyin.")

giris_sistemi()

