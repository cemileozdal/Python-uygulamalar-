import numpy as np

def matris_oluştur(satir, sutun, min_deger=0, max_deger=10,):
    return np.random.randint(min_deger,max_deger + 1, size=(satir,sutun))

def matris_toplamlari(matris):
    return np.sum(matris)

def matris_transpoz(matris):
    return np.transpose(matris)

def matris_carpimlari(matris1,matris2):
    return np.dot(matris1,matris2)

if __name__ == "__main__" :

    satir_sayisi = int(input("Satir sayisi giriniz: "))
    sutun_sayisi = int(input("Sutun sayisi giriniz: "))

    matris1 = matris_oluştur(satir_sayisi,sutun_sayisi)
    matris2 = matris_oluştur(satir_sayisi,sutun_sayisi)

    print(f"Matris1:\n {matris1}")
    print(f"Matris2:\n {matris2}")

    toplam = matris_toplamlari(matris1)
    print(f"Matris1 in toplami: {toplam}")
    toplam = matris_toplamlari(matris2)
    print(f"Matris2 nin toplamlari: {toplam}")

    transpoz = matris_transpoz(matris1)
    print(f"Matris1 in transpozu:\n {transpoz}")
    transpoz = matris_transpoz(matris2)
    print(f"Matris2 in transpozu:\n {transpoz}")

    carpim = matris_carpimlari(matris1,matris2)
    print(f"Matris çarpimi:\n {carpim}")