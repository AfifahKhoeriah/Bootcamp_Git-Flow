"""
Afifah Kho'eriah

Bangun Ruang Kubus dan balok
Luas Kubus = 6*sisi**2
Luas Prisma Segitiga = 2*(alas*tinggi_segitiga)/2 + (3*(tinggi_prisma*alas))

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