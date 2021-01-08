#Membuat class untuk Luas Kerucut
class LuasKerucut:
    def __init__(self):
        self.radius = float(input("Masukkan radius kerucut: "))
        self.pelukis = float(input("Masukkan garis pelukis kerucut: "))

    def luas(self):
        pi = 3.14
        return (pi*(self.radius))*(self.radius +self.pelukis)

#Membuat class untuk Luas Bola
class LuasBola:
    def __init__(self):
        self.radius = float(input("Masukkan radius bola: "))

    def luas(self):
        pi = 3.14
        return 4*pi*(self.radius**2)