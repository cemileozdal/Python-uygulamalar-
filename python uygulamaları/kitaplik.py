import pandas as pd

class kitaplik():
    def __init__(self):
        self.kitap = pd.DataFrame(columns=['Kitap adi','Kitap yazari','cilt'])
    
    def ekle(self,kitap_adi,kitap_yazari,cilt):
        yeni_kitap = pd.DataFrame([[kitap_adi, kitap_yazari, cilt]], columns=['Kitap adi', 'Kitap yazari', 'Cilt'])
        self.kitap = pd.concat([self.kitap, yeni_kitap], ignore_index=True)
        print(f"{kitap_adi} adli kitap başariyla kaydedildi.")

    def sil(self, kitap_adi):
        self.kitap = self.kitap[self.kitap['Kitap adi'] != kitap_Adi]
        print(f'{kitap_Adi} adli kitap başariyla silinmiştir.')

    def göster(self):

        print(self.kitap)

if __name__ == "__main__":
    kitaplik = kitaplik()
    
    while True:
        
        print("1. Kitap ekle")
        print("2. Kitap sil ")
        print("3.Kitaplari göster ")
        print('4. Çikiş ')

        secim = input("Yapmak istediğiniz işlemi giriniz: ")

        if secim == '1':
            kitap_Adi = input("Eklemek istediğiniz kitap adini giriniz: ")
            kitap_yazari = input("Eklemek istediğiniz kitabin yazarini giriniz:  ")
            cilt = input("Eklemek istediğiniz kitabin cildini giriniz: ")
            kitaplik.ekle(kitap_Adi, kitap_yazari, cilt)

        if secim == '2':
            kitap_Adi = input('Silmek istediğiniz kitabin adini giriniz: ')
            kitaplik.sil(kitap_Adi)

        if secim == '3':
            kitaplik.göster(kitap_Adi, kitap_yazari, cilt)
            