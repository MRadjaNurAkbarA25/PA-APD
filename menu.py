from function import *
from petugas import *
from warga import *
from data import akun

def menu_petugas(username):
    while True:
        clear()
        print(f'''=== MENU PETUGAS ({username}) ===
1. Lihat laporan
2. Buat Laporan
3. Ubah Data laporan
4. Logout
5. Keluar Program''')

        pilihan = pilih_opsi('Pilih menu: ', ['1', '2', '3', '4', '5'])

        if pilihan == '1':
            clear()
            print('=== DAFTAR LAPORAN ===')
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
            return

def menu_warga(username):
    while True:
        clear()
        print(f'''=== MENU WARGA ({username}) ===
1. Lihat laporan saya
2. Buat laporan baru
3. Ubah Data Laporan
4. Logout''')

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
            return
