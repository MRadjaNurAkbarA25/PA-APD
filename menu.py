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
            menu_filter_laporan()
        
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
            if logout():
                return
            
        elif pilihan == '6':
            keluar() 

def menu_warga(username):
    while True:
        clear()
        print(f'''=== MENU WARGA ({username}) ===
1. Lihat laporan saya
2. Buat laporan baru
3. Ubah Data Laporan
4. Logout
5. Keluar Program''')

        pilihan = pilih_opsi('Pilih menu: ', ['1', '2', '3','4', '5'])

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
            if logout():
                return
        
        elif pilihan == '5':
            keluar()

def menu_laporan(username):
    while True:
        clear()
        print('''=== MENU LAPORAN ===
1. Lihat Laporan
2. Buat Laporan
3. Ubah Data Laporan
4. Hapus Laporan
5. Kembali''')
        pilihan = pilih_opsi('Pilih: ', ['1', '2', '3', '4', '5'])
        
        if pilihan == '1':
            clear()
            menu_filter_laporan()
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
            return
        
def menu_akun(username):
    while True:
        clear()
        print('''=== MENU AKUN ===
1. Lihat daftar akun
2. Ubah Role Akun
3. Hapus Akun
4. Kembali''')
        pilihan = pilih_opsi('Pilih', ['1', '2', '3', '4'])
        
        if pilihan == '1':
            clear()
            print(Fore.CYAN + Style.BRIGHT + 'Daftar Akun')
            print(tabul())
            input('\nEnter untuk kembali...')
        elif pilihan == '2':
            clear()
            ubah_role()
        elif pilihan == '3':
            clear()
            hapus_akun(username)
            input('\nEnter untuk kembali...')
        elif pilihan == '4':
            clear()
            return

def menu_lainnya():
    while True:
        clear()
        print('''=== MENU AKUN ===
1. Lihat statistik laporan
2. Ekspor laporan ke csv
3. Kembali
''')
        pilihan = pilih_opsi('Pilih: ', ['1', '2', '3'])
        
        if pilihan == '1':
            clear()
            statistik()
            input('\nEnter untuk kembali...')
        elif pilihan == '2':
            clear()
            ekspor()
            input('\nEnter untuk kembali...')
        elif pilihan == '3':
            clear()
            return
        
def menu_ketua_rt(username):
    while True:
        clear()
        print(f'''=== MENU KETUA RT ({username}) ===
1. Menu Laporan
2. Menu Akun
3. Menu Lainnya
4. Log-out
5. Keluar Program''')
        
        pilihan = pilih_opsi('Pilih: ', ['1','2','3','4','5'])
        if pilihan == '1':
            clear()
            menu_laporan(username)
        elif pilihan == '2':
            clear()
            menu_akun(username)
        elif pilihan == '3':
            clear()
            menu_lainnya()
        elif pilihan == '4':
            clear()
            if logout():
                return    
        elif pilihan == '5':
            keluar()