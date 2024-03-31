ad = input("Ad ve Soyad: ")
no = input("Hesap Numarasi: ")
bakiye = int(input("Heaspta bulunan para: "))

hesap = {"hesap sahibinin adi" : ad , "Hesap Numarasi" : no , "Hesaptaki para" : bakiye}
print(hesap)

while True:
    print("1. para yatir.")
    print("2. para cek.")
    print("3. bakiye sorgula.")
    print('4. Çikiş ')
    
    secenek = int(input("yapilacak islemi seciniz (1-4): "))

    if secenek == 1 :
        YatiralacakPara = int(input("Yatirilacak para miktarini giriniz: "))
        bakiye += YatiralacakPara
        print(f"Toplam bakiye: {bakiye}")
        

    elif secenek == 2 :
        CekilecekPara = int(input("Cekilecek para miktarini giriniz: "))
        if bakiye >= CekilecekPara :
            bakiye -= CekilecekPara
            print(f"kalan tutar: {bakiye}")
            break
        else:     
            print("Bakiye yetersiz")

    elif secenek == 3 :
        print(f"Bakiyede bulunan para miktari: {bakiye} ")

    elif secenek == 4 :
        print("çikiş yapiliyor")
        break

    else :
        print("Geçersiz bir seçim yaptiniz. Lütfen tekrar deneyiniz.")
        continue
     






  