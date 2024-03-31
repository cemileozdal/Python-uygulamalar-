from ucus import Ucus
from yolcu import Yolcu

ucus_listesi =[]
yolcu_listesi = []

def yeni_ucus():
    ucus_no = input("Ucus numarasini giriniz: ")
    kalkis_yeri = input("Kalakis yerini giriniz: ")
    varis_yeri = input("Varis yerini giriniz: ")
    kalkis_tarihi = input("Kalkis tarihini giriniz (gün-ay-yil saat-dakika): ")
    varis_tarihi = input("Varis tarihini giriniz (gün-ay-yil saat-dakika): ")
    
    ucus = Ucus(ucus_no ,kalkis_yeri,varis_yeri,kalkis_tarihi,varis_tarihi)
    ucus_listesi.append(ucus)
    print("Yeni ucus oluşturuldu.")

def yolcu_ekle():
    ad = input("Yolcunun adini giriniz: ")
    soyad = input("Yolcunun soyadini giriniz: ")
    koltuk_no = input("Koltuk numarasini giriniz: ")

    yolcu = Yolcu(ad,soyad,koltuk_no)
    yolcu_listesi.append(yolcu)
    print(f"Yolcu listesi: {yolcu}")

    for i, ucus in enumerate(ucus_listesi):
        print(i+1, "-", ucus.ucus_no, "Kalkis yeri: ", ucus.kalkis_yeri, "Kalkis tarihi: ", ucus.kalkis_tarihi)

    ucus_i = int(input("Kaç numarali uçusa eklemek istersiniz: "))
    ucus = ucus_listesi[ucus_i-1]
    ucus.yolcu_ekle(yolcu)

def yolcu_sil():
    print("Ucus listesi: ")
    for i,ucus in enumerate(ucus_listesi):
        print(i+1, "-", ucus.ucus_no, "Kalkis yeri: ", ucus.kalkis_yeri, "Kalkis tarihi: ",ucus.kalkis_tarihi)
        ucus_i = int(input("Kaç numarali ucustan yolcu silmek istersiniz: "))
        ucus = ucus_listesi[ucus_i-1]

    print("Yolcu listesi: ")
    for i,yolcu in enumerate(ucus.yolcular):
        print(i+1, "-", ucus.ucus_no, "Kalkis yeri: ", ucus.kalkis_yeri, "Kalkis tarihi: ",ucus.kalkis_tarihi)
        yolcu_i = int(input("Kaç numarali yolcuyu silmek istersiniz: "))
        yolcu = ucus.yolcular[yolcu_i-1]
        ucus.yolcu_sil(yolcu)

def bilgiler():
    print("Uçuş Listesi:")
    for i,ucus in enumerate(ucus_listesi):
        print(i+1, "-", ucus.ucus_no, "Kalkiş Yeri: ", ucus.kalkis_yeri, "Variş Yeri: ", ucus.varis_yeri)

    ucus_i = int(input("Kaç numarali uçuşun bilgilerini görüntülemek istersiniz: "))
    ucus = ucus_listesi[ucus_i -1]
    ucus.bilgiler()


def menu_goster():
        print("Menü:")
        print("1. Yeni Uçuş Oluştur")
        print("2. Yolcu Ekle")
        print("3. Yolcu Sil")
        print("4. Uçuş Bilgilerini Görüntüle")
        print("5. Çikiş")
if __name__ == "__main__":
    while True:
        menu_goster()
        secim = input("Yapmak istediğiniz işlemi seçiniz: ")

        if secim == "1":
            yeni_ucus()
        elif secim == "2":
            yolcu_ekle()
        elif secim == "3":
            yolcu_sil()
        elif secim == "4":
            bilgiler()
        elif secim == "5":
            print("Çikiş yapiliyor.")
            break
        else:
            print("Tekrar deneyiniz!")
            continue                 