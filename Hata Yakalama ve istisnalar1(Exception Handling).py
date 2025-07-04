def bolme_islemi():
    try:
        sayi1 = int(input("Bölünecek sayıyı girin: "))
        sayi2 = int(input("Bölen sayıyı girin: "))
        sonuc = sayi1 / sayi2
    except ZeroDivisionError:
        print("HATA: Bir sayıyı sıfıra bölemezsiniz.")
    except ValueError:
        print("HATA: Lütfen sadece sayı girin.")
    else:
        print("Sonuç:", sonuc)
    finally:
        print("İşlem tamamlandı (başarılı veya hatalı).")

bolme_islemi()
