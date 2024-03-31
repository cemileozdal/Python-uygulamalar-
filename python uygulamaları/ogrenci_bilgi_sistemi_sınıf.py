def menü_göster():
    print('1. Öğrenci bilgisi ekleyiniz')
    print('2. Öğrenci bilgisi siliniz ')
    print('3. Öğrenci bilgilerini göster ')
    print('4. Öğrenci sinav sonuçlarina eriş')
    print('5. Çikiş ')

def öğrenci_ekle(öğrenciler):

    ad = input("Öğrencinin adini giriniz: ")
    soyad = input("Öğrencinin soyadini giriniz: ")
    no = input("öğrencini okul numarasini giriniz: ")
    sinav1 = input('Öğrencinin 1. sinav notunu giriniz: ')
    sinav2 = input('Öğrencinin 2. sinav notunu giriniz: ')

    öğrenci = {"Ad": ad , "Soyad": soyad , "no": no , "Sinav Sonuçlari": (sinav1,sinav2)}
    öğrenciler.append(öğrenci)
    print(öğrenci)

def öğrenci_sil(öğrenciler):
    no = input("öğrencini okul numarasini giriniz: ")

    for öğrenci in öğrenciler :
        if öğrenci['no'] == no:
            öğrenciler.remove(öğrenci)
            print("Öğrenciyi silme işlemi başariyla gerçekleştirilmiştir.")
            return
         
    print("Girilen bilgilere ait öğrenci bulunamiyor.")

def öğrenci_bilgileri(öğrenciler):
    no = input("Öğrencinin numarasiniz giriniz: ")

    for öğrenci in öğrenciler :
        if öğrenci["no"] == no:

            print("Ad:" + öğrenci["Ad"])
            print("Soyad:" + öğrenci["Soyad"])
            print("no:" + öğrenci["no"])
            return

    print("Girilen bilgilere ait öğrenci bulunamiyor.")

def sinav_sonuçlari(öğrenciler):
    no = input("Öğrencinin numarasini giriniz: ")

    for öğrenci in öğrenciler :
        if öğrenci["no"] == no :

            print("öğrencinin sinav sonuçlari: ")
            
            for i,sonuç in enumerate(öğrenci["Sinav Sonuçlari"]):
                print('{}. sinav sonucu {}'.format(i+1,sonuç))
                return

        print("Girilen bilgilere ait öğrenci bulunamiyor.")

def menu_kapat(öğrenciler):

    print("Programdan çikiş yapiliyor.")

def ana_menu():
    öğrenciler = []

    while True:
        menü_göster()
        seçenek = int(input('yapilacak işlemi seçiniz(1-5): '))

        if seçenek == 1:
            öğrenci_ekle(öğrenciler)
        elif seçenek == 2 :
            öğrenci_sil(öğrenciler)
        elif seçenek == 3 :
            öğrenci_bilgileri(öğrenciler)
        elif seçenek == 4 :
            sinav_sonuçlari(öğrenciler)
        elif seçenek == 5 :
            menu_kapat(öğrenciler)
        else:
            print('Geçersiz bir seçim yaptiniz. Lütfen tekrar deneyiniz.')

ana_menu()
        


    



       

           
