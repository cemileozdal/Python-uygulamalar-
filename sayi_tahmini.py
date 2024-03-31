import random
sayi = random.randint(1,100)
hak = int(input('kaç hak kullanmak istersiniz: '))
can = hak
sayaç = 0

while hak > 0:
    hak -= 1
    sayaç += 1
    tahmin = int(input('tahmin: '))
    if sayi == tahmin:
        print(f'tebrikler {sayaç}. defada doğru bildiniz : {100-(100/can)*(sayaç-1)}')
        break

    elif sayi > tahmin :
        print('yukarı')
    
    else:
        print('aşağı')

    if hak == 0 :
        print(f'hakkınız bitti tutulan sayı {sayi}')
