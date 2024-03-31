import random 
def oyun():
    result = ["taş", "kagit", "makas"]
    rakip = 0
    oyuncu = 0

    while True:
        secenek = input("taş, kagit ya da makas ?  (çikiş icin e tusuna basiniz.): ")

        if secenek == 'e':
            print("Cikis yapiliyor.")
            break

        if secenek not in result :
            print("Yanlis secim yapildi lütfen tekrar deneyiniz.")
            continue

        Rakip = random.choice(result)
        print(f"Rakip: {Rakip}")

        if secenek == Rakip:
            print("Berabere.")

        elif (secenek == "taş" and Rakip == "makas") or (secenek == "kagit" and Rakip == "taş") or (secenek == "makas" and Rakip == "kagit"):
            oyuncu += 1
            print(f"Tebrikler kazandiniz. Oyuncu : {oyuncu} Rakip: {rakip}")

        else: 
            rakip += 1    
            print(f"Rakip kazandi. Oyuncu: {oyuncu} Rakip: {rakip}")    

        if oyuncu == 3 or rakip  == 3:

            if oyuncu == 3:
                print("Oyun bitti oyuncu kazandi.")

            else:
                print("Oyun bitti rakip kazandi. ")

oyun()