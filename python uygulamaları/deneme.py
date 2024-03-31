import pandas as pd


class kitaplik():
    def menu_göster():
        print("1. Kitap ekle")
        print("2. Kitap sil ")
        print("3.Kitaplari göster ")
        print('4. Çikiş ')


    def __init__(self):
        self.kitap = pd.DataFrame(columns=['Kitap Adi', 'Kitap Yazari', 'Cilt'])

    def kitap_ekle(self,Kitap_Adi, Kitap_Yazari, Cilt):
        
        yeni_kitap = pd.DataFrame([[Kitap_Adi, Kitap_Yazari, Cilt]], columns=['Kitap Adi', 'Kitap Yazari', 'Cilt'])
        self.kitap = pd.concat([self.kitap, yeni_kitap], ignore_index=True)
      


    def kitap_sil(self,Kitap_Adi):
        self.kitap = self.kitap[self.kitap['Kitap Adi'] != Kitap_Adi]
        print(f"{Kitap_Adi} adli kitap kitapliktan kaldirildi.")

    def göster(self):
        print(self.kitap)


    if __name__ =='__main__' :
        kitaplik = kitaplik()
        while True:
            
            secim = input("Yapmak istediğiniz işlemi giriniz: ")

            if secim == "1":
                Kitap_Adi = input("Eklemek istediğiniz kitap adini giriniz: ")
                Kitap_yazari = input("Eklemek istediğiniz kitabin yazarini giriniz:  ")
                Cilt = input("Eklemek istediğiniz kitabin cildini giriniz: ")
                


            