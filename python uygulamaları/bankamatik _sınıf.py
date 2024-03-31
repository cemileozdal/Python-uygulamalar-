class BankaHesabi:
    def __init__(self,hesap_sahibi,hesap_no,bakiye):
        self.hesap_sahibi = hesap_sahibi
        self.hesap_no = hesap_no
        self.bakiye = bakiye 

    def para_yatir(self,YatirilacakPara):
        self.bakiye += YatirilacakPara
        print(f"Toplam bakiye: {self.bakiye}")

    def para_cek(self,CekilecekPara):
        if self.bakiye >= CekilecekPara:
            self.bakiye -= CekilecekPara
            print(f"kalan bakiye: {bakiye}")
            return
        print("bakiyeniz yetersiz.")
            
    def bakiye_sorgula(self):
        print(f"Bakiyede bulunan para miktari: {bakiye}")

def menu_göster():
    print("1. para yatir.")
    print("2. para cek.")
    print("3. bakiye sorgula.")
    print('4. Çikiş ')

if __name__ =="__main__":
    hesap_sahibi = input("Ad ve Soyad: ")
    hesap_no = input("Hesap Numarasi: ")
    bakiye = int(input("Heaspta bulunan para: "))

    Hesap = BankaHesabi(hesap_sahibi,hesap_no,bakiye)

    while True:
        menu_göster()

        secim = input("Yapmak istediğiniz işlemi giriniz: ")

        if secim == "1":
            YatiralacakPara = float(input("Yatirmak istediğiniz tutari giriniz: "))
            Hesap.para_yatir(YatiralacakPara)
        elif secim == "2":
            Cekilecekpara = float(input("Çekmek istediğiniz tutari giriniz: "))
            Hesap.para_cek(Cekilecekpara)
        elif secim == "3":
            Hesap.bakiye_sorgula()
        elif secim == "4":
            print("Çikiş yapiliyor...")
            break
        else:
            print("Hatali işlem girdiniz. Lütfen tekrar deneyiniz!")
            continue            

  