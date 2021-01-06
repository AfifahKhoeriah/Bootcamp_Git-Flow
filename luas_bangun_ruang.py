"""
Afifah 
Anisa
Ibnu
Ragil

LUAS BANGUN RUANG

"""

class kubus:
    def __init__(self):
        self.sisi = float(input("Masukkan sisi Kubus: "))        
    
    def luas_kubus(self):
        self.luas_kubus = 6*(self.sisi**2)
        return self.luas_kubus

class prisma_segitiga:
    def __init__(self):
        self.alas = float(input("Masukkan alas prisma: "))  
        self.tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))  
        self.tinggi_prisma = float(input("Masukkan tinggi prisma: "))  

    def luas_prisma_segitiga(self):
        self.luas_prisma_segitiga = 2*(self.alas*self.tinggi_segitiga)/2 + 3*(self.tinggi_prisma*self.alas)
        return self.luas_prisma_segitiga

class balok:
    def __init__(self):
        self.panjang = float(input("Masukkan panjang balok: "))  
        self.lebar = float(input("Masukkan lebar balok: "))  
        self.tinggi = float(input("Masukkan tinggi balok: "))  

    def luas_balok(self):
        self.luas_balok = 2*(self.panjang*self.lebar + self.panjang*self.tinggi + self.lebar*self.tinggi)
        return self.luas_balok
    
class LuasKerucut:
    def __init__(self):
        self.radius = float(input("Masukkan radius kerucut: "))
        self.pelukis = float(input("Masukkan garis pelukis kerucut: "))

    def luas(self):
        phi = 3.14
        return (phi*(self.radius))*(self.radius +self.pelukis)

class LuasBola:
    def __init__(self):
        self.radius = float(input("Masukkan radius bola: "))

    def luas(self):
        phi = 3.14
        return 4*phi*(self.radius**2)

#class untuk menghitung luas tabung
class Tabung:
    #inisialisasi atribut
    def __init__(self):
        self.jari_jari = float(input("Masukkan jari-jari tabung: "))        
        self.tinggi = float(input("Masukkan tinggi tabung: ")) 

    #menghitung luas tabung
    def luasTabung(self):
        self.luas = 2*(22/7)*self.jari_jari*(self.jari_jari+self.tinggi)
        return self.luas

#class untuk menghitung luas limas segitiga sama sisi
class LimasSegitiga:
    #inisialisasi atribut
    def __init__(self):
        self.alas_segitiga = float(input("Masukkan panjang alas segitiga: "))  
        self.tinggi_segitiga = float(input("Masukkan panjang tinggi segitiga: "))  
        self.rusuk = float(input("Masukkan rusuk tegak "))  

    #menghitung luas limas segitiga sama sisi
    def luasLimasSegitiga(self):
        self.luas = (self.alas_segitiga*self.tinggi_segitiga/2) + (self.rusuk*self.alas_segitiga/2)
        return self.luas
