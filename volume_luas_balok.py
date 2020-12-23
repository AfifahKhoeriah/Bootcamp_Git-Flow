# Ibnu Dafa

print('aplikasi menghitung :\n1. luas\n2. volume')
pilihan = int(input('ayo dipilih : '))
 
def luas(p,l,t):
    L = 2 * ( (p*l) + (p*t) + (l*t))
    return L
 
def volume(p,l,t):
    V = p * l * t
    return V
 
 
if pilihan == 1:
    p = int(input('panjang balok: '))
    l = int(input('lebar balok: '))
    t = int(input('tinggi balok: '))
    luas(p,l,t)
    print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{}\nMempunyai luas:{}'.format(p,l,t, luas(p,l,t)))
 
elif pilihan == 2:
    p = int(input(' panjang balok: '))
    l = int(input(' lebar balok: '))
    t = int(input(' tinggi balok: '))
    volume(p,l,t)
    print('Jadi balok dengan ukuran panjang:{}, lebar:{}, tinggi:{}\nMempunyai volume:{}'.format(p,l,t, volume(p,l,t)))

 
else:
    print('yang tersedia ada dua pilihan loh , yaitu luas dan volume :D')