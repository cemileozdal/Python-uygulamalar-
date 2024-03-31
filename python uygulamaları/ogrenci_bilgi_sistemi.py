öğrenciler = []

while True :
    print('1. Öğrenci bilgisi ekleyiniz')
    print('2. Öğrenci bilgisi siliniz ')
    print('3. Öğrenci bilgilerini göster ')
    print('4. Öğrenci sinav sonuçlarina eriş')
    print('5. Çikiş ')
    
    seçenek = int(input('yapilacak işlemi seçiniz(1-5): '))

    if seçenek == 1 :
        seçenek = int(input('yapilacak işlemi seçiniz(1-5): '))

    if seçenek == 1 :
        ad = input('Öğrencinin adini giriniz: ')
        soyad = input('Öğrencinin soyadini giriniz: ')
        no = input('Öğrencinin okul numarasini giriniz: ')
        sinav1 = int(input('Öğrencinin 1. sinav notunu giriniz: '))
        sinav2 = int(input('Öğrencinin 2. sinav notunu giriniz: '))

        öğrenci = {'ad' : ad,'soyad' : soyad, 'no' : no, 'Sinav Sonuçlari' : (sinav1 , sinav2)}
        öğrenciler.append(öğrenci)
        print(öğrenci)

    elif seçenek == 2 :
        no = input('Öğrencinin okul numarasini giriniz: ')

        for öğrenci in öğrenciler :
            if öğrenci['no'] == no :
                öğrenciler.remove(öğrenci)
                print('Öğrenci silme işi başari ile gerçekleşti.')
                break

        else :
            print('Girilen bilgiye ait öğrenci bulunamiyor.')
            break

    elif seçenek == 3 :
        no = input('Öğrencinin okul numarasini giriniz: ')

        for öğrenci in öğrenciler :
            if öğrenci['no'] == no :
                print('Ad:' + öğrenci['ad'])
                print('Soyad:' + öğrenci['soyad'])
                print('Okul Numarasi:' + öğrenci['no'])
                print('Sinav1:' + öğrenci['sinav1'])
                print('Sinav2:' + öğrenci['sinav2'])
                break
        else :
            print('Girilen bilgilere ait öğrenci bulunamiyor')

    elif seçenek == 4 :
        no = input('Öğrencinin okul numarasini giriniz: ')

        for öğrenci in öğrenciler :
            if öğrenci['no'] == no :
                print('Öğrencinin sinav sonuçlari:')
                for i,sonuç in enumerate(öğrenci['Sinav Sonuçlari']):
                    print('{}. sinav notu: {}'.format(i+1,sonuç))
            break
        else :
            print('Girilen bilgilere ait öğrenci bulunamiyor.')       

    elif seçenek == 5 :
        print('Programdan çikiş yapiliyor.')
        break   

    else : 
        print('Geçersiz bir seçim yaptiniz. Lütfen tekrar deneyiniz.')

    
