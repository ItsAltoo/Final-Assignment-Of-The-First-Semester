import os
from rich import print
from rich.style import Style

os.system('cls')


class DataMahasiswa:
    def __init__(self,fullName,nim):
        self.fullName = fullName
        self.nim = nim
    
    def tambah_mahasiswa(self):
        DB_NAME = 'db/data_mahasiswa.txt'
        with open(DB_NAME,'a') as file:
            dataMhs = f""" 
Nama lengkap :{self.fullName} 
NIM :{self.nim} 
            """
            file.write(dataMhs)
            print(30*'~','\n')
            print(f'Data anda telah di tambahkan ke dalam "{DB_NAME}"\n')
            print(30*'~','\n')

class Kehadiran:
    def __init__(self,name,absen):
        self.name = name
        self.absen = absen
    
    def tambahKehadiran(self):
        with open('db/kehadiran.txt','a')as file:
            absen_data = f""" 
{self.name},Telah {self.absen}            
            """
            file.write(absen_data)
            
    def cekKehadiran():
        with open('db/kehadiran.txt','r')as file:
            print(file.read())

class BacaData:
    def bacaData():
        with open('db/data_mahasiswa.txt','r')as file:
            print(file.read())

class HapusData:
    def hapusData():
        DATA = ['db/data_mahasiswa.txt','db/kehadiran.txt']
        
        while True:
            print(f""" 
1.Hapus Data ke-1 = {DATA[0]}
2.Hapus Data ke-2 = {DATA[1]}
3.Exit
              """)
            inpt = input("Pilih Opsi :")

            if inpt == '1': #jika inputan memilih opsi 1 program ini di jalankan
                choose = input(f'Ingin menghapus file {DATA[0]} (y/n)? :')
                if choose == 'y' or choose == 'Y':
                    try: 
                        print(f'Data {DATA[0]} telah di hapus !')
                        os.remove(DATA[0]) #os.remove untuk menghapus file
                    except:
                        print('Data tidak di temukan !')
                elif choose == 'n' or choose == 'N':
                    break
                else:
                    print("Tidak ada di opsi !")
            elif inpt == '2':
                choose = input(f'Ingin menghapus file {DATA[1]} (y/n)? :')
                if choose == 'y' or choose == 'Y':
                    try:
                        print(f'Data {DATA[1]} telah di hapus !') 
                        os.remove(DATA[1]) #os.remove untuk menghapus file
                    except:
                        print('Data tidak di temukan !')
                elif choose == 'n' or choose == 'N':
                    break
                else:
                    print("Tidak ada di opsi !")
            elif inpt == '3':
                break
            else:
                    print("Tidak ada di opsi !")



#Main
while True:
    print(f"""
          
            [blue]+====================================================+
            |  __        __     _                                |
            |  \ \      / /___ | |  ___  ___   _ __ ___    ___   |
            |   \ \ /\ / // _ \| | / __|/ _ \ | '_ ` _ \  / _ \  |
            |    \ V  V /|  __/| || (__| (_) || | | | | ||  __/  |
            |     \_/\_/  \___||_| \___|\___/ |_| |_| |_| \___|  |
            +====================================================+ [/blue]
.-=~=-.                                                                 .-=~=-.
(__  _)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(__  _)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
(_ ___)                                                                 (_ ___)
(__  _)                                                                 (__  _)
( _ __)                     1.[yellow]Tambah Data Mahasiswa[/yellow]                     ( _ __)
(__  _)                                                                 (__  _)
(_ ___)                     2.[yellow]Absen Kehadiran[/yellow]                           (_ ___)
(__  _)                                                                 (__  _)
( _ __)                     3.[green]Cek Kehadiran Mahasiswa[/green]                   ( _ __)
(__  _)                                                                 (__  _)
(_ ___)                     4.[green]Cek Data Mahasiswa[/green]                        (_ ___)
(__  _)                                                                 (__  _)
( _ __)                     5.[red]Hapus Data[/red]                                ( _ __)
(__  _)                                                                 (__  _)
(_ ___)                     6.[red]Exit Program[/red]                              (_ ___)
(__  _)                                                                 (__  _)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
(_ ___)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(_ ___)
`-._.-'                                                                 `-._.-'
""")

    opsi = int(input("Pilih Opsi :"))
    
    if opsi == 1:
        fullName = input('Masukkan Nama Lengkap Anda :')
        nim = input('Masukkan Nim Anda :')
        tambah_mhs = DataMahasiswa(fullName,nim)
        tambah_mhs.tambah_mahasiswa()
    elif opsi == 2:
        name = input('Masukkan Nama :')
        absen = input('Hadir/Tidak Hadir :')
        kehadiran = Kehadiran(name,absen)
        kehadiran.tambahKehadiran()
    elif opsi == 3:
        print(35*'~')
        Kehadiran.cekKehadiran()
        print(35*'~')
    elif opsi == 4:
        print(35*'~')
        BacaData.bacaData()
        print(35*'~')
    elif opsi == 5:
        HapusData.hapusData()
    elif opsi == 6:
        break
    else:
        print('Opsi Tidak Ada')

