# Özel hata sınıfı tanımı
class NegatifSayiHatasi(Exception):
    def __init__(self, sayi):
        super().__init__(f"Negatif sayı hatası: {sayi} geçersizdir.")
        self.sayi = sayi

def karekok_al(sayi):
    if sayi < 0:
        raise NegatifSayiHatasi(sayi)
    return sayi ** 0.5

def program():
    try:
        giris = float(input("Karekökünü almak istediğiniz sayıyı girin: "))
        sonuc = karekok_al(giris)
    except NegatifSayiHatasi as hata:
        print("ÖZEL HATA:", hata)
    except Exception as e:
        print("GENEL HATA:", e)
    else:
        print("Sonuç:", sonuc)
    finally:
        print("Program sonlandı.")

program()
