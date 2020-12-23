"""
Afifah Kho'eriah

Bangun Ruang Kubus dan Prisma segitiga
Volume Kubus = s**3
Volume Prisma segitiga = (1/2*alas*tinggi_segitiga)*tinggi_prisma

"""

class kubus:
    def __init__(self):
        self.sisi = float(input("Masukkan sisi Kubus: "))        
    
    def volume_kubus(self):
        self.luas_kubus = self.sisi**3
        return self.luas_kubus

class prisma_segitiga:
    def __init__(self):
        self.alas = float(input("Masukkan alas prisma: "))  
        self.tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))  
        self.tinggi_prisma = float(input("Masukkan tinggi prisma: "))  

    def Volume_prisma_segitiga(self):
        self.Volume_prisma_segitiga = (self.alas*self.tinggi_segitiga)/2*self.tinggi_prisma
        return self.Volume_prisma_segitiga