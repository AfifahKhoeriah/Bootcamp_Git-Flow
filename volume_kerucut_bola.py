
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
