# main
def main():
    pilih = input('Pilih Luas Bangun Ruang Apa? \n1. Kubus\n2. Balok\n3. Kerucut\n4. Bola \n5. Tabung\n6. Limas Segitiga\n7. Prisma Segitiga\n')
    if pilih in ["Kubus","kubus","1"]:
        print("\nLuas Kubus Adalah:  ", kubus().luas_kubus())
    elif pilih in ["Balok","balok","2"]:
        print("\nLuas Balok Adalah:  ", balok().luas_balok())
    elif pilih in ["Kerucut","kerucut","3"]:
        print("\nLuas Kerucut Adalah:  ", LuasKerucut().luas())    
    elif pilih in ["Bola","bola","4"]:
        print("\nLuas Bola Adalah:  ", LuasBola().luas())  
    elif pilih in ["Tabung","tabung","5"]:
        print("\nLuas Tabung Adalah:  ", Tabung().luasTabung())  
    elif pilih in ["Limas Segitiga","limas segitiga","6"]:
        print("\nLuas Limas Segitiga Adalah:  ", LimasSegitiga().luasLimasSegitiga()) 
    elif pilih in ["Prisma Segitiga","prisma segitiga","7"]:
        print("\nLuas Prisma Segitiga Adalah:  ", prisma_segitiga().luas_prisma_segitiga()) 
    else:
        print("Masukkan inputan yang benar ")

# run program
if __name__ == "__main__":
    main()