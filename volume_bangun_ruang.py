"""
Afifah 
Anisa
Ibnu
Ragil

VOLUME BANGUN RUANG

"""

class kubus:
    def __init__(self):
        self.sisi = float(input("Masukkan sisi Kubus: "))        
    
    def volume_kubus(self):
        self.luas_kubus = self.sisi**3
        return self.luas_kubus

class balok:
    def __init__(self):
        self.panjang = float(input("Masukkan panjang balok: "))  
        self.lebar = float(input("Masukkan lebar balok: "))  
        self.tinggi = float(input("Masukkan tinggi balok: "))  

    def Volume_balok(self):
        self.luas_balok = self.panjang*self.lebar*self.tinggi
        return self.luas_balok
    
class prisma_segitiga:
    def __init__(self):
        self.alas = float(input("Masukkan alas prisma: "))  
        self.tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))  
        self.tinggi_prisma = float(input("Masukkan tinggi prisma: "))  

    def Volume_prisma_segitiga(self):
        self.Volume_prisma_segitiga = (self.alas*self.tinggi_segitiga)/2*self.tinggi_prisma
        return self.Volume_prisma_segitiga


class VolKerucut:
    def __init__(self):
        self.radius = float(input("Masukkan radius kerucut: "))
        self.tinggi = float(input("Masukkan tinggi kerucut: "))

    def volume(self):
        phi = 3.14
        return (phi*(self.radius**2)*self.tinggi)/3

class VolBola:
    def __init__(self):
        self.radius = float(input("Masukkan radius bola:"))

    def volume(self):
        phi = 3.14
        return (4*phi*(self.radius**3))/3
        
#class untuk menghitung voume tabung
class Tabung:
    #inisialisasi atribut
    def __init__(self):
        self.jari_jari = float(input("Masukkan jari-jari tabung: "))        
        self.tinggi = float(input("Masukkan tinggi tabung: ")) 

    #menghitung volume tabung
    def volumeTabung(self):
        self.volume = (22/7)*(self.jari_jari*self.jari_jari)*self.tinggi
        return self.volume

#class untuk menghitung limas segitiga sama sisi
class LimasSegitiga:
    #inisialisasi atribut
    def __init__(self):
        self.tinggi = float(input("Masukkan tinggi limas: "))  
        self.alas_segitiga = float(input("Masukkan alas segitiga: "))  
        self.tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))  

    #menghitung volume limas segitiga sama sisi
    def volumeLimasSegitiga(self):
        self.volume = (1/3)*(self.alas_segitiga*self.tinggi_segitiga/2)*self.tinggi
        return self.volume
