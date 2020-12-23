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