from function import *
from petugas import *
from warga import *
from ketua import *
from auth import *
from data import akun
from colorama import Fore, Style, init
init(autoreset=True)

def menu_petugas(username):
    while True:
        clear()
        print(f'''=== MENU PETUGAS ({username}) ===
1. Lihat laporan
2. Buat Laporan
3. Ubah Data laporan
4. Hapus Laporan
5. Logout
6. Keluar Program''')

        pilihan = pilih_opsi('Pilih menu: ', ['1', '2', '3', '4', '5', '6'])

        if pilihan == '1':
            clear()
            print(Fore.CYAN + Style.BRIGHT + '=== DAFTAR LAPORAN ===')
            print(tabel())
            input('\nEnter untuk kembali...')
        
        elif pilihan == '2':
            clear()
            buat_laporan(username)
            input('\nEnter untuk kembali...')
            
        elif pilihan == '3':
            clear()
            ubah_data_petugas()
            input('\nEnter untuk kembali...')

        elif pilihan == '4':
            clear()
            hapus_laporan()
            input('\nEnter untuk kembali...')
            
        elif pilihan == '5':
            clear()
            return
            
        elif pilihan == '6':
            clear()
            simpan_semua()
            print(Fore.CYAN + Style.BRIGHT + 'Terima kasih telah menggunakan LAPOR AJA!!!')
            delay()
            exit() 

def menu_warga(username):
    while True:
        clear()
        print(f'''=== MENU WARGA ({username}) ===
1. Lihat laporan saya
2. Buat laporan baru
3. Ubah Data Laporan
4. Logout
5. Keluar Program''')

        pilihan = pilih_opsi('Pilih menu: ', ['1', '2', '3','4'])

        if pilihan == '1':
            clear()
            lihat_laporan_spesifik(username)
            input('\nEnter untuk kembali...')

        elif pilihan == '2':
            clear()
            buat_laporan(username)
            input('\nEnter untuk kembali...')
            
        elif pilihan == '3':
            clear()
            ubah_laporan_warga(username)
            input('\nEnter untuk kembali...')

        elif pilihan == '4':
            clear()
            return
        
        elif pilihan == '5':
            clear()
            simpan_semua()
            print(Fore.CYAN + Style.BRIGHT + 
'Terima kasih telah menggunakan LAPOR AJA!!!')
            delay()
            exit() 

def menu_ketua_rt(username):
    while True:
        clear()
        print(f'''=== MENU KETUA RT ({username}) ===
1. Lihat Semua Laporan
2. Hapus Laporan
3. Lihat Statistik Status
4. Ekspor Laporan ke CSV
5. Lihat Daftar Akun
6. Ubah Role Akun
7. Hapus Akun
8. Log-out
9. Keluar Program''')
        
        pilihan = pilih_opsi('Pilih: ', ['1','2','3','4','5','6','7','8', '9'])
        if pilihan == '1':
            clear()
            print(tabel())
            input('\nEnter untuk kembali...')
        elif pilihan == '2':
            clear()
            hapus_laporan()
            input('\nEnter untuk kembali...')
        elif pilihan == '3':
            clear()
            statistik()
            input('\nEnter untuk kembali...')
        elif pilihan == '4':
            clear()
            ekspor()
            input('\nEnter untuk kembali...')
        elif pilihan == '5':
            clear()
            print('Daftar Akun')
            print(tabul())
            input('\nEnter untuk kembali...')
        elif pilihan == '6':
            clear()
            ubah_role()
        elif pilihan == '7':
            clear()
            hapus_akun(username)
        elif pilihan == '8':
            clear()
            return
        elif pilihan == '9':
            clear()
            simpan_semua()
            print(Fore.CYAN + Style.BRIGHT + 'Terima kasih telah menggunakan LAPOR AJA!!!')
            delay()
            exit()