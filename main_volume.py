# main
def main():
    pilih = input('Pilih Volume Bangun Ruang Apa? \n1. Kubus\n2. Balok\n3. Kerucut\n4. Bola \n5. Tabung\n6. Limas Segitiga\n7. Prisma Segitiga\n')
    if pilih in ["Kubus","kubus","1"]:
        print("\nVolume Kubus Adalah:  ", kubus().volume_kubus())
    elif pilih in ["Balok","balok","2"]:
        print("\nVolume Balok Adalah:  ", balok().Volume_balok())
    elif pilih in ["Kerucut","kerucut","3"]:
        print("\nVolume Kerucut Adalah:  ", VolKerucut().volume())    
    elif pilih in ["Bola","bola","4"]:
        print("\nVolume Bola Adalah:  ", VolBola().volume())  
    elif pilih in ["Tabung","tabung","5"]:
        print("\nVolume Tabung Adalah:  ", Tabung().volumeTabung())  
    elif pilih in ["Limas Segitiga","limas segitiga","6"]:
        print("\nVolume Limas Segitiga Adalah:  ", LimasSegitiga().volumeLimasSegitiga()) 
    elif pilih in ["Prisma Segitiga","prisma segitiga","7"]:
        print("\nVolume Prisma Segitiga Adalah:  ", prisma_segitiga().Volume_prisma_segitiga()) 
    else:
        print("Masukkan inputan yang benar ")

# run program
if __name__ == "__main__":
    main()