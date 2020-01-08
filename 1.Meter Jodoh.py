import random
import datetime

print("===Selamat Datang di Pengukur Jodoh===")
print("===Jangan Menyesal Dengan Hasilnya===")
tanggal_saat_ini = datetime.date.today( )
print(tanggal_saat_ini)

ulang = True
while ulang:
    cowok = input("Masukkan Nama Cowok: ")
    umurcowok = input("Masukkan Umur: ")
    ttlcowok = input("Masukkan TTL Anda: ")
    hobicowok = input("Masukkan Hobi Anda: ")
    print("==============================")
    cewek = input("Masukkan Nama Cewek: ")
    umurcewek = input("Masukkan Umur: ")
    ttlcewek = input("Masukkan TTL Anda: ")
    hobicewek = input("Masukkan Hobi Anda: ")

    print("=========Biodata Anda=========")
    print("Nama Cowok: ", cowok)
    print("Umur Cowok: ",umurcowok)
    print("TTL Cowok: ",ttlcowok)
    print("Hobi Cowok: ",hobicowok)
    print("==============================")
    print("Nama Cewek: ", cewek)
    print("Umur Cewek: ",umurcewek)
    print("TTL Cewek: ",ttlcewek)
    print("Hobi Cewek: ",hobicewek)
    confirm = input("Apakah nama sudah benar? y/n: ")
    if confirm=='y':
        ulang = False

cocok = random.randrange(0,100)
print('Kecocokan ', cocok, '%')

if cocok>80:
    print('Nikah Daaaahh.....')
elif cocok>60:
    print('Coba Dipikir Lagi.....')
elif cocok>40:
    print('Yakin.....')
elif cocok>20:
    print('Cari Lagi.....')
else:
    print('Putusin Aja.....')

print('Terus Berusaha dan Berdoa Ya.....')
