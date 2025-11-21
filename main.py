from function import *
from petugas import *
from warga import *
from data import akun
from menu import *
from auth import *

while True:
    clear()
    print('''=== SISTEM LAPORAN ===
1. Login
2. Keluar''')

    pilihan = pilih_opsi('Pilih menu: ', ['1', '2'])

    if pilihan == '1':
        username, role = login()
        if username:
            if role == 'petugas':
                menu_petugas(username)
            else:
                menu_warga(username)

    elif pilihan == '2':
        clear()
        print('Keluar dari program...')
        delay()
        break
