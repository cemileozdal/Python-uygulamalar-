class Personel():
    mesai = "9 -18"
    sirket = "AS-AS"
    def __init__(self,isim,maas,yetenek,rutbe): 
        print("Yeni personel oluşturuldu",isim)
        self.isim = isim
        self.yetenek = yetenek
        self.maas = maas
        self.gunsayisi = 0
        self.rutbe = rutbe
    def calıs(self): 
        print(self.isim,"çalışıyor")
        self.gunsayisi+=1
    def terfi(self): 
        print("Tebrikler ",self.isim,"Terfi aldın")
        self.maas+=200
    def bilgileriGoster(self):
        print("*-"*20)
        print("Personelin ismi: ",self.isim)
        print("Personelin yetenekleri: ",self.yetenek)
        print("Personelin maaşı: ",self.maas)
        print("Personelin toplam gün sayısı",self.gunsayisi)
        print("Personelin konumu: ",self.rutbe)
        print("*-"*20)

class Yonetici(Personel):
    def terfi(self):
        self.maas+=523
   
    def __init__(self,isim,maas,yetenek,rutbe,yonetimBecerisi):
        super().__init__(isim,maas,yetenek,rutbe)
       
        self.yonetimBecerisi = yonetimBecerisi
    def bilgileriGoster(self):
        super().bilgileriGoster()
        print("Yonetim becerisi: ",self.yonetimBecerisi)
        print("*-"*20)
    def calıs(self):
        super().calıs()
        self.yonetimBecerisi+= 0.5
        print("Yönetim becerisi artırıldı.")


asim = Personel("asim",1600,"linux,java,pentest","Mühendis") 
emel = Yonetici("Emel",2000,"İnsan kaynakları","Yönetici",50)
asim.calıs()
asim.bilgileriGoster()
emel.calıs()
emel.bilgileriGoster()
