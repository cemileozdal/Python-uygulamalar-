def ucus_takip():
    while True:

        print("1. Uçuşlari listele: ")
        print("2. Ucuş ekle: ")
        print("3. Uçuş sil: ")
        print("4. Çikiş")

        seçenek = input("Yapmak istediğiniz işlemi seçiniz: ")

        if seçenek == "1":
            ucuslari_listele()
        elif seçenek == "2":
            ucus_ekle()
        elif seçenek == "3": 
            ucus_sil()
        elif seçenek == "4":
            print("Çikiş yapiliyor.")
            break
        else:
            print("Geçersiz bir seçim yaptiniz. Tekrar deneyiniz.")

def ucuslari_listele():
    with open('ucuslar.txt','r') as file: 
        ucuslar = file.readlines()

    for ucus in ucuslar:
        ucus_bilgileri = ucus.split(',')
        ucus_no = ucus_bilgileri[0]
        kalkis = ucus_bilgileri[1]
        varis = ucus_bilgileri[2]
        kalkis_zamani = ucus_bilgileri[3]
        varis_zamani = ucus_bilgileri[4].strip()


        print(f"Uçuş No: {ucus_no}")
        print(f"Kalkiş Yeri: {kalkis}")
        print(f"Variş Yeri: {varis}")
        print(f"Kalkiş Zamani: {kalkis_zamani}")
        print(f"Variş Zamani: {varis_zamani}\n")

def ucus_ekle():

    ucus_no = input("Ucus no ekle: ")
    kalkis = input("Kalkiş yeri ekle: ")
    varis = input("Varis yeri ekle: ")
    kalkis_zamani = input("Kalkiş zamani ekle: ")
    varis_zamani = input("Variş zamani ekle: ")

    ucus_bilgisi = print(f"{ucus_no}, {kalkis}, {varis}, {kalkis_zamani}, {varis_zamani}\n")

    with open('ucuslar.txt','a') as file:
        file.write(ucus_bilgisi)

    print("Ucus başariyle kaydedildi")

def ucus_sil():
    ucus_no = input("Silmek istediğiniz uçuş numarasini giriniz: ")

    with open('ucuslar.txt','r') as file:
        ucuslar = file.readlines()

    with open('ucuslar.txt','w') as file:

        for ucus in ucuslar:
            ucus_bilgileri = ucus.split(',')
            
            if ucus_bilgileri[0] != ucus_no:
                file.write(ucus)
        
ucus_takip()